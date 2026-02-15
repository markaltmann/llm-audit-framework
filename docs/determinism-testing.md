# Determinism Testing

## Purpose

Determinism testing evaluates the consistency and repeatability of LLM outputs. While LLMs are inherently probabilistic, many use cases require predictable behavior, particularly for decision-making, classification, or structured output generation.

## Key Concepts

### What is Determinism?

In the context of LLM systems, determinism refers to:
- **Decision Determinism**: Consistent decision outcomes (e.g., approve/deny, category A/B/C) across multiple runs with identical inputs
- **Output Repeatability**: Similarity of generated text across multiple runs with identical inputs
- **Behavior Consistency**: Predictable responses to semantically equivalent inputs (paraphrases, reordering)

### Why Determinism Matters

- **Auditability**: Reproducible results support audit and compliance review
- **User Trust**: Inconsistent answers to the same question erode user confidence
- **System Reliability**: Unpredictable behavior complicates testing and validation
- **Decision Quality**: Critical decisions should not depend on random variation
- **Debugging**: Reproducibility is essential for investigating issues

## Types of Determinism Testing

### 1. Decision Determinism Testing

**Applicable to**: Classification, routing, approval workflows, structured extraction

**Method**:
1. Identify test cases with clear decision outcomes (e.g., "classify sentiment as positive/negative/neutral")
2. Execute each test case N times (N≥5 for medium risk, N≥10 for high risk, N≥20 for critical risk)
3. Extract the decision from each response
4. Calculate decision consistency rate: `consistent_decisions / total_runs`

**Example Test Case**:
```yaml
id: det-001
category: decision_determinism
input: "Customer says: 'This product is terrible and broke after one day.' Classify sentiment."
expected_decision: "negative"
repetitions: 10
```

**Success Criteria**:
- Critical risk: ≥95% decision consistency
- High risk: ≥90% decision consistency
- Medium risk: ≥85% decision consistency

### 2. Exact Match Repeatability Testing

**Applicable to**: Template-based responses, code generation, structured formats

**Method**:
1. Identify test cases expecting highly consistent outputs
2. Execute each test case N times
3. Compare outputs for exact string matches
4. Calculate exact match rate: `exact_matches / total_runs`

**Example Test Case**:
```yaml
id: det-002
category: exact_match
input: "Generate JSON with fields: name, age, city. Use example: John, 30, Boston."
expected_format: '{"name": "John", "age": 30, "city": "Boston"}'
repetitions: 5
```

**Success Criteria**:
- Exact match rate ≥70% for structured outputs (JSON, code)
- Note: This is a strict measure; semantic consistency is often more relevant

### 3. Semantic Consistency Testing

**Applicable to**: Open-ended responses, explanations, recommendations

**Method**:
1. Execute test case N times
2. Use semantic similarity measures (e.g., embedding cosine similarity, LLM-as-judge)
3. Calculate average pairwise similarity across runs
4. Flag cases with high variance (similarity <0.8)

**Example Test Case**:
```yaml
id: det-003
category: semantic_consistency
input: "Explain the benefits of regular software updates."
repetitions: 10
similarity_threshold: 0.85
```

**Success Criteria**:
- Mean pairwise similarity ≥0.85 for high-risk cases
- Mean pairwise similarity ≥0.80 for medium-risk cases

### 4. Paraphrase Consistency Testing

**Applicable to**: Question answering, information retrieval

**Method**:
1. Create semantically equivalent input paraphrases
2. Execute each paraphrase version
3. Assess whether the system provides consistent answers
4. Calculate consistency rate across paraphrase sets

**Example Test Case**:
```yaml
id: det-004
category: paraphrase_consistency
inputs:
  - "What is the return policy?"
  - "How can I return a product?"
  - "Tell me about your returns process."
expected_consistency: "All versions should provide same core information"
```

**Success Criteria**:
- ≥90% of paraphrase sets should yield consistent core information

## Testing Protocol

### Test Configuration

When configuring LLM API calls for determinism testing:

**Temperature Settings**:
- Use temperature=0 (or lowest available setting) for maximum determinism
- Test at production temperature settings to assess real-world consistency
- Document temperature parameter in test metadata

**Seed Settings** (if available):
- Set a fixed random seed when available
- Document whether determinism holds across different seeds
- Note: Not all LLM providers support seed parameters

**Model Version**:
- Pin model version for repeatability
- Document model version in test results
- Re-test when upgrading model versions

### Execution Best Practices

1. **Run Order**: Randomize or interleave test case executions to avoid temporal bias
2. **Timing**: Space repetitions by several seconds to avoid caching effects (if applicable)
3. **Context**: Ensure identical context and conversation history for each repetition
4. **Infrastructure**: Use the same API endpoint and configuration for all repetitions
5. **Documentation**: Capture all configuration parameters in test metadata

### Metrics to Capture

For each test case, record:
- **Decision Consistency Rate**: Proportion of runs yielding the same decision
- **Exact Match Rate**: Proportion of runs yielding identical text output
- **Semantic Similarity**: Mean and std deviation of pairwise similarity scores
- **Variance Indicators**: Maximum deviation from expected output
- **Response Length Stability**: Consistency of response length (token count)

## Interpreting Results

### High Determinism (>90% consistency)

**Interpretation**: System behavior is highly predictable for this use case

**Actions**:
- Suitable for production deployment in high-stakes contexts
- Establish baseline for regression testing
- Monitor for degradation over time

### Moderate Determinism (70-90% consistency)

**Interpretation**: Some variability present; may be acceptable depending on use case

**Actions**:
- Assess whether variability impacts user experience or decisions
- Consider prompt engineering to improve consistency
- Implement human review for critical instances
- Document known variability in user guidance

### Low Determinism (<70% consistency)

**Interpretation**: Significant unpredictability; may not be suitable for critical use cases

**Actions**:
- Investigate root causes (temperature, prompt ambiguity, model limitations)
- Consider alternative approaches (e.g., retrieval-based, rule-based)
- Downgrade risk tier or implement strict human oversight
- Document limitations for users and stakeholders

### Trends Over Time

Monitor determinism metrics across releases:
- **Degradation**: May indicate model updates, configuration drift, or prompt changes
- **Improvement**: May result from prompt engineering or model fine-tuning
- **Instability**: Fluctuating metrics suggest system or infrastructure issues

## Common Causes of Low Determinism

1. **High Temperature Settings**: Intentionally increases randomness
2. **Ambiguous Prompts**: Under-specified tasks allow multiple valid interpretations
3. **Complex Reasoning**: Multi-step reasoning is more variable than simple tasks
4. **Model Limitations**: Model may not have been trained for deterministic behavior
5. **Context Length**: Very long contexts can introduce variability
6. **Infrastructure**: Load balancing across different model instances may introduce variance

## Mitigation Strategies

### Prompt Engineering

- Provide explicit structure or format requirements
- Use few-shot examples demonstrating desired consistency
- Break complex tasks into simpler, more deterministic sub-tasks
- Request step-by-step reasoning to guide model behavior

### Temperature and Configuration

- Use temperature=0 for classification and structured tasks
- Use lower temperatures (0.1-0.3) for factual question answering
- Reserve higher temperatures (0.7-1.0) for creative tasks where variability is desired

### Post-Processing

- Implement deterministic post-processing layers (e.g., regex extraction, format validation)
- Use ensemble methods (majority voting across multiple runs) for critical decisions
- Apply business rules to normalize outputs

### Model Selection

- Evaluate different model sizes or versions for consistency
- Consider fine-tuning for specific deterministic tasks
- Use specialized models (e.g., classifiers) for highly structured outputs

## Test Case Design Guidelines

### Good Test Cases for Determinism

- Clear, unambiguous expected outcome
- Objective evaluation criteria
- Representative of production workload
- Cover edge cases and boundary conditions
- Include both simple and complex scenarios

### Example Test Suite Structure

```
Determinism Test Suite (50 cases)
├── Classification (20 cases, N=10 each)
│   ├── Sentiment analysis
│   ├── Intent detection
│   └── Category routing
├── Structured Generation (15 cases, N=5 each)
│   ├── JSON extraction
│   ├── Form filling
│   └── Data normalization
└── Paraphrase Consistency (15 case sets)
    ├── Policy questions
    ├── Technical queries
    └── Procedural requests
```

## Reporting Determinism Results

### Summary Metrics

- Overall decision consistency rate (%)
- Mean semantic similarity across all test cases
- Number of cases below threshold
- Distribution of consistency scores

### Detailed Case Review

For cases failing consistency thresholds:
- Document variance observed
- Provide example outputs illustrating inconsistency
- Assess impact on use case suitability
- Recommend mitigations or re-classification

### Trend Dashboard

- Consistency metrics over time
- Comparison across model versions
- Comparison across risk tiers

## Integration with Other Testing

Determinism testing complements:
- **Truthfulness Testing**: Inconsistent outputs may indicate unreliable information
- **Effectiveness Testing**: Variability can impact task completion rates
- **Adversarial Testing**: Inconsistency may indicate vulnerability to manipulation

## Related Documentation

- [Framework Overview](framework-overview.md)
- [Risk Tiering Rubric](risk-tiering-rubric.md)
- [Test Case Catalog Template](../templates/test-case-catalog.yaml)
- [Metrics Implementation](../tools/python/src/llm_audit_runner/metrics.py)

## Governance Notes

Organizations should:
- Define acceptable determinism thresholds for each risk tier
- Establish monitoring processes for production systems
- Document determinism requirements in use case specifications
- Include determinism testing in change control procedures
- Integrate with organizational quality frameworks (e.g., [Reference internal RBGF/CD here])
