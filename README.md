# LLM Audit Framework

A comprehensive, audit-ready framework for testing and validating LLM chatbot systems. This framework provides structured approaches to evaluate determinism, truthfulness, effectiveness, and adversarial robustness of AI systems.

## Purpose

This framework enables organizations to:
- Conduct risk-based testing of LLM applications
- Generate audit-ready evidence packs
- Map testing activities to control objectives
- Execute automated test campaigns
- Track and report quality metrics

## Key Features

### 📚 Comprehensive Documentation
- **Risk-tiered approach**: Classification framework from critical to low-risk use cases
- **Control objectives mapping**: Align testing to governance requirements
- **Testing methodologies**: Detailed guides for four key dimensions
- **Evidence pack guidelines**: Audit-ready documentation standards

### 📋 Ready-to-Use Templates
- Use case register and risk classification
- Test plan and test case catalogs (YAML)
- Scoring rubrics for quality evaluation
- Defect logs and audit report templates

### 🔧 Python Test Runner
- CLI tool for automated test execution
- Vendor-agnostic provider interface
- JSONL transcript capture
- Automated metrics computation
- Extensible architecture

### 📊 Example Test Suite
- Generic sample test cases
- Expected behavior documentation
- Results format examples

## Quick Start

### 1. Review the Framework

Start with the [Framework Overview](docs/framework-overview.md) to understand the approach, then review:

- [Risk Tiering Rubric](docs/risk-tiering-rubric.md) - Classify your use cases
- [Control Objectives Matrix](docs/control-objectives-matrix.md) - Map to your governance framework
- [Testing Methodologies](docs/framework-overview.md) - Understand each dimension

### 2. Set Up Your Use Cases

Use the [Use Case Register](templates/use-case-register.csv) to document and classify your chatbot use cases.

### 3. Define Test Cases

Adapt the [Test Case Catalog template](templates/test-case-catalog.yaml) for your use cases. See [sample cases](example-suite/cases/sample-cases.yaml) for examples.

### 4. Run Tests

Install and run the Python test runner:

```bash
cd tools/python
pip install -e .

# Run tests with stub provider (no actual LLM calls)
python -m llm_audit_runner.cli \
  --catalog ../../example-suite/cases/sample-cases.yaml \
  --output results/ \
  --provider stub \
  --verbose
```

See [Python Runner Documentation](tools/python/README.md) for full details.

### 5. Generate Evidence Pack

Use the execution results to compile an [evidence pack](docs/evidence-pack.md) using the [audit report template](templates/audit-report-template.md).

## Documentation Index

### Core Framework
- [Framework Overview](docs/framework-overview.md) - Start here
- [Risk Tiering Rubric](docs/risk-tiering-rubric.md) - Use case classification
- [Control Objectives Matrix](docs/control-objectives-matrix.md) - Governance mapping
- [Evidence Pack Requirements](docs/evidence-pack.md) - Audit documentation standards
- [Glossary](docs/glossary.md) - Terminology reference

### Testing Methodologies
- [Determinism Testing](docs/determinism-testing.md) - Consistency and repeatability
- [Truthfulness and Groundedness Testing](docs/truthfulness-groundedness-testing.md) - Factuality and RAG
- [Effectiveness Evaluation](docs/effectiveness-evaluation.md) - Task completion and quality
- [Adversarial Testing](docs/adversarial-testing.md) - Security and safety validation

### Templates
- [Use Case Register](templates/use-case-register.csv) - Use case inventory
- [Test Plan Template](templates/test-plan-template.md) - Test planning
- [Test Case Catalog](templates/test-case-catalog.yaml) - YAML test definitions
- [Scoring Rubric](templates/scoring-rubric.yaml) - Quality evaluation
- [Defect Log](templates/defect-log.csv) - Issue tracking
- [Audit Report Template](templates/audit-report-template.md) - Results documentation

### Tools
- [Python Test Runner](tools/python/README.md) - Automated execution
- [Sample Test Cases](example-suite/cases/sample-cases.yaml) - Example catalog
- [Expected Behavior Guide](example-suite/expected-behavior.md) - Evaluation reference

## Testing Dimensions

### Determinism
Evaluates consistency and repeatability of LLM outputs. Key for classification tasks, structured outputs, and decision-making systems.

**Key Metrics**: Decision consistency rate, semantic similarity, exact match rate

### Truthfulness and Groundedness
Assesses factual accuracy and proper source attribution (particularly for RAG systems). Critical for information retrieval and knowledge-based applications.

**Key Metrics**: Factual accuracy, hallucination rate, citation precision, groundedness score

### Effectiveness
Measures task completion success and response quality. Focuses on whether the system meets user needs and accomplishes intended functions.

**Key Metrics**: Task completion rate, quality scores (relevance, clarity, completeness), rework rate

### Adversarial
Validates security and safety guardrails through malicious or problematic inputs. Essential for production readiness.

**Key Metrics**: Attack resistance rate, safety bypass rate, refusal appropriateness

## Architecture

```
llm-audit-framework/
├── docs/                          # Framework documentation
│   ├── framework-overview.md
│   ├── control-objectives-matrix.md
│   ├── risk-tiering-rubric.md
│   ├── determinism-testing.md
│   ├── truthfulness-groundedness-testing.md
│   ├── effectiveness-evaluation.md
│   ├── adversarial-testing.md
│   ├── evidence-pack.md
│   └── glossary.md
├── templates/                     # Ready-to-use templates
│   ├── use-case-register.csv
│   ├── test-plan-template.md
│   ├── test-case-catalog.yaml
│   ├── scoring-rubric.yaml
│   ├── defect-log.csv
│   └── audit-report-template.md
├── example-suite/                 # Sample test cases
│   ├── cases/sample-cases.yaml
│   ├── expected-behavior.md
│   └── sample-results/README.md
├── tools/python/                  # Python test runner
│   ├── src/llm_audit_runner/
│   │   ├── cli.py              # Command-line interface
│   │   ├── catalog.py          # Catalog loading
│   │   ├── provider.py         # LLM provider interface
│   │   ├── run.py              # Test execution
│   │   ├── metrics.py          # Metrics computation
│   │   └── io.py               # JSONL I/O
│   ├── tests/                  # Unit tests
│   └── README.md
└── README.md                      # This file
```

## Customization

This framework is designed to be adapted to your organization's needs:

### Extend Testing Dimensions
Add custom metrics in `tools/python/src/llm_audit_runner/metrics.py`

### Integrate Your LLM Provider
Implement the `LLMProvider` interface in `tools/python/src/llm_audit_runner/provider.py`

### Custom Control Mappings
Adapt the control objectives matrix to your governance framework

### Domain-Specific Test Cases
Create test case catalogs for your specific use cases and domains

## Requirements

### Python Runner
- Python ≥3.8
- PyYAML ≥6.0
- Optional: pytest (for development), sentence-transformers (for semantic similarity)

### Documentation
- No special requirements - markdown files readable in any text editor or viewer

## Contributing

Contributions are welcome! Areas for contribution:
- Additional LLM provider implementations
- Enhanced metrics and evaluation methods
- Additional test case examples
- Documentation improvements
- Bug fixes and feature enhancements

Please ensure:
- Code follows existing style (ruff/black formatting)
- Tests pass (`pytest tests/`)
- Documentation is updated for new features

## License

This project is licensed under the MIT License. See [LICENSE.md](LICENSE.md) for full text.

## Support and Feedback

For questions, issues, or suggestions:
- Open an issue on GitHub
- Review documentation in the `docs/` directory
- Check example test cases in `example-suite/`

## Governance Notes

This framework provides generic guidance suitable for various organizational contexts. Organizations should:
- Map framework controls to internal governance frameworks
- Ensure test cases reflect relevant regulatory requirements
- Establish clear ownership and approval processes
- Maintain version control for all test artifacts
- Integrate with existing quality management systems

For organizations with specific governance frameworks (e.g., Bosch RBGF/CD), map the framework's control objectives to your internal requirements.