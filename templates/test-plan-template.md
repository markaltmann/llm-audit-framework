# Test Plan Template

## Test Identification

**Test Plan ID**: TP-YYYY-MM-NNN  
**Use Case ID**: UC-XXX  
**Use Case Name**: [Use Case Name]  
**Risk Tier**: [Critical / High / Medium / Low]  
**Test Plan Version**: 1.0  
**Date**: YYYY-MM-DD  
**Author**: [Name]  

## Use Case Summary

**Description**: [Brief description of the use case and its intended function]

**Target Audience**: [Who will use this system]

**Key Functionality**: [What the system is expected to do]

**Risk Classification Rationale**: [Why this risk tier was assigned, referencing risk tiering rubric]

## Testing Objectives

**Primary Objectives**:
1. [Objective 1, e.g., "Verify factual accuracy ≥95%"]
2. [Objective 2, e.g., "Validate appropriate refusal of unsafe requests"]
3. [Objective 3, e.g., "Assess task completion rate ≥90%"]

**Control Objectives Addressed**:
- [Control objective 1] - Maps to [testing dimension]
- [Control objective 2] - Maps to [testing dimension]

See [Control Objectives Matrix](../docs/control-objectives-matrix.md) for detailed mapping.

## Testing Scope

### In Scope
- [Testing dimension 1, e.g., "Determinism testing on classification tasks"]
- [Testing dimension 2, e.g., "Truthfulness testing on factual queries"]
- [Testing dimension 3, e.g., "Adversarial testing for prompt injection"]

### Out of Scope
- [What will not be tested and why]
- [Any known limitations or future work]

### Testing Dimensions

| Dimension | Included? | Rationale |
|-----------|-----------|-----------|
| Determinism | Yes/No | [Why included or excluded based on risk tier and use case] |
| Truthfulness | Yes/No | [Rationale] |
| Effectiveness | Yes/No | [Rationale] |
| Adversarial | Yes/No | [Rationale] |

## Test Strategy

### Test Case Coverage

**Total Test Cases**: [Number]

**Breakdown by Dimension**:
- Determinism: [N] cases, [R] repetitions each
- Truthfulness: [N] cases
- Effectiveness: [N] cases
- Adversarial: [N] cases

**Test Case Selection Criteria**:
- [How test cases were chosen, e.g., "Representative queries from production logs"]
- [Coverage considerations, e.g., "Span common, edge, and error cases"]

### Evaluation Methods

**Automated Testing**:
- [What will be tested automatically, e.g., "Decision determinism via test runner"]
- [Metrics that can be computed automatically]

**Manual Evaluation**:
- [What requires human judgment, e.g., "Response appropriateness scoring"]
- [Number of evaluators and qualifications]

**Expert Review** (if applicable):
- [Subject matter expert requirements]
- [Review scope and criteria]

### Test Environment

**System Configuration**:
- Model: [Model name and version]
- Temperature: [Value]
- Max tokens: [Value]
- Other parameters: [List any other relevant configuration]

**Test Infrastructure**:
- Test runner: [Version]
- Execution platform: [Where tests will run]
- Data storage: [Where results will be stored]

**Test Data**:
- Source: [Where test cases come from]
- Preparation: [Any data preparation or anonymization steps]

## Success Criteria

### Quantitative Thresholds

Based on risk tier [Critical/High/Medium/Low]:

| Metric | Target | Justification |
|--------|--------|---------------|
| Decision consistency | ≥[N]% | [Per determinism testing guidelines for this tier] |
| Factual accuracy | ≥[N]% | [Per truthfulness testing guidelines for this tier] |
| Task completion rate | ≥[N]% | [Per effectiveness guidelines for this tier] |
| Attack resistance | ≥[N]% | [Per adversarial testing guidelines for this tier] |
| Critical defects | 0 | [Zero tolerance for safety/security critical issues] |

### Qualitative Criteria

- [Criterion 1, e.g., "No unsafe advice provided in any test case"]
- [Criterion 2, e.g., "Response tone appropriate for target audience"]
- [Criterion 3, e.g., "System demonstrates proper uncertainty handling"]

### Acceptance Decision

**Approval Conditions**:
- All quantitative thresholds met
- All qualitative criteria satisfied
- All critical and high-severity defects resolved or formally accepted as risks
- Evidence pack complete and reviewed

**Conditional Approval** (if applicable):
- [Conditions under which system can deploy with caveats]
- [Required monitoring or compensating controls]

**Rejection Criteria**:
- [Conditions that would prevent deployment]

## Test Execution

### Schedule

| Phase | Start Date | End Date | Responsible Party |
|-------|------------|----------|-------------------|
| Test case development | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Environment setup | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Automated test execution | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Manual evaluation | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Expert review (if applicable) | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Results analysis | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Evidence pack compilation | YYYY-MM-DD | YYYY-MM-DD | [Name] |
| Review and approval | YYYY-MM-DD | YYYY-MM-DD | [Name] |

### Resources Required

**Personnel**:
- Test lead: [Name]
- Test engineers: [Names]
- Manual evaluators: [Number and qualifications]
- Subject matter experts: [Names and expertise]
- Approvers: [Names and roles]

**Infrastructure**:
- LLM API access and quota
- Test runner infrastructure
- Storage for test results
- Analysis tools

**Estimated Effort**:
- Test development: [Person-days]
- Execution: [Person-days]
- Evaluation: [Person-days]
- Documentation: [Person-days]
- Total: [Person-days]

## Risk and Mitigation

### Testing Risks

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1, e.g., "API rate limits delay execution"] | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy] |
| [Risk 2, e.g., "Manual evaluator availability"] | [Low/Med/High] | [Low/Med/High] | [Mitigation strategy] |

### Dependencies

- [Dependency 1, e.g., "Model version freeze during test period"]
- [Dependency 2, e.g., "Access to production retrieval corpus"]

## Deliverables

### Evidence Pack Components

- [ ] Executive summary
- [ ] This test plan
- [ ] Test case catalog (YAML)
- [ ] Execution transcripts (JSONL)
- [ ] Metrics report
- [ ] Defect log
- [ ] Approval sign-off

### Additional Artifacts

- [Any supplementary documentation]
- [Screen captures or recordings if applicable]

## References

- [Use Case Register](use-case-register.csv)
- [Test Case Catalog](test-case-catalog.yaml)
- [Scoring Rubric](scoring-rubric.yaml)
- [Defect Log](defect-log.csv)
- [Framework Documentation](../docs/framework-overview.md)

## Approval

**Prepared By**: [Name, Role] - [Date]  
**Reviewed By**: [Name, Role] - [Date]  
**Approved By**: [Name, Role] - [Date]  

**Next Review Date**: [YYYY-MM-DD]

---

*This test plan follows the LLM Audit Framework guidelines. See [framework documentation](../docs/framework-overview.md) for methodology details.*
