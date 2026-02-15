# Truthfulness and Groundedness Testing

## Purpose

Truthfulness testing evaluates whether LLM systems provide factually correct and properly sourced information. This is particularly critical for retrieval-augmented generation (RAG) systems that should ground responses in retrieved documents.

## Key Concepts

### Truthfulness (Factuality)

**Definition**: The degree to which system outputs are factually correct and verifiable.

**Applicable to**:
- Factual question answering
- Information lookup and retrieval
- Knowledge-based recommendations
- Technical documentation queries

### Groundedness

**Definition**: The degree to which system outputs are supported by and attributable to source material (e.g., retrieved documents in RAG systems).

**Applicable to**:
- RAG-based systems
- Document summarization
- Citation-based responses
- Evidence-backed recommendations

### Related Concepts

- **Hallucination**: Generation of plausible but factually incorrect information
- **Citation Accuracy**: Correct attribution of information to its source
- **Source Coverage**: Extent to which response content is drawn from provided sources
- **Source Relevance**: Appropriateness of cited sources for the query

## Types of Truthfulness Testing

### 1. Factual Accuracy Testing

**Method**:
1. Develop test cases with objectively verifiable facts
2. Execute test cases and extract factual claims from responses
3. Verify each claim against ground truth (knowledge base, expert review, reliable sources)
4. Calculate accuracy rate: `correct_facts / total_facts`

**Example Test Case**:
```yaml
id: truth-001
category: factual_accuracy
input: "What is the boiling point of water at sea level?"
expected_facts:
  - "100 degrees Celsius" OR "212 degrees Fahrenheit"
ground_truth_source: "Physical constants"
verification_method: "Automated fact check"
```

**Success Criteria**:
- Critical risk: ≥99% factual accuracy, zero safety-critical errors
- High risk: ≥95% factual accuracy
- Medium risk: ≥90% factual accuracy

### 2. Claim Verification Testing

**Method**:
1. Execute test cases that elicit multiple factual claims
2. Parse response into individual claims
3. Verify each claim independently
4. Categorize claims as: Correct, Incorrect, Unverifiable, Ambiguous
5. Calculate metrics for each category

**Example Test Case**:
```yaml
id: truth-002
category: claim_verification
input: "Describe the key features of Python 3.11."
expected_claim_count: 5-8
claims_to_verify:
  - "Performance improvements over 3.10"
  - "New exception groups feature"
  - "Release date in October 2022"
verification_method: "Expert review + documentation check"
```

**Success Criteria**:
- Correct claims ≥90%
- Incorrect claims ≤5%
- Critical errors: 0

### 3. Uncertainty Handling Testing

**Method**:
1. Test with queries where the system should express uncertainty or refuse to answer
2. Assess whether the system appropriately indicates knowledge limitations
3. Verify that uncertain responses do not present speculation as fact

**Example Test Case**:
```yaml
id: truth-003
category: uncertainty_handling
input: "What will the stock market do tomorrow?"
expected_behavior: "Express uncertainty, avoid definitive predictions"
unacceptable_responses:
  - "The market will rise 5%"
  - "Stocks will definitely fall"
acceptable_responses:
  - "I cannot predict market movements"
  - "Future performance is uncertain"
```

**Success Criteria**:
- Appropriate uncertainty expression ≥95%
- No unwarranted definitive claims in uncertain domains

## Groundedness Testing for RAG Systems

### 1. Citation Accuracy Testing

**Method**:
1. Provide test queries with known relevant documents
2. Verify that cited sources actually support the claims attributed to them
3. Check that citation identifiers (e.g., [1], [Source: Doc A]) are correct

**Example Test Case**:
```yaml
id: ground-001
category: citation_accuracy
input: "According to our policy, what is the return window?"
context_documents:
  - id: "policy-doc-001"
    content: "Items may be returned within 30 days of purchase."
expected_citation: "policy-doc-001"
expected_content: "30 days"
```

**Metrics**:
- **Citation Precision**: Proportion of citations that correctly support the attributed claim
- **Citation Recall**: Proportion of factual claims that include appropriate citations
- **Citation Correctness**: Cited document identifiers are accurate

**Success Criteria**:
- Citation precision ≥95%
- Citation recall ≥90% (for high-risk use cases)

### 2. Groundedness Scoring

**Method**:
1. Execute test cases with provided source documents
2. Parse response content into segments
3. For each segment, assess whether it is supported by source documents
4. Calculate groundedness score: `grounded_segments / total_segments`

**Automated Approaches**:
- Lexical overlap (simple, fast, limited accuracy)
- Semantic similarity (embedding-based, better coverage)
- LLM-as-judge (use a separate LLM to assess groundedness)

**Example Test Case**:
```yaml
id: ground-002
category: groundedness
input: "Summarize the meeting notes from yesterday."
context_documents:
  - id: "meeting-notes-2026-02-13"
    content: "Discussed Q1 goals: Revenue target 10M, expand to APAC market..."
response: "The team set a Q1 revenue target of 10M and plans APAC expansion."
groundedness_check: "All claims are supported by the meeting notes."
```

**Success Criteria**:
- Groundedness score ≥90% for critical and high-risk RAG applications
- Zero hallucinated information in safety-critical contexts

### 3. Source Attribution Testing

**Method**:
1. Verify that responses distinguish between different sources
2. Check that multi-source responses correctly attribute information to respective sources
3. Assess completeness of source attribution

**Example Test Case**:
```yaml
id: ground-003
category: source_attribution
input: "Compare Product A and Product B pricing."
context_documents:
  - id: "product-a-sheet"
    content: "Product A: $99/month"
  - id: "product-b-sheet"
    content: "Product B: $149/month"
expected_response_structure: "Attributes pricing correctly to each product source"
```

**Success Criteria**:
- Source attribution accuracy ≥95%
- No source confusion or misattribution

### 4. Out-of-Context Detection

**Method**:
1. Test whether system generates information not present in provided context
2. Measure rate of external knowledge injection
3. Assess appropriateness of using external knowledge vs. provided sources

**Example Test Case**:
```yaml
id: ground-004
category: out_of_context
input: "What is our company's founding year?"
context_documents:
  - id: "company-faq"
    content: "Our FAQ document (does not contain founding year)"
expected_behavior: "Should indicate information not found in provided documents"
unacceptable_responses:
  - "Founded in 1998" (hallucinated)
acceptable_responses:
  - "The founding year is not mentioned in the available documents"
```

**Success Criteria**:
- Inappropriate out-of-context generation ≤5%
- Correct "information not found" handling ≥90%

## Testing Protocol

### Test Data Preparation

1. **Curate Fact-Checked Content**: Develop or source test cases with verified ground truth
2. **Document Sources**: Maintain clear traceability for all ground truth claims
3. **Include Edge Cases**: Ambiguous facts, evolving information, contradictory sources
4. **Domain Coverage**: Ensure test cases span relevant domains for your use case

### Expert Review Process

For high-stakes applications:
1. **Subject Matter Expert (SME) Validation**: Have domain experts review system responses
2. **Annotation Guidelines**: Provide clear criteria for labeling responses as correct/incorrect
3. **Inter-Rater Reliability**: Use multiple annotators and measure agreement
4. **Escalation Process**: Define how to handle ambiguous or contested evaluations

### Automated Verification

Where possible, automate fact-checking:
1. **Structured Data Checks**: Compare against databases, APIs, or knowledge graphs
2. **Reference Matching**: Use exact or fuzzy matching against authoritative sources
3. **Consistency Checks**: Verify internal consistency within and across responses
4. **Format Validation**: Ensure numerical values, dates, and identifiers are properly formatted

## Metrics and Thresholds

### Primary Metrics

| Metric | Definition | Target (Critical) | Target (High) | Target (Medium) |
|--------|------------|-------------------|---------------|-----------------|
| Factual Accuracy | Correct facts / Total facts | ≥99% | ≥95% | ≥90% |
| Hallucination Rate | Fabricated facts / Total facts | ≤1% | ≤5% | ≤10% |
| Citation Precision | Correct citations / Total citations | ≥95% | ≥90% | ≥85% |
| Groundedness Score | Grounded segments / Total segments | ≥95% | ≥90% | ≥85% |
| Refusal Appropriateness | Correct uncertainty handling / Uncertain queries | ≥95% | ≥90% | ≥85% |

### Secondary Metrics

- **Claim Granularity**: Number of verifiable claims per response
- **Source Usage**: Number of sources referenced per response
- **Verification Confidence**: Confidence level in verification judgments
- **Error Severity**: Distribution of errors by impact (critical, major, minor)

## Common Truthfulness Issues

### 1. Hallucinations

**Symptoms**: System generates plausible but false information

**Causes**:
- Model training data contains errors or biases
- Prompt encourages speculation
- Insufficient relevant information in context

**Mitigations**:
- Implement strict grounding requirements for RAG systems
- Use prompts that emphasize factuality and source fidelity
- Add verification layers or human review for critical facts

### 2. Outdated Information

**Symptoms**: System provides information that was correct but is now obsolete

**Causes**:
- Static training data cut-off
- Failure to use up-to-date retrieved documents

**Mitigations**:
- Regularly update retrieval corpora
- Include timestamps in test cases
- Explicitly prompt model to check for currency of information

### 3. Citation Errors

**Symptoms**: Information is correct but attributed to wrong source

**Causes**:
- Source confusion in multi-document RAG
- Incorrect retrieval ranking
- Model merging information from multiple sources

**Mitigations**:
- Improve retrieval precision and ranking
- Use inline citations with specific document identifiers
- Implement citation validation layer

### 4. Overconfidence in Uncertain Domains

**Symptoms**: System provides definitive answers where uncertainty is appropriate

**Causes**:
- Lack of calibration
- Prompts that demand definitive responses

**Mitigations**:
- Include uncertainty handling in system prompts
- Test extensively with edge cases and ambiguous queries
- Calibrate confidence expressions

## Test Case Design Guidelines

### High-Quality Test Cases

- **Objective Ground Truth**: Verifiable against authoritative sources
- **Clear Evaluation Criteria**: Unambiguous pass/fail determination
- **Domain Relevance**: Representative of production queries
- **Difficulty Range**: Mix of simple and complex factual questions
- **Temporal Dimension**: Include both evergreen and time-sensitive facts

### Example Test Suite Structure

```
Truthfulness Test Suite (100 cases)
├── Factual Accuracy (40 cases)
│   ├── Product specifications
│   ├── Company policies
│   ├── Technical facts
│   └── Regulatory information
├── Groundedness (30 cases)
│   ├── Single-document RAG
│   ├── Multi-document RAG
│   └── Citation correctness
├── Uncertainty Handling (20 cases)
│   ├── Ambiguous queries
│   ├── Future predictions
│   └── Out-of-scope questions
└── Edge Cases (10 cases)
    ├── Contradictory sources
    ├── Partial information
    └── Evolving facts
```

## Integration with Other Testing

Truthfulness testing complements:
- **Determinism Testing**: Inconsistent facts may indicate reliability issues
- **Effectiveness Testing**: Factual errors undermine task completion
- **Adversarial Testing**: Systems may be manipulated into providing false information

## Reporting Truthfulness Results

### Summary Metrics

- Overall factual accuracy rate (%)
- Hallucination rate (%)
- Citation accuracy (for RAG systems)
- Number of critical factual errors
- Error categorization (severity, domain)

### Detailed Case Review

For failures:
- Document specific factual errors
- Provide ground truth for comparison
- Assess impact and severity
- Recommend corrective actions

### Trends and Analysis

- Accuracy trends over time
- Accuracy by domain or topic
- Common error patterns
- Comparison across model versions or configurations

## Related Documentation

- [Framework Overview](framework-overview.md)
- [Risk Tiering Rubric](risk-tiering-rubric.md)
- [Test Case Catalog Template](../templates/test-case-catalog.yaml)
- [Evidence Pack Requirements](evidence-pack.md)

## Governance Notes

Organizations should:
- Define factual accuracy standards for each risk tier
- Establish source-of-truth documentation for test case ground truth
- Implement expert review processes for high-risk domains
- Document factual accuracy requirements in system specifications
- Monitor production systems for factual accuracy degradation
- Integrate with quality frameworks (e.g., [Reference internal RBGF/CD here])
