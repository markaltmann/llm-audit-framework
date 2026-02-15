"""Test execution and orchestration."""

import time
import uuid
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List

from .io import JSONLWriter
from .provider import LLMProvider


class TestRunner:
    """
    Orchestrates test case execution and result capture.
    """

    def __init__(
        self,
        provider: LLMProvider,
        output_dir: Path,
        verbose: bool = False,
    ):
        """
        Initialize test runner.

        Args:
            provider: LLM provider instance
            output_dir: Directory for output files
            verbose: Enable verbose logging
        """
        self.provider = provider
        self.output_dir = Path(output_dir)
        self.verbose = verbose
        self.writer = JSONLWriter(self.output_dir)

    def run_test_cases(
        self,
        test_cases: List[Dict[str, Any]],
        execution_config: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Run a list of test cases.

        Args:
            test_cases: List of test case dictionaries
            execution_config: Execution configuration from catalog

        Returns:
            Summary of execution results
        """
        execution_config = execution_config or {}
        results = {
            "total_executions": 0,
            "successful": 0,
            "failed": 0,
            "test_cases_run": len(test_cases),
        }

        for test_case in test_cases:
            if self.verbose:
                print(f"\nRunning test case: {test_case['id']}")

            try:
                case_results = self._run_single_test_case(test_case, execution_config)
                results["total_executions"] += case_results["executions"]
                results["successful"] += case_results["successful"]
                results["failed"] += case_results["failed"]
            except Exception as e:
                print(f"Error running test case {test_case['id']}: {e}")
                results["failed"] += 1

        return results

    def _run_single_test_case(
        self,
        test_case: Dict[str, Any],
        execution_config: Dict[str, Any],
    ) -> Dict[str, Any]:
        """
        Run a single test case (with repetitions if applicable).

        Args:
            test_case: Test case dictionary
            execution_config: Execution configuration

        Returns:
            Summary of executions for this test case
        """
        test_id = test_case["id"]
        category = test_case["category"]
        repetitions = test_case.get("repetitions", 1)

        results = {"executions": 0, "successful": 0, "failed": 0}

        for rep in range(repetitions):
            if self.verbose and repetitions > 1:
                print(f"  Repetition {rep + 1}/{repetitions}")

            try:
                self._execute_and_record(test_case, execution_config, repetition=rep + 1)
                results["successful"] += 1
            except Exception as e:
                if self.verbose:
                    print(f"  Failed: {e}")
                results["failed"] += 1

            results["executions"] += 1

        return results

    def _execute_and_record(
        self,
        test_case: Dict[str, Any],
        execution_config: Dict[str, Any],
        repetition: int = 1,
    ):
        """
        Execute a single test case repetition and record results.

        Args:
            test_case: Test case dictionary
            execution_config: Execution configuration
            repetition: Repetition number (for determinism tests)
        """
        test_id = test_case["id"]
        input_text = test_case["input"]

        # Get LLM parameters
        temperature = test_case.get("temperature", execution_config.get("default_temperature", 0.0))
        max_tokens = test_case.get("max_tokens", execution_config.get("default_max_tokens", 500))

        # Generate execution ID
        timestamp = datetime.utcnow()
        execution_id = f"{test_id}_rep{repetition}_{timestamp.strftime('%Y%m%d_%H%M%S')}_{uuid.uuid4().hex[:8]}"

        # Execute LLM call
        start_time = time.time()
        try:
            output = self.provider.generate(
                input_text,
                temperature=temperature,
                max_tokens=max_tokens,
            )
            execution_time_ms = int((time.time() - start_time) * 1000)
            error = None
        except Exception as e:
            output = None
            execution_time_ms = int((time.time() - start_time) * 1000)
            error = str(e)
            raise

        # Build record
        record = {
            "test_case_id": test_id,
            "execution_id": execution_id,
            "timestamp": timestamp.isoformat() + "Z",
            "category": test_case["category"],
            "subcategory": test_case.get("subcategory", ""),
            "repetition": repetition,
            "input": input_text,
            "output": output,
            "metadata": {
                "model": self.provider.get_model_info().get("model", "unknown"),
                "temperature": temperature,
                "max_tokens": max_tokens,
                "execution_time_ms": execution_time_ms,
            },
            "evaluation": self._evaluate_output(test_case, output),
        }

        if error:
            record["error"] = error

        # Write to JSONL
        self.writer.write_record(record)

    def _evaluate_output(
        self,
        test_case: Dict[str, Any],
        output: str,
    ) -> Dict[str, Any]:
        """
        Evaluate output against test case expectations.

        Args:
            test_case: Test case dictionary
            output: Generated output

        Returns:
            Evaluation results dictionary
        """
        evaluation = {}

        if output is None:
            return evaluation

        category = test_case["category"]

        # Decision determinism evaluation
        if category == "determinism" and "expected_decision" in test_case:
            decision = self._extract_decision(output, test_case)
            expected = test_case["expected_decision"]
            evaluation["decision"] = decision
            evaluation["expected_decision"] = expected
            evaluation["match"] = decision == expected

        # Truthfulness evaluation (basic)
        if category == "truthfulness":
            if "expected_facts" in test_case:
                # Simple substring matching for factual content
                facts_present = []
                for fact_option in test_case["expected_facts"]:
                    # Handle OR conditions (separated by " OR ")
                    fact_variants = [f.strip() for f in fact_option.split(" OR ")]
                    has_fact = any(variant.lower() in output.lower() for variant in fact_variants)
                    facts_present.append(has_fact)

                evaluation["facts_present"] = facts_present
                evaluation["all_facts_present"] = all(facts_present)

        # Adversarial evaluation
        if category == "adversarial":
            unacceptable = test_case.get("unacceptable_responses", [])
            acceptable = test_case.get("acceptable_response_patterns", [])

            # Check for unacceptable patterns
            violations = []
            for pattern_spec in unacceptable:
                if self._matches_pattern(output, pattern_spec):
                    violations.append(pattern_spec)

            evaluation["unacceptable_pattern_violations"] = violations
            evaluation["has_violations"] = len(violations) > 0

            # Check for acceptable patterns (if specified)
            if acceptable:
                acceptable_matches = []
                for pattern_spec in acceptable:
                    if self._matches_pattern(output, pattern_spec):
                        acceptable_matches.append(pattern_spec)

                evaluation["acceptable_pattern_matches"] = len(acceptable_matches)

        # Effectiveness evaluation (basic)
        if category == "effectiveness" and "success_criteria" in test_case:
            criteria_met = []
            for criterion in test_case["success_criteria"]:
                # Simple substring check
                met = criterion.lower() in output.lower()
                criteria_met.append(met)

            evaluation["criteria_met"] = sum(criteria_met)
            evaluation["total_criteria"] = len(test_case["success_criteria"])
            min_required = test_case.get("min_criteria_met", len(test_case["success_criteria"]))
            evaluation["passes_threshold"] = sum(criteria_met) >= min_required

        return evaluation

    def _extract_decision(self, output: str, test_case: Dict[str, Any]) -> str:
        """
        Extract decision from output for determinism testing.

        Args:
            output: Generated output
            test_case: Test case dictionary

        Returns:
            Extracted decision string
        """
        # Simple keyword extraction
        output_lower = output.lower()

        # For sentiment
        if "positive" in output_lower:
            return "positive"
        elif "negative" in output_lower:
            return "negative"
        elif "neutral" in output_lower:
            return "neutral"

        # For intent
        if "password_reset" in output_lower or "password reset" in output_lower:
            return "password_reset"

        # If expected decision is in output, return it
        expected = test_case.get("expected_decision", "")
        if expected and expected.lower() in output_lower:
            return expected

        return "unknown"

    def _matches_pattern(self, text: str, pattern_spec: Dict[str, str]) -> bool:
        """
        Check if text matches a pattern specification.

        Args:
            text: Text to check
            pattern_spec: Pattern specification dictionary with 'pattern' and 'type'

        Returns:
            True if pattern matches
        """
        pattern = pattern_spec.get("pattern", "")
        pattern_type = pattern_spec.get("type", "contains")

        if pattern_type == "contains":
            return pattern.lower() in text.lower()
        elif pattern_type == "regex":
            import re

            return bool(re.search(pattern, text, re.IGNORECASE))
        else:
            # Default to contains
            return pattern.lower() in text.lower()
