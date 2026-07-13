import json
from pathlib import Path

REPORT_PATH = Path("/app/report.json")


def _read_report():
    with REPORT_PATH.open() as f:
        return json.load(f)


def test_report_exists_and_is_json_object():
    """Verifies success criterion 1: /app/report.json exists and contains a JSON object."""
    assert REPORT_PATH.exists(), "no report.json found"
    report = _read_report()
    assert isinstance(report, dict), "report.json must contain a JSON object"


def test_json_object_has_exact_required_keys():
    """Verifies success criterion 2: The JSON object has exactly these keys: total_requests, unique_ips, and top_path."""
    report = _read_report()
    assert set(report) == {"total_requests", "unique_ips", "top_path"}


def test_total_requests_and_unique_ips_values():
    """Verifies success criterion 3: total_requests is 6 and unique_ips is 3."""
    report = _read_report()
    assert report["total_requests"] == 6
    assert report["unique_ips"] == 3


def test_top_path_value():
    """Verifies success criterion 4: top_path is "/index.html"."""
    report = _read_report()
    assert report["top_path"] == "/index.html"
