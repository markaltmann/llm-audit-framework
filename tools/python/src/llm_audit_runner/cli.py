"""Command-line interface for LLM audit runner."""

import argparse
import sys
from pathlib import Path

from .catalog import load_catalog
from .provider import StubLLMProvider, get_provider
from .run import TestRunner


def parse_args():
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="LLM Audit Runner - Execute test cases and compute metrics",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run tests with stub provider
  %(prog)s --catalog tests.yaml --output results/ --provider stub
  
  # Filter to specific test cases
  %(prog)s --catalog tests.yaml --output results/ --provider stub --filter "det-*"
  
  # Compute metrics only (no execution)
  %(prog)s --metrics-only --output results/
        """,
    )

    parser.add_argument(
        "--catalog",
        type=Path,
        help="Path to YAML test case catalog",
    )

    parser.add_argument(
        "--output",
        type=Path,
        required=True,
        help="Output directory for results",
    )

    parser.add_argument(
        "--provider",
        choices=["stub", "custom"],
        help="LLM provider to use",
    )

    parser.add_argument(
        "--provider-config",
        type=Path,
        help="JSON configuration file for provider",
    )

    parser.add_argument(
        "--filter",
        help="Filter test cases by ID pattern (e.g., 'det-*')",
    )

    parser.add_argument(
        "--verbose",
        action="store_true",
        help="Enable verbose logging",
    )

    parser.add_argument(
        "--metrics-only",
        action="store_true",
        help="Compute metrics from existing transcripts without re-running tests",
    )

    args = parser.parse_args()

    # Validation
    if not args.metrics_only:
        if not args.catalog:
            parser.error("--catalog is required unless --metrics-only is specified")
        if not args.provider:
            parser.error("--provider is required unless --metrics-only is specified")

    return args


def main():
    """Main entry point for CLI."""
    args = parse_args()

    # Create output directory
    args.output.mkdir(parents=True, exist_ok=True)

    if args.metrics_only:
        print("Computing metrics from existing transcripts...")
        from .metrics import MetricsComputer

        computer = MetricsComputer(args.output)
        metrics = computer.compute_all_metrics()

        # Write metrics summary
        import json

        metrics_file = args.output / "metrics_summary.json"
        with open(metrics_file, "w") as f:
            json.dump(metrics, indent=2, fp=f)

        print(f"Metrics saved to {metrics_file}")
        print("\nSummary:")
        print(json.dumps(metrics, indent=2))
        return 0

    # Load test catalog
    print(f"Loading test catalog from {args.catalog}...")
    try:
        catalog = load_catalog(args.catalog)
    except Exception as e:
        print(f"Error loading catalog: {e}", file=sys.stderr)
        return 1

    # Filter test cases if requested
    test_cases = catalog["test_cases"]
    if args.filter:
        import fnmatch

        filtered = [tc for tc in test_cases if fnmatch.fnmatch(tc["id"], args.filter)]
        print(f"Filtered {len(test_cases)} cases to {len(filtered)} matching '{args.filter}'")
        test_cases = filtered

    if not test_cases:
        print("No test cases to run", file=sys.stderr)
        return 1

    # Initialize provider
    print(f"Initializing {args.provider} provider...")
    provider_config = {}
    if args.provider_config:
        import json

        with open(args.provider_config) as f:
            provider_config = json.load(f)

    provider = get_provider(args.provider, provider_config)

    # Run tests
    print(f"Running {len(test_cases)} test cases...")
    runner = TestRunner(
        provider=provider,
        output_dir=args.output,
        verbose=args.verbose,
    )

    try:
        results = runner.run_test_cases(test_cases, catalog.get("execution_config", {}))
    except Exception as e:
        print(f"Error running tests: {e}", file=sys.stderr)
        if args.verbose:
            import traceback

            traceback.print_exc()
        return 1

    # Compute and save metrics
    print("\nComputing metrics...")
    from .metrics import MetricsComputer

    computer = MetricsComputer(args.output)
    metrics = computer.compute_all_metrics()

    import json

    metrics_file = args.output / "metrics_summary.json"
    with open(metrics_file, "w") as f:
        json.dump(metrics, indent=2, fp=f)

    print(f"\nResults saved to {args.output}")
    print(f"Metrics summary: {metrics_file}")
    print("\nTest execution complete!")
    print(f"  Total executions: {results['total_executions']}")
    print(f"  Successful: {results['successful']}")
    print(f"  Failed: {results['failed']}")

    return 0 if results["failed"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
