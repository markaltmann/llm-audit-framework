# Glossary

## Testing Framework Terms

### Adversarial Testing
Systematic testing of LLM systems against malicious or problematic inputs designed to elicit undesired, unsafe, or policy-violating responses. Includes prompt injection, jailbreaking, and data exfiltration attempts.

### Citation Accuracy
In RAG systems, the correctness of source attributions—whether cited sources actually support the claims attributed to them.

### Decision Determinism
Consistency of categorical decisions (e.g., approve/deny, category selection) across multiple executions with identical inputs. Preferred metric for classification and routing tasks.

### Defect
An identified issue, error, or deviation from expected behavior discovered during testing. Tracked in the defect log with severity classification and remediation status.

### Determinism Testing
Evaluation of consistency and repeatability of LLM outputs across multiple runs with identical or equivalent inputs.

### Effectiveness Testing
Assessment of whether LLM systems successfully accomplish intended tasks and meet user needs, focusing on functional performance rather than technical correctness.

### Evidence Pack
Comprehensive, audit-ready collection of documentation covering test planning, execution, results, and approvals for a specific LLM use case or system.

### Exact Match Rate
Proportion of test case repetitions that produce character-for-character identical outputs. Strict metric typically used for structured or template-based responses.

### Factual Accuracy
Degree to which system outputs contain factually correct and verifiable information. Key metric for truthfulness testing.

### Few-Shot Learning
Technique where example input-output pairs are included in the prompt to guide model behavior. Often used to improve determinism and task performance.

### Groundedness
Degree to which system outputs are supported by and attributable to provided source material (e.g., retrieved documents in RAG systems). Distinct from general factual accuracy.

### Hallucination
Generation of plausible but factually incorrect or unsupported information by an LLM. Critical concern for truthfulness and groundedness.

### Jailbreaking
Attempts to bypass safety constraints, content policies, or usage restrictions in an LLM system through carefully crafted prompts or conversation patterns.

### LLM (Large Language Model)
Deep learning models trained on large text corpora, capable of generating human-like text and performing various natural language tasks.

### LLM-as-Judge
Evaluation technique where a separate LLM is used to assess the quality, correctness, or appropriateness of another LLM's outputs against specified criteria.

### Prompt Injection
Attack technique where instructions embedded in user input attempt to override system directives or manipulate system behavior.

### RAG (Retrieval-Augmented Generation)
Architecture where an LLM generates responses based on information retrieved from external documents or knowledge bases, rather than relying solely on training data.

### Refusal Appropriateness
Correctness of system decisions to decline answering or performing tasks, particularly for unsafe, out-of-scope, or uncertain queries.

### Repeatability
Ability to reproduce similar outputs across multiple executions with identical inputs. Related to but broader than exact match—can include semantic consistency.

### Rework Rate
Proportion of conversations requiring follow-up clarification, correction, or restated queries due to inadequate initial responses. Key effectiveness metric.

### Risk Tier
Classification of use case by potential impact and harm (Tier 1: Critical, Tier 2: High, Tier 3: Medium, Tier 4: Low). Determines testing depth and requirements.

### Rubric
Structured scoring framework with multiple quality dimensions (e.g., relevance, completeness, clarity) used to evaluate LLM responses.

### Semantic Similarity
Measure of meaning similarity between two texts, often computed using embedding vectors. Used to assess consistency without requiring exact word-for-word matches.

### Temperature
LLM configuration parameter controlling randomness in output generation. Lower values (e.g., 0) produce more deterministic outputs; higher values (e.g., 1.0) increase variability.

### Test Case
Individual testing scenario with defined input, expected behavior, and success criteria. Cataloged in YAML format for automated execution.

### Test Campaign
Coordinated execution of multiple test cases, typically covering a use case or testing dimension over a defined period.

### Truthfulness Testing
Evaluation of whether LLM outputs are factually correct and verifiable. Includes fact-checking, claim verification, and uncertainty handling assessment.

### Use Case
Specific application or function of an LLM system (e.g., "customer FAQ answering," "technical troubleshooting"), characterized by intended purpose, audience, and risk level.

## Risk and Governance Terms

### Audit Trail
Chronological record of system activities, test executions, and decisions, maintained for accountability and compliance verification.

### Control Objective
Specific security, quality, or compliance goal that testing activities aim to demonstrate or validate (e.g., "system outputs are factually correct").

### Governance Framework
Organizational structure of policies, standards, and processes for managing and overseeing LLM systems. May include references to internal frameworks (e.g., [Reference internal RBGF/CD here]).

### Reliance Rule
Guideline specifying appropriate level of user dependence on system outputs based on risk classification (e.g., "verify independently" for high-risk use cases).

### Risk Assessment
Systematic evaluation of potential harms, impacts, and likelihood associated with a use case, used to determine risk tier and testing requirements.

### Severity Classification
Categorization of defects or vulnerabilities by potential impact: Critical (life/safety/security), High (significant policy violation), Medium (moderate issue), Low (minor issue).

### Threshold
Minimum acceptable performance level for a metric (e.g., "≥95% factual accuracy"). Varies by risk tier and testing dimension.

## Technical Terms

### API (Application Programming Interface)
Interface through which applications interact with LLM services, typically REST-based endpoints accepting prompts and returning generated text.

### Context Window
Maximum amount of input text (measured in tokens) an LLM can process in a single request, including prompt, conversation history, and retrieved documents.

### Embedding
Dense vector representation of text capturing semantic meaning, used for similarity calculations and retrieval ranking.

### Fine-Tuning
Process of further training a pre-trained LLM on specific data to specialize behavior for particular tasks or domains.

### JSONL (JSON Lines)
Text file format where each line is a valid JSON object, used for storing test transcripts and execution records.

### Provider Interface
Abstract software interface defining methods for LLM interaction, enabling vendor-agnostic test runner implementation.

### Prompt
Text input provided to an LLM, including user queries, system instructions, examples, and context. Prompt engineering focuses on optimizing prompts for desired behavior.

### Seed (Random Seed)
Value used to initialize pseudo-random number generation in LLMs. Fixed seeds can improve reproducibility (where supported by LLM provider).

### System Prompt
Instructions provided to the LLM defining its role, behavior constraints, and output format. Typically separate from user input.

### Token
Basic unit of text processing in LLMs, roughly corresponding to words or sub-words. Used for measuring input/output length and API pricing.

### Transcript
Complete record of an LLM interaction, including input prompts, system responses, metadata (timestamps, configuration), and evaluation results.

## Metrics and Statistics

### Consistency Rate
Proportion of test repetitions yielding the same decision or outcome. Primary metric for decision determinism.

### Inter-Rater Reliability
Measure of agreement between multiple human evaluators scoring the same test cases. Used to validate evaluation quality.

### Mean (Average)
Central tendency statistic calculated as sum of values divided by count. Used for quality scores, similarity measures, etc.

### Precision
In citation or classification contexts: proportion of provided answers/citations that are correct. Measures accuracy of positive claims.

### Recall
In citation or classification contexts: proportion of required information/citations that are provided. Measures completeness.

### Standard Deviation (Std Dev)
Measure of variability or spread in a dataset. Used to assess consistency of metrics like semantic similarity or response length.

### Task Completion Rate
Proportion of test cases where the system successfully accomplished the intended task objective. Primary effectiveness metric.

## Quality Assurance Terms

### Acceptance Criteria
Specific conditions that must be met for a use case or system to be approved for deployment, typically expressed as metric thresholds.

### Baseline
Reference performance measurement from a previous system version, configuration, or initial testing phase. Used for comparison and regression detection.

### Edge Case
Unusual, extreme, or boundary-condition scenario that may reveal system limitations or vulnerabilities. Important for comprehensive testing.

### Regression Testing
Re-execution of test cases after system changes to verify that previously working functionality remains intact and performance hasn't degraded.

### Root Cause Analysis
Systematic investigation to identify underlying reasons for defects or failures, enabling targeted remediation.

### Sampling
Selection of a representative subset of test cases from a larger population. Used to balance testing depth with resource constraints.

### Test Coverage
Extent to which test cases span relevant scenarios, input variations, and risk areas for a use case. Higher coverage reduces blind spots.

### Validation
Confirmation that a system meets its intended purpose and user needs (as opposed to verification, which checks compliance with specifications).

### Verification
Confirmation that a system meets specified requirements and design criteria (as opposed to validation, which checks fitness for purpose).

## Related Documentation

For detailed information on specific topics, see:
- [Framework Overview](framework-overview.md)
- [Determinism Testing](determinism-testing.md)
- [Truthfulness and Groundedness Testing](truthfulness-groundedness-testing.md)
- [Effectiveness Evaluation](effectiveness-evaluation.md)
- [Adversarial Testing](adversarial-testing.md)
- [Risk Tiering Rubric](risk-tiering-rubric.md)
- [Control Objectives Matrix](control-objectives-matrix.md)
- [Evidence Pack Requirements](evidence-pack.md)
