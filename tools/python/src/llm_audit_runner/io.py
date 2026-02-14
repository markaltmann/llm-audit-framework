"""Input/output utilities for test results."""

import json
from datetime import datetime
from pathlib import Path
from typing import Any, Dict


class JSONLWriter:
    """
    Writes test execution records to JSONL (JSON Lines) format.

    Each record is written as a single line of JSON for easy streaming
    and processing.
    """

    def __init__(self, output_dir: Path):
        """
        Initialize JSONL writer.

        Args:
            output_dir: Directory for output files
        """
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

        # Create filename with timestamp
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        self.filename = self.output_dir / f"results_{timestamp}.jsonl"

        # Open file in append mode
        self.file = open(self.filename, "a")

    def write_record(self, record: Dict[str, Any]):
        """
        Write a single record to the JSONL file.

        Args:
            record: Dictionary to write as JSON line
        """
        json_line = json.dumps(record, ensure_ascii=False)
        self.file.write(json_line + "\n")
        self.file.flush()  # Ensure immediate write

    def close(self):
        """Close the output file."""
        if self.file and not self.file.closed:
            self.file.close()

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.close()

    def __del__(self):
        """Destructor to ensure file is closed."""
        self.close()


def read_jsonl(filepath: Path):
    """
    Read records from a JSONL file.

    Args:
        filepath: Path to JSONL file

    Yields:
        Dictionary for each line in the file
    """
    with open(filepath, "r") as f:
        for line in f:
            if line.strip():
                yield json.loads(line)


def load_all_transcripts(results_dir: Path) -> list:
    """
    Load all transcripts from JSONL files in a directory.

    Args:
        results_dir: Directory containing JSONL files

    Returns:
        List of all transcript records
    """
    transcripts = []

    for jsonl_file in Path(results_dir).glob("*.jsonl"):
        for record in read_jsonl(jsonl_file):
            transcripts.append(record)

    return transcripts


def write_metrics_summary(metrics: Dict[str, Any], output_dir: Path):
    """
    Write metrics summary to JSON file.

    Args:
        metrics: Metrics dictionary
        output_dir: Output directory
    """
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
    filename = output_dir / f"metrics_summary_{timestamp}.json"

    with open(filename, "w") as f:
        json.dump(metrics, f, indent=2, ensure_ascii=False)

    return filename
