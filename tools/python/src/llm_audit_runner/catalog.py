"""Test case catalog loading and validation."""

from pathlib import Path
from typing import Any, Dict

import yaml


def load_catalog(catalog_path: Path) -> Dict[str, Any]:
    """
    Load and validate a YAML test case catalog.

    Args:
        catalog_path: Path to the YAML catalog file

    Returns:
        Dictionary containing catalog metadata and test cases

    Raises:
        FileNotFoundError: If catalog file doesn't exist
        yaml.YAMLError: If catalog is not valid YAML
        ValueError: If catalog structure is invalid
    """
    if not catalog_path.exists():
        raise FileNotFoundError(f"Catalog not found: {catalog_path}")

    with open(catalog_path, "r") as f:
        catalog = yaml.safe_load(f)

    # Validate basic structure
    if not isinstance(catalog, dict):
        raise ValueError("Catalog must be a dictionary")

    if "test_cases" not in catalog:
        raise ValueError("Catalog must contain 'test_cases' key")

    if not isinstance(catalog["test_cases"], list):
        raise ValueError("'test_cases' must be a list")

    # Validate each test case has required fields
    for i, test_case in enumerate(catalog["test_cases"]):
        if not isinstance(test_case, dict):
            raise ValueError(f"Test case {i} must be a dictionary")

        required_fields = ["id", "category", "input"]
        for field in required_fields:
            if field not in test_case:
                raise ValueError(f"Test case {i} missing required field: {field}")

    return catalog


def validate_test_case(test_case: Dict[str, Any]) -> bool:
    """
    Validate that a test case has required fields and valid structure.

    Args:
        test_case: Test case dictionary

    Returns:
        True if valid, raises ValueError if not
    """
    required = ["id", "category", "input"]
    for field in required:
        if field not in test_case:
            raise ValueError(f"Test case missing required field: {field}")

    # Category-specific validation
    category = test_case.get("category")

    if category == "determinism":
        if "repetitions" not in test_case:
            raise ValueError(f"Determinism test case {test_case['id']} missing 'repetitions'")
        if not isinstance(test_case["repetitions"], int) or test_case["repetitions"] < 2:
            raise ValueError(
                f"Test case {test_case['id']} 'repetitions' must be integer ≥ 2"
            )

    if category == "adversarial":
        subcategory = test_case.get("subcategory", "")
        if "expected_behavior" not in test_case:
            raise ValueError(
                f"Adversarial test case {test_case['id']} missing 'expected_behavior'"
            )

    return True


def get_test_case_by_id(catalog: Dict[str, Any], test_id: str) -> Dict[str, Any]:
    """
    Retrieve a specific test case by ID.

    Args:
        catalog: Loaded catalog dictionary
        test_id: Test case ID to find

    Returns:
        Test case dictionary

    Raises:
        KeyError: If test case ID not found
    """
    for test_case in catalog["test_cases"]:
        if test_case["id"] == test_id:
            return test_case

    raise KeyError(f"Test case not found: {test_id}")


def filter_test_cases(
    catalog: Dict[str, Any],
    category: str = None,
    subcategory: str = None,
    tags: list = None,
) -> list:
    """
    Filter test cases by criteria.

    Args:
        catalog: Loaded catalog dictionary
        category: Filter by category (e.g., "determinism")
        subcategory: Filter by subcategory
        tags: Filter by tags (test case must have at least one matching tag)

    Returns:
        List of matching test cases
    """
    test_cases = catalog["test_cases"]

    if category:
        test_cases = [tc for tc in test_cases if tc.get("category") == category]

    if subcategory:
        test_cases = [tc for tc in test_cases if tc.get("subcategory") == subcategory]

    if tags:
        test_cases = [
            tc for tc in test_cases if any(tag in tc.get("tags", []) for tag in tags)
        ]

    return test_cases
