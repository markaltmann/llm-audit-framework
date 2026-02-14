# LLM Audit Runner

Python-based test runner for the LLM Audit Framework. Executes test cases, captures transcripts, and computes metrics for determinism, truthfulness, effectiveness, and adversarial testing.

## Features

- **YAML-based test catalogs**: Define test cases in structured YAML format
- **Provider interface**: Vendor-agnostic LLM integration (implement for your provider)
- **Automated metrics**: Determinism, accuracy, consistency calculations
- **JSONL output**: Structured transcript capture for audit trail
- **CLI interface**: Easy command-line execution
- **Extensible**: Clear extension points for custom metrics and providers

## Installation

### From Source

```bash
cd tools/python
pip install -e .
```

### Dependencies

Minimal dependencies for core functionality:
- Python ≥3.8
- PyYAML (for catalog parsing)
- Standard library only for core runner

Optional dependencies for advanced features:
- `sentence-transformers` (for semantic similarity)
- `ruff` or `black` (for code formatting)
- `pytest` (for running tests)

## Quick Start

### 1. Define Test Cases

Create a test case catalog in YAML format (see [test-case-catalog.yaml](../../templates/test-case-catalog.yaml)):

```yaml
catalog_version: "1.0"
use_case_id: "UC-001"
test_cases:
  - id: "det-001"
    category: "determinism"
    input: "Classify sentiment: 'This product is great!'"
    expected_decision: "positive"
    repetitions: 10
```

### 2. Run Tests (Stub Mode)

Execute with the stub provider (no actual LLM calls):

```bash
python -m llm_audit_runner.cli \
  --catalog path/to/test-catalog.yaml \
  --output results/ \
  --provider stub
```

### 3. Implement Your Provider

Create a custom provider for your LLM service:

```python
from llm_audit_runner.provider import LLMProvider

class MyLLMProvider(LLMProvider):
    def __init__(self, config):
        self.api_key = config.get('api_key')
        # Initialize your LLM client
    
    def generate(self, prompt, **kwargs):
        # Call your LLM API
        response = your_llm_api.generate(prompt, **kwargs)
        return response.text
```

### 4. Run with Custom Provider

```bash
python -m llm_audit_runner.cli \
  --catalog path/to/test-catalog.yaml \
  --output results/ \
  --provider custom \
  --provider-config config.json
```

## Command-Line Interface

### Basic Usage

```bash
python -m llm_audit_runner.cli --catalog CATALOG --output OUTPUT --provider PROVIDER
```

### Options

- `--catalog PATH`: Path to YAML test case catalog (required)
- `--output PATH`: Output directory for results (required)
- `--provider NAME`: Provider to use: stub, custom (required)
- `--provider-config PATH`: JSON config file for provider (optional)
- `--filter PATTERN`: Filter test cases by ID pattern (optional)
- `--verbose`: Enable verbose logging (optional)
- `--metrics-only`: Compute metrics from existing transcripts without re-running (optional)

### Examples

**Run all tests with stub provider:**
```bash
python -m llm_audit_runner.cli \
  --catalog catalog.yaml \
  --output results/ \
  --provider stub
```

**Run only determinism tests:**
```bash
python -m llm_audit_runner.cli \
  --catalog catalog.yaml \
  --output results/ \
  --provider stub \
  --filter "det-*"
```

**Compute metrics from existing results:**
```bash
python -m llm_audit_runner.cli \
  --metrics-only \
  --output results/
```

## Output Format

### Transcript JSONL

Each test execution produces a line in the JSONL file:

```json
{
  "test_case_id": "det-001",
  "execution_id": "run001_20260214_143022",
  "timestamp": "2026-02-14T14:30:22Z",
  "category": "determinism",
  "input": "Classify sentiment: 'This product is great!'",
  "output": "Positive sentiment detected.",
  "metadata": {
    "model": "stub-model",
    "temperature": 0.0,
    "execution_time_ms": 10
  },
  "evaluation": {
    "decision": "positive",
    "expected_decision": "positive",
    "match": true
  }
}
```

### Metrics JSON

Summary metrics file:

```json
{
  "test_campaign_id": "UC-001_2026-02-14",
  "determinism": {
    "decision_consistency": 0.95,
    "cases_below_threshold": 0
  },
  "truthfulness": {
    "factual_accuracy": 0.92,
    "hallucination_rate": 0.08
  }
}
```

## Architecture

### Modules

- **cli.py**: Command-line interface and argument parsing
- **catalog.py**: YAML catalog loading and validation
- **provider.py**: Abstract provider interface and stub implementation
- **run.py**: Test execution orchestration
- **metrics.py**: Metrics computation (determinism, accuracy, etc.)
- **io.py**: JSONL writing and file handling

### Extension Points

**Custom Metrics:**

```python
from llm_audit_runner.metrics import MetricsComputer

class MyMetrics(MetricsComputer):
    def compute_custom_metric(self, transcripts):
        # Your custom metric logic
        return metric_value
```

**Custom Providers:**

Implement the `LLMProvider` interface with your LLM integration.

**Custom Evaluators:**

Add evaluation logic in `metrics.py` for domain-specific checks.

## Development

### Running Tests

```bash
cd tools/python
pytest tests/
```

### Code Formatting

```bash
# Using ruff (recommended)
ruff format src/ tests/

# Or using black
black src/ tests/
```

### Linting

```bash
ruff check src/ tests/
```

## Limitations and Future Enhancements

### Current Limitations

- **Stub provider only**: Real LLM integration requires custom provider implementation
- **Basic metrics**: Advanced metrics (LLM-as-judge, semantic similarity) are placeholders
- **No concurrency**: Sequential execution only (safe but slower)
- **Limited evaluation**: Pattern matching for adversarial tests; no complex NLP

### Planned Enhancements

- Pre-built providers for common LLM services (OpenAI, Anthropic, etc.)
- Semantic similarity using sentence transformers
- LLM-as-judge evaluation mode
- Parallel execution option
- Interactive report generation
- Integration with CI/CD systems

## Contributing

To contribute to the runner:

1. Implement new features in appropriate modules
2. Add tests for new functionality
3. Update documentation
4. Ensure code passes linting and formatting checks

## Related Documentation

- [Framework Overview](../../docs/framework-overview.md)
- [Test Case Catalog Template](../../templates/test-case-catalog.yaml)
- [Sample Test Cases](../../example-suite/cases/sample-cases.yaml)
- [Evidence Pack Requirements](../../docs/evidence-pack.md)

## License

MIT License - see [LICENSE.md](../../LICENSE.md) for details.
