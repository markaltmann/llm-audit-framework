# Risk Tiering Rubric

## Purpose

This rubric provides a structured approach to classifying LLM use cases by risk level. Risk classification determines the depth, frequency, and rigor of testing required for each use case.

## Risk Dimensions

Risk assessment considers multiple dimensions:

1. **Impact Severity**: Potential harm if the system provides incorrect or inappropriate information
2. **Decision Autonomy**: Degree to which users rely on system outputs without independent verification
3. **Data Sensitivity**: Handling of personal, confidential, or regulated information
4. **Audience Scope**: Number and vulnerability of affected users
5. **Regulatory Context**: Applicability of legal or compliance requirements

## Risk Tiers

### Critical Risk (Tier 1)

**Characteristics**:
- Life, health, or safety implications
- Financial decisions with significant monetary impact
- Legal or regulatory compliance requirements
- Fully autonomous decision-making without human review
- Large-scale impact on vulnerable populations

**Examples**:
- Medical diagnosis or treatment recommendations
- Safety-critical equipment operation guidance
- Legal advice with binding consequences
- Financial investment recommendations
- Child safety or welfare decisions

**Testing Requirements**:
- Comprehensive test coverage (100+ test cases per category)
- Expert review and validation required
- Determinism testing: N≥20 repetitions per critical case
- Factual accuracy: ≥99% threshold
- Adversarial testing: Full attack surface coverage
- Continuous monitoring in production
- Documented approval process for deployment
- Regular re-validation (monthly or per release)

**Evidence Pack**:
- Complete test case catalog with results
- Expert validation reports
- Metrics dashboard with all dimensions
- Risk assessment documentation
- Governance approval records
- Incident response plan

### High Risk (Tier 2)

**Characteristics**:
- Significant operational or business impact
- Moderate financial implications
- Processing of sensitive but not highly regulated data
- Human-in-the-loop with substantial reliance on system outputs
- Moderate audience size with mixed vulnerability

**Examples**:
- HR policy interpretation and guidance
- Technical troubleshooting for critical systems
- Customer support for high-value accounts
- Product selection for regulated industries
- Internal audit and compliance queries

**Testing Requirements**:
- Substantial test coverage (50+ test cases per category)
- Subject matter expert review recommended
- Determinism testing: N≥10 repetitions per case
- Factual accuracy: ≥95% threshold
- Adversarial testing: Common attack vectors covered
- Periodic validation (quarterly or per major release)

**Evidence Pack**:
- Test case catalog with results
- Metrics report covering key dimensions
- Risk assessment summary
- SME review notes (where applicable)
- Defect log with resolution status

### Medium Risk (Tier 3)

**Characteristics**:
- Limited operational impact
- Low to moderate financial implications
- General information without sensitive data
- User verification expected and typical
- Broad audience with low vulnerability

**Examples**:
- General product information queries
- Company policy FAQs (non-sensitive)
- Technical documentation lookup
- Training and learning assistance
- Routine customer service inquiries

**Testing Requirements**:
- Targeted test coverage (20+ test cases per category)
- Peer review acceptable
- Determinism testing: N≥5 repetitions for key cases
- Factual accuracy: ≥90% threshold
- Adversarial testing: Basic prompt injection checks
- Validation per release or semi-annually

**Evidence Pack**:
- Representative test cases with results
- Summary metrics report
- Defect log (if issues identified)

### Low Risk (Tier 4)

**Characteristics**:
- Minimal impact if incorrect
- No financial or operational consequences
- Public or non-sensitive information only
- User treats as suggestion, not authoritative
- Internal or limited audience

**Examples**:
- Casual conversation and small talk
- General knowledge queries (non-critical)
- Brainstorming and ideation support
- Entertainment or engagement features
- Internal experimentation and prototypes

**Testing Requirements**:
- Spot check testing (10+ representative cases)
- Informal review acceptable
- Determinism testing: Optional
- Factual accuracy: No formal threshold
- Adversarial testing: Basic safety checks only
- Validation at initial deployment and major changes

**Evidence Pack**:
- Test case examples
- Brief summary of approach and results

## Risk Scoring Framework

### Quantitative Scoring (Optional)

Organizations may choose to implement a quantitative scoring system:

| Dimension | Weight | Score Range |
|-----------|--------|-------------|
| Impact Severity | 35% | 1 (minimal) - 5 (critical) |
| Decision Autonomy | 25% | 1 (fully verified) - 5 (fully autonomous) |
| Data Sensitivity | 20% | 1 (public) - 5 (highly sensitive) |
| Audience Scope | 10% | 1 (limited) - 5 (broad/vulnerable) |
| Regulatory Context | 10% | 1 (none) - 5 (strictly regulated) |

**Risk Tier Assignment**:
- Weighted Score ≥ 4.0: Critical Risk (Tier 1)
- Weighted Score 3.0-3.9: High Risk (Tier 2)
- Weighted Score 2.0-2.9: Medium Risk (Tier 3)
- Weighted Score < 2.0: Low Risk (Tier 4)

### Qualitative Assessment

For simpler classification, answer these key questions:

1. **Could incorrect information cause harm?** (Yes = Tier 1 or 2)
2. **Will users act on the information without verification?** (Yes = Tier 2 or higher)
3. **Does the use case involve regulated data or decisions?** (Yes = Tier 2 or higher)
4. **Is the information mission-critical to operations?** (Yes = Tier 2 or higher)

If all answers are "No," the use case is typically Tier 3 or Tier 4.

## Risk Re-Classification

Risk tiers should be reviewed when:

- Use case scope or audience changes
- System behavior or capabilities evolve
- Regulatory requirements are introduced or updated
- Incidents or near-misses occur
- Organizational risk tolerance changes

## Use Case Registration

All use cases should be documented in the [Use Case Register](../templates/use-case-register.csv) with:
- Use case identifier and description
- Assigned risk tier with justification
- Responsible owner
- Testing requirements
- Review frequency
- Last assessment date

## Reliance Rules

Based on risk tier, establish appropriate reliance rules:

| Risk Tier | Reliance Rule |
|-----------|---------------|
| Critical | System outputs must be independently verified by qualified personnel before action |
| High | System outputs should be reviewed by knowledgeable users; verification required for high-stakes decisions |
| Medium | Users should apply professional judgment; spot verification recommended |
| Low | Users may rely on outputs for low-stakes decisions; exercise reasonable judgment |

## Escalation Criteria

Escalate for higher-tier classification if:
- Actual or potential harm is identified
- Users demonstrate over-reliance on system outputs
- Regulatory attention is directed at the use case
- Stakeholder concerns are raised
- Similar systems experience incidents

## Related Documentation

- [Control Objectives Matrix](control-objectives-matrix.md)
- [Use Case Register Template](../templates/use-case-register.csv)
- [Test Plan Template](../templates/test-plan-template.md)
- [Framework Overview](framework-overview.md)

## Governance Notes

Organizations should:
- Establish a cross-functional team for risk classification decisions
- Document risk classification rationale and approvals
- Integrate risk tiers with organizational risk frameworks (e.g., [Reference internal RBGF/CD here])
- Review and update the rubric annually or as needed
- Ensure consistency across similar use cases and systems
