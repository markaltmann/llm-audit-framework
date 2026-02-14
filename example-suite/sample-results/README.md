# Sample Results Directory

## Purpose

This directory is intended to store example test execution results demonstrating the output format and structure produced by the LLM audit runner.

## Directory Structure

When test campaigns are executed, results are organized as follows:

```
sample-results/
├── README.md (this file)
├── transcripts/
│   ├── results_SAMPLE-001_2026-02-14_run001.jsonl
│   ├── results_SAMPLE-001_2026-02-14_run002.jsonl
│   └── ...
├── metrics/
│   ├── metrics_summary_2026-02-14.json
│   ├── determinism_report_2026-02-14.json
│   ├── truthfulness_report_2026-02-14.json
│   └── ...
└── reports/
    ├── test_report_2026-02-14.md
    └── evidence_pack_2026-02-14/
```

## File Formats

### Transcript Files (JSONL)

Each line in a transcript file is a JSON object representing one test execution:

```json
{
  "test_case_id": "sample-det-001",
  "execution_id": "run001_20260214_143022",
  "timestamp": "2026-02-14T14:30:22Z",
  "category": "determinism",
  "subcategory": "decision_determinism",
  "input": "Customer feedback: 'The product quality is excellent...'",
  "output": "Based on the feedback, this represents positive sentiment...",
  "metadata": {
    "model": "test-model-v1",
    "temperature": 0.0,
    "max_tokens": 500,
    "execution_time_ms": 234
  },
  "evaluation": {
    "decision": "positive",
    "expected_decision": "positive",
    "match": true
  }
}
```

### Metrics Files (JSON)

Summary metrics in JSON format:

```json
{
  "test_campaign_id": "SAMPLE-001_2026-02-14",
  "date": "2026-02-14",
  "summary": {
    "total_test_cases": 12,
    "total_executions": 62,
    "pass_rate": 0.95
  },
  "determinism": {
    "decision_consistency": 0.92,
    "cases_below_threshold": 1
  },
  "truthfulness": {
    "factual_accuracy": 0.94,
    "hallucination_rate": 0.06
  },
  "effectiveness": {
    "task_completion_rate": 0.89,
    "mean_quality_score": 4.2
  },
  "adversarial": {
    "attack_resistance": 0.98,
    "critical_failures": 0
  }
}
```

## Sample Execution

To generate sample results using the Python runner:

```bash
cd tools/python
python -m llm_audit_runner.cli \
  --catalog ../../example-suite/cases/sample-cases.yaml \
  --output ../../example-suite/sample-results/transcripts/ \
  --provider stub
```

This will execute test cases using the stub provider (no actual LLM calls) and generate example output files.

## Using Results in Evidence Packs

Transcript and metrics files from this directory can be included in evidence packs as:

1. **Execution Records**: JSONL transcripts demonstrate test execution
2. **Metrics Documentation**: JSON metrics provide quantitative results
3. **Trend Analysis**: Multiple execution runs show consistency over time
4. **Audit Trail**: Timestamps and execution IDs ensure traceability

## File Naming Conventions

**Transcripts**: `results_<use-case-id>_<YYYY-MM-DD>_<run-id>.jsonl`

**Metrics**: `metrics_summary_<YYYY-MM-DD>.json`

**Reports**: `test_report_<YYYY-MM-DD>.md`

## Storage and Retention

- **Test transcripts**: Retain per risk tier requirements (see [Evidence Pack](../../docs/evidence-pack.md))
- **Metrics summaries**: Retain for trend analysis and baseline comparisons
- **Reports**: Archive per organizational policy

## Privacy and Security

When storing actual test results:

- Ensure proper access controls for confidential data
- Anonymize or redact sensitive information in transcripts
- Follow organizational data retention and disposal policies
- Encrypt at rest if results contain sensitive content

## Next Steps

After generating results:

1. **Review Transcripts**: Spot-check execution records for correctness
2. **Analyze Metrics**: Compare against thresholds and targets
3. **Identify Issues**: Flag test cases that failed or underperformed
4. **Generate Reports**: Use templates to create audit-ready summaries
5. **Compile Evidence Pack**: Organize artifacts per evidence pack requirements

## Related Documentation

- [Expected Behavior Guide](../expected-behavior.md)
- [Evidence Pack Requirements](../../docs/evidence-pack.md)
- [Python Runner Documentation](../../tools/python/README.md)
- [Test Case Catalog](../cases/sample-cases.yaml)
