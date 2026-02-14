# Effectiveness Evaluation

## Purpose

Effectiveness evaluation assesses whether LLM systems successfully accomplish their intended tasks and meet user needs. This dimension focuses on functional performance rather than technical correctness.

## Key Concepts

### Effectiveness

**Definition**: The degree to which the system achieves its intended purpose and satisfies user requirements.

**Key Aspects**:
- **Task Completion**: Successfully fulfilling the user's request
- **Response Quality**: Usefulness, clarity, and appropriateness of responses
- **User Satisfaction**: Meeting user expectations and needs
- **Efficiency**: Minimizing rework and follow-up interactions

### Effectiveness vs. Correctness

- **Correctness** (truthfulness): Is the information factually accurate?
- **Effectiveness**: Does the response solve the user's problem?

A response can be factually correct but ineffective (e.g., too technical for the audience) or effective but incomplete (e.g., helpful guidance with minor inaccuracies in low-stakes contexts).

## Types of Effectiveness Testing

### 1. Task Completion Scoring

**Method**:
1. Define clear task objectives for each test case
2. Execute test cases and capture responses
3. Evaluate whether the task objective was met
4. Score on a binary (success/failure) or graduated scale

**Example Test Case**:
```yaml
id: eff-001
category: task_completion
input: "Help me troubleshoot why my printer won't connect to WiFi."
task_objective: "Provide actionable troubleshooting steps"
success_criteria:
  - "Mentions checking WiFi settings"
  - "Suggests printer restart"
  - "Provides clear step-by-step guidance"
scoring: "Pass if ≥2 of 3 criteria met"
```

**Scoring Scales**:
- **Binary**: Task completed (yes/no)
- **3-Point**: Incomplete, Partial, Complete
- **5-Point**: Failed, Poor, Adequate, Good, Excellent

**Success Criteria**:
- Critical risk: ≥95% task completion rate
- High risk: ≥90% task completion rate
- Medium risk: ≥85% task completion rate

### 2. Quality Rubric Scoring

**Method**:
1. Develop a scoring rubric with multiple quality dimensions
2. Evaluate responses against each dimension
3. Calculate overall quality score
4. Identify patterns in quality issues

**Example Rubric Dimensions**:
- **Relevance**: Addresses the query directly (1-5 scale)
- **Completeness**: Covers necessary information (1-5 scale)
- **Clarity**: Easy to understand for target audience (1-5 scale)
- **Actionability**: Provides concrete next steps (1-5 scale)
- **Tone**: Appropriate for context and audience (1-5 scale)

**Example Test Case**:
```yaml
id: eff-002
category: quality_rubric
input: "Explain our vacation policy to a new employee."
rubric:
  relevance: 5
  completeness: 4
  clarity: 5
  actionability: 4
  tone: 5
overall_score: 4.6/5.0
```

**Success Criteria**:
- Mean quality score ≥4.0/5.0 for critical and high-risk use cases
- Mean quality score ≥3.5/5.0 for medium-risk use cases

### 3. Rework Rate Analysis

**Method**:
1. Track multi-turn conversations in production or simulated scenarios
2. Identify cases requiring follow-up clarification or correction
3. Calculate rework rate: `conversations_requiring_rework / total_conversations`

**Rework Indicators**:
- User asks clarifying questions indicating initial response was unclear
- User corrects the system's misunderstanding
- User restates the query in different terms
- User explicitly indicates dissatisfaction

**Example Test Case**:
```yaml
id: eff-003
category: rework_rate
conversation:
  - user: "What's the status of my order #12345?"
    system: "I can help with order status. What is your order number?"
    rework_needed: true
    reason: "User already provided order number"
  - user: "I just said it's 12345"
    system: "Order #12345 was shipped on Feb 10 and is expected to arrive Feb 14."
    rework_needed: false
```

**Success Criteria**:
- Rework rate ≤10% for critical and high-risk use cases
- Rework rate ≤15% for medium-risk use cases

### 4. Response Appropriateness

**Method**:
1. Evaluate whether response style and content match the context
2. Assess audience appropriateness (technical level, formality, language)
3. Check for tone and sensitivity issues

**Evaluation Dimensions**:
- **Technical Level**: Matches user's expertise
- **Detail Level**: Appropriate depth for the query
- **Formality**: Matches organizational culture and context
- **Empathy**: Appropriate for user's situation or emotion
- **Safety**: Avoids inappropriate or harmful content

**Example Test Case**:
```yaml
id: eff-004
category: appropriateness
input: "I'm frustrated because my account was charged twice."
expected_tone: "Empathetic, apologetic, solution-focused"
inappropriate_responses:
  - "You should have checked your account" (dismissive)
  - "That's not possible" (defensive)
appropriate_responses:
  - "I apologize for the inconvenience. Let me investigate this charge issue immediately."
```

**Success Criteria**:
- Appropriateness score ≥90% across contexts

### 5. Comparative Evaluation

**Method**:
1. Generate responses from multiple system versions, configurations, or prompts
2. Compare responses side-by-side (A/B testing)
3. Evaluate which version better meets effectiveness criteria

**Example Test Case**:
```yaml
id: eff-005
category: comparative
input: "Recommend a laptop for video editing."
version_a: "I recommend the XPS 15 with 32GB RAM and RTX 4060..."
version_b: "For video editing, you'll want: 1) 32GB+ RAM, 2) Dedicated GPU..."
evaluation: "Version B is more educational and helps user make informed choice"
winner: "version_b"
```

**Use Cases**:
- Prompt optimization
- Model version selection
- Configuration tuning

## Testing Protocol

### Test Case Development

1. **Define Task Objectives**: Clear, measurable success criteria for each test case
2. **Create Diverse Scenarios**: Cover common, edge, and difficult cases
3. **Establish Baselines**: Benchmark current performance before changes
4. **Include User Perspective**: Design test cases reflecting actual user needs

### Evaluation Methods

#### Manual Evaluation

**Advantages**:
- Nuanced judgment for complex quality dimensions
- Context-aware assessment
- Can evaluate subjective aspects (tone, appropriateness)

**Process**:
1. Train evaluators on rubric criteria
2. Use multiple evaluators for consistency
3. Measure inter-rater agreement
4. Document evaluation rationale

**Best Practices**:
- Use structured rubrics to reduce subjectivity
- Provide example responses for each score level
- Calibrate evaluators periodically
- Blind evaluation when possible (hide version/configuration)

#### Automated Evaluation

**Advantages**:
- Scalable to large test suites
- Consistent and reproducible
- Fast feedback loops

**Approaches**:
- **Rule-Based**: Check for presence of keywords, required elements, format compliance
- **LLM-as-Judge**: Use a separate LLM to score responses against rubric criteria
- **Reference Matching**: Compare against known good responses (exact or semantic similarity)

**Limitations**:
- May miss nuanced quality issues
- Can be gamed or exploited
- Requires careful prompt design for LLM-as-judge

### Sample Size and Confidence

- **Critical risk**: N≥100 test cases per use case category
- **High risk**: N≥50 test cases per use case category
- **Medium risk**: N≥20 test cases per use case category
- **Low risk**: N≥10 representative test cases

## Metrics and Thresholds

### Primary Metrics

| Metric | Definition | Target (Critical) | Target (High) | Target (Medium) |
|--------|------------|-------------------|---------------|-----------------|
| Task Completion Rate | Successfully completed tasks / Total tasks | ≥95% | ≥90% | ≥85% |
| Mean Quality Score | Average rubric score across all dimensions | ≥4.0/5.0 | ≥3.5/5.0 | ≥3.0/5.0 |
| Rework Rate | Conversations requiring clarification / Total | ≤10% | ≤15% | ≤20% |
| Appropriateness | Contextually appropriate responses / Total | ≥95% | ≥90% | ≥85% |

### Secondary Metrics

- **Response Time**: Average time to generate response (for user experience)
- **Response Length**: Token count or word count (check for verbosity or brevity)
- **Actionability**: Proportion of responses providing clear next steps
- **User Satisfaction** (if available): Survey ratings or feedback scores

## Common Effectiveness Issues

### 1. Incomplete Responses

**Symptoms**: System provides partial information but omits critical details

**Causes**:
- Prompt doesn't emphasize completeness
- Model bias toward brevity
- Context window limitations

**Mitigations**:
- Explicitly request comprehensive coverage in prompts
- Use checklists or structured output formats
- Implement multi-step reasoning for complex tasks

### 2. Overly Verbose Responses

**Symptoms**: System provides excessive detail, burying key information

**Causes**:
- Prompt encourages elaboration
- Model tendency to over-explain
- Lack of audience awareness

**Mitigations**:
- Optimize prompts for conciseness
- Request summaries upfront with details available on request
- Tailor detail level to audience and context

### 3. Off-Target Responses

**Symptoms**: System misinterprets query and addresses wrong topic

**Causes**:
- Ambiguous user queries
- Poor intent detection
- Retrieval system returning irrelevant context

**Mitigations**:
- Improve query understanding through few-shot examples
- Implement clarification questions for ambiguous inputs
- Enhance retrieval relevance and ranking

### 4. Inappropriate Tone or Style

**Symptoms**: Response tone doesn't match context (e.g., too casual for serious topic)

**Causes**:
- Generic prompts not accounting for context
- Lack of persona or style guidance
- Model default behavior

**Mitigations**:
- Include tone/style instructions in system prompts
- Provide few-shot examples demonstrating desired tone
- Implement post-processing for sensitive topics

### 5. Lack of Actionability

**Symptoms**: Response provides information but no clear next steps

**Causes**:
- Prompt doesn't emphasize action items
- Model focuses on explanation over guidance
- Use case doesn't explicitly require actionability

**Mitigations**:
- Explicitly request actionable recommendations
- Structure outputs with "Next Steps" sections
- Test specifically for actionability dimension

## Test Case Design Guidelines

### High-Quality Effectiveness Test Cases

- **Realistic User Queries**: Reflect actual production usage patterns
- **Clear Success Criteria**: Evaluators can consistently judge pass/fail
- **Representative Difficulty**: Include easy, moderate, and challenging cases
- **Contextual Variation**: Test across different user personas and scenarios
- **Edge Cases**: Ambiguous queries, multi-step tasks, complex requirements

### Example Test Suite Structure

```
Effectiveness Test Suite (80 cases)
├── Task Completion (30 cases)
│   ├── Information retrieval
│   ├── Troubleshooting guidance
│   └── Decision support
├── Quality Rubric (30 cases)
│   ├── Technical queries
│   ├── Policy questions
│   └── Customer support scenarios
├── Rework Analysis (10 conversation scenarios)
│   ├── Clarification needs
│   ├── Misunderstanding recovery
│   └── Follow-up efficiency
└── Appropriateness (10 cases)
    ├── Tone sensitivity
    ├── Audience matching
    └── Context awareness
```

## Integration with Other Testing

Effectiveness testing complements:
- **Truthfulness Testing**: Accurate but ineffective responses indicate usability issues
- **Determinism Testing**: Inconsistent effectiveness suggests reliability problems
- **Adversarial Testing**: Effectiveness should not be easily degraded by adversarial inputs

## Reporting Effectiveness Results

### Summary Metrics

- Overall task completion rate (%)
- Mean quality score by dimension
- Rework rate
- Distribution of scores (histograms)
- Comparison to baseline or targets

### Detailed Case Review

For underperforming cases:
- Document specific shortcomings
- Categorize failure modes
- Assess severity and impact
- Recommend improvements (prompt engineering, retrieval tuning, etc.)

### Trends and Analysis

- Effectiveness trends over time
- Effectiveness by use case category
- Correlation between quality dimensions
- Comparison across system versions

### User Feedback Integration

Where available:
- Production satisfaction scores
- Support ticket volume and content
- Direct user feedback and complaints
- Usage analytics (session length, abandonment rate)

## Related Documentation

- [Framework Overview](framework-overview.md)
- [Risk Tiering Rubric](risk-tiering-rubric.md)
- [Scoring Rubric Template](../templates/scoring-rubric.yaml)
- [Test Case Catalog Template](../templates/test-case-catalog.yaml)

## Governance Notes

Organizations should:
- Define effectiveness standards for each use case and risk tier
- Establish evaluation processes (manual, automated, or hybrid)
- Train and calibrate evaluators for consistent scoring
- Integrate effectiveness metrics into release criteria
- Monitor production effectiveness through analytics and user feedback
- Align effectiveness requirements with business objectives and user needs
- Document effectiveness criteria in system specifications
- Reference organizational quality frameworks (e.g., [Reference internal RBGF/CD here])
