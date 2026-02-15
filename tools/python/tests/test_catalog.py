"""Tests for catalog loading and validation."""

import pytest
import tempfile
from pathlib import Path

from llm_audit_runner.catalog import (
    load_catalog,
    validate_test_case,
    get_test_case_by_id,
    filter_test_cases,
)


def create_test_catalog(content: str) -> Path:
    """Helper to create a temporary catalog file."""
    with tempfile.NamedTemporaryFile(mode="w", suffix=".yaml", delete=False) as f:
        f.write(content)
        return Path(f.name)


def test_load_valid_catalog():
    """Test loading a valid catalog."""
    catalog_content = """
catalog_version: "1.0"
use_case_id: "TEST-001"
test_cases:
  - id: "test-001"
    category: "determinism"
    input: "Test input"
    repetitions: 5
"""
    catalog_path = create_test_catalog(catalog_content)

    try:
        catalog = load_catalog(catalog_path)
        assert catalog["catalog_version"] == "1.0"
        assert catalog["use_case_id"] == "TEST-001"
        assert len(catalog["test_cases"]) == 1
        assert catalog["test_cases"][0]["id"] == "test-001"
    finally:
        catalog_path.unlink()


def test_load_missing_catalog():
    """Test loading a non-existent catalog."""
    with pytest.raises(FileNotFoundError):
        load_catalog(Path("nonexistent.yaml"))


def test_load_invalid_yaml():
    """Test loading invalid YAML."""
    catalog_content = "invalid: yaml: content:"
    catalog_path = create_test_catalog(catalog_content)

    try:
        with pytest.raises(Exception):  # YAML error
            load_catalog(catalog_path)
    finally:
        catalog_path.unlink()


def test_load_catalog_missing_test_cases():
    """Test catalog without test_cases key."""
    catalog_content = """
catalog_version: "1.0"
use_case_id: "TEST-001"
"""
    catalog_path = create_test_catalog(catalog_content)

    try:
        with pytest.raises(ValueError, match="test_cases"):
            load_catalog(catalog_path)
    finally:
        catalog_path.unlink()


def test_validate_test_case_valid():
    """Test validating a valid test case."""
    test_case = {
        "id": "test-001",
        "category": "truthfulness",
        "input": "Test input",
    }
    assert validate_test_case(test_case) is True


def test_validate_test_case_missing_id():
    """Test validating test case without ID."""
    test_case = {
        "category": "truthfulness",
        "input": "Test input",
    }
    with pytest.raises(ValueError, match="id"):
        validate_test_case(test_case)


def test_validate_determinism_test_case():
    """Test validating determinism test case."""
    # Valid determinism test
    test_case = {
        "id": "det-001",
        "category": "determinism",
        "input": "Test input",
        "repetitions": 10,
    }
    assert validate_test_case(test_case) is True

    # Missing repetitions
    test_case_invalid = {
        "id": "det-001",
        "category": "determinism",
        "input": "Test input",
    }
    with pytest.raises(ValueError, match="repetitions"):
        validate_test_case(test_case_invalid)


def test_get_test_case_by_id():
    """Test retrieving test case by ID."""
    catalog = {
        "test_cases": [
            {"id": "test-001", "category": "determinism", "input": "Input 1"},
            {"id": "test-002", "category": "truthfulness", "input": "Input 2"},
        ]
    }

    test_case = get_test_case_by_id(catalog, "test-002")
    assert test_case["id"] == "test-002"
    assert test_case["category"] == "truthfulness"

    # Non-existent ID
    with pytest.raises(KeyError):
        get_test_case_by_id(catalog, "test-999")


def test_filter_test_cases_by_category():
    """Test filtering test cases by category."""
    catalog = {
        "test_cases": [
            {"id": "det-001", "category": "determinism", "input": "Input 1"},
            {"id": "truth-001", "category": "truthfulness", "input": "Input 2"},
            {"id": "det-002", "category": "determinism", "input": "Input 3"},
        ]
    }

    filtered = filter_test_cases(catalog, category="determinism")
    assert len(filtered) == 2
    assert all(tc["category"] == "determinism" for tc in filtered)


def test_filter_test_cases_by_tags():
    """Test filtering test cases by tags."""
    catalog = {
        "test_cases": [
            {"id": "test-001", "category": "determinism", "input": "I1", "tags": ["sentiment"]},
            {
                "id": "test-002",
                "category": "truthfulness",
                "input": "I2",
                "tags": ["facts", "policy"],
            },
            {"id": "test-003", "category": "effectiveness", "input": "I3", "tags": ["sentiment"]},
        ]
    }

    filtered = filter_test_cases(catalog, tags=["sentiment"])
    assert len(filtered) == 2
    assert all("sentiment" in tc["tags"] for tc in filtered)

    filtered = filter_test_cases(catalog, tags=["policy"])
    assert len(filtered) == 1
    assert filtered[0]["id"] == "test-002"
