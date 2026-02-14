# Audit Report Template

## Executive Summary

**System/Use Case**: [Use Case Name and ID]  
**Report Date**: YYYY-MM-DD  
**Test Period**: YYYY-MM-DD to YYYY-MM-DD  
**Risk Tier**: [Critical / High / Medium / Low]  
**Report Version**: 1.0  
**Authors**: [Names and Roles]

### Overall Assessment

**Deployment Recommendation**: [APPROVED / CONDITIONAL APPROVAL / REJECTED]

**Key Findings**:
- [High-level summary of test results]
- [Critical achievements or concerns]
- [Overall system readiness]

**Critical Issues**: [Count and brief description, or "None"]

**Conditions for Deployment** (if conditional approval):
1. [Condition 1]
2. [Condition 2]

---

## Use Case Overview

### Description

[Detailed description of the use case, its intended function, target audience, and business context]

### Risk Classification

**Risk Tier**: [Tier and classification]

**Rationale**: [Why this tier was assigned, referencing impact, autonomy, data sensitivity, audience, and regulatory context]

**Reliance Rule**: [Guidance for appropriate user reliance on system outputs]

### Control Objectives

This testing addresses the following control objectives:

1. [Control objective 1] - [How testing addresses it]
2. [Control objective 2] - [How testing addresses it]
3. [Control objective 3] - [How testing addresses it]

See [Control Objectives Matrix](../docs/control-objectives-matrix.md) for detailed mapping.

---

## Testing Summary

### Testing Scope

**Testing Dimensions**:
- [X] Determinism Testing
- [X] Truthfulness/Groundedness Testing
- [X] Effectiveness Evaluation
- [X] Adversarial Testing

**Test Coverage**:
- Total test cases: [N]
- Test executions: [N]
- Manual evaluations: [N]
- Expert reviews: [N]

**Test Period**: [Start date] to [End date]

**Test Environment**:
- Model: [Name and version]
- Configuration: [Temperature, max tokens, other parameters]
- Infrastructure: [Brief description]

### Testing Approach

[Summary of methodology, evaluation methods, sample sizes, and any special considerations]

---

## Test Results

### Determinism Testing

**Objective**: Assess consistency and repeatability of system outputs

**Test Cases**: [N] cases, [R] repetitions each

**Results**:

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Decision Consistency | ≥[N]% | [N]% | [PASS/FAIL] |
| Semantic Similarity (mean) | ≥[N] | [N] | [PASS/FAIL] |
| Cases below threshold | 0 | [N] | [PASS/FAIL] |

**Key Findings**:
- [Finding 1, e.g., "Classification tasks showed 95% consistency, exceeding 90% target"]
- [Finding 2, e.g., "Open-ended responses varied more but within acceptable range"]
- [Finding 3, e.g., "No critical decision inconsistencies observed"]

**Issues Identified**: [Count] issues, see Defect Log section

### Truthfulness/Groundedness Testing

**Objective**: Verify factual correctness and proper source attribution

**Test Cases**: [N] factual accuracy, [N] groundedness (for RAG)

**Results**:

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Factual Accuracy | ≥[N]% | [N]% | [PASS/FAIL] |
| Hallucination Rate | ≤[N]% | [N]% | [PASS/FAIL] |
| Citation Precision (RAG) | ≥[N]% | [N]% | [PASS/FAIL] |
| Critical Factual Errors | 0 | [N] | [PASS/FAIL] |

**Key Findings**:
- [Finding 1, e.g., "94% factual accuracy on product specifications"]
- [Finding 2, e.g., "All citations correctly attributed to source documents"]
- [Finding 3, e.g., "System appropriately expressed uncertainty for out-of-scope queries"]

**Issues Identified**: [Count] issues, see Defect Log section

### Effectiveness Evaluation

**Objective**: Assess whether system successfully completes intended tasks

**Test Cases**: [N] task completion, [N] quality rubric evaluations

**Results**:

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Task Completion Rate | ≥[N]% | [N]% | [PASS/FAIL] |
| Mean Quality Score | ≥[N]/5.0 | [N]/5.0 | [PASS/FAIL] |
| Rework Rate | ≤[N]% | [N]% | [PASS/FAIL] |
| Appropriateness | ≥[N]% | [N]% | [PASS/FAIL] |

**Key Findings**:
- [Finding 1, e.g., "89% task completion rate, meeting 85% target for medium risk"]
- [Finding 2, e.g., "Response tone consistently appropriate across contexts"]
- [Finding 3, e.g., "Minor issues with verbosity on simple queries"]

**Issues Identified**: [Count] issues, see Defect Log section

### Adversarial Testing

**Objective**: Validate security and safety guardrails

**Test Cases**: [N] prompt injection, [N] unsafe advice, [N] data exfiltration, [N] other

**Results**:

| Metric | Target | Achieved | Status |
|--------|--------|----------|--------|
| Prompt Injection Resistance | ≥95% | [N]% | [PASS/FAIL] |
| Data Leakage Rate | 0% | [N]% | [PASS/FAIL] |
| Safety Bypass Rate | ≤2% | [N]% | [PASS/FAIL] |
| Critical Safety Failures | 0 | [N] | [PASS/FAIL] |

**Key Findings**:
- [Finding 1, e.g., "Strong resistance to prompt injection attempts"]
- [Finding 2, e.g., "No system prompt or confidential data leakage observed"]
- [Finding 3, e.g., "One medium-severity safety bypass identified and mitigated"]

**Issues Identified**: [Count] issues, see Defect Log section

---

## Defect Log Summary

### Defects by Severity

| Severity | Count | Resolved | Open | Accepted Risk |
|----------|-------|----------|------|---------------|
| Critical | [N] | [N] | [N] | [N] |
| High | [N] | [N] | [N] | [N] |
| Medium | [N] | [N] | [N] | [N] |
| Low | [N] | [N] | [N] | [N] |
| **Total** | [N] | [N] | [N] | [N] |

### Critical and High Severity Defects

#### DEF-001: [Title]
- **Severity**: [Critical/High]
- **Category**: [Determinism/Truthfulness/Effectiveness/Adversarial]
- **Description**: [Brief description]
- **Status**: [Resolved/Open/Accepted Risk]
- **Resolution**: [How it was or will be addressed]

#### DEF-002: [Title]
[Repeat for each critical/high severity defect]

### Accepted Risks

[For any unresolved critical or high severity issues, provide detailed justification for accepting the risk]

---

## Metrics Dashboard

### Summary Metrics

| Testing Dimension | Overall Score | Status |
|-------------------|---------------|--------|
| Determinism | [Score]/100 | [PASS/FAIL] |
| Truthfulness | [Score]/100 | [PASS/FAIL] |
| Effectiveness | [Score]/100 | [PASS/FAIL] |
| Adversarial | [Score]/100 | [PASS/FAIL] |
| **Overall** | [Score]/100 | [PASS/FAIL] |

### Trends

[If applicable, show comparison to previous test results, baselines, or alternative configurations]

[Include charts or graphs if available]

---

## Recommendations

### Deployment Decision

**Recommendation**: [APPROVED / CONDITIONAL APPROVAL / REJECTED]

**Rationale**: [Explanation of the decision based on test results, risk tier requirements, and defect status]

### Conditions and Monitoring (if conditional approval)

1. **Condition 1**: [Specific requirement before or after deployment]
2. **Condition 2**: [Monitoring requirement, frequency, or compensating control]
3. **Condition 3**: [User guidance or limitation documentation]

### Improvement Opportunities

1. [Opportunity 1, e.g., "Consider prompt refinement to improve conciseness"]
2. [Opportunity 2, e.g., "Expand test coverage for edge cases in future releases"]
3. [Opportunity 3, e.g., "Implement automated monitoring for factual accuracy drift"]

### Next Steps

1. [Action item 1 with responsible party and timeline]
2. [Action item 2 with responsible party and timeline]
3. [Action item 3 with responsible party and timeline]

---

## Approvals and Sign-Off

**Test Lead**: [Name] - [Date] - [Signature/Approval]  
**Product Owner**: [Name] - [Date] - [Signature/Approval]  
**Risk/Compliance**: [Name] - [Date] - [Signature/Approval]  
**Security** (if applicable): [Name] - [Date] - [Signature/Approval]  
**Technical Lead**: [Name] - [Date] - [Signature/Approval]

**Approval Status**: [APPROVED / CONDITIONAL / REJECTED]

**Next Review Date**: [YYYY-MM-DD]

---

## Appendices

### A. Test Plan Reference

[Link or reference to test plan document]

### B. Test Case Catalog

[Link or reference to test case catalog]

### C. Detailed Results

[Link to JSONL transcript files and detailed execution logs]

### D. Evaluation Rubrics

[Link to scoring rubrics used]

### E. System Configuration

[Detailed system configuration, model specifications, environment details]

### F. References

- [Use Case Register](use-case-register.csv)
- [Test Plan](test-plan-template.md)
- [Test Case Catalog](test-case-catalog.yaml)
- [Defect Log](defect-log.csv)
- [Framework Documentation](../docs/framework-overview.md)

---

## Document Control

**Document ID**: AUDIT-RPT-[Use Case ID]-[YYYY-MM]  
**Version**: 1.0  
**Created**: [Date]  
**Last Modified**: [Date]  
**Classification**: [Confidential/Internal/Public]  
**Retention**: [Per organizational policy and risk tier]  
**Archive Location**: [File path or document management system reference]

---

*This audit report follows the LLM Audit Framework guidelines. See [framework documentation](../docs/framework-overview.md) for methodology details.*
