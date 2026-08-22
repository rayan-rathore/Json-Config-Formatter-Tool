"""
test for difference/comparator.py (JSONComparator)
"""
import pytest

from difference.comparator import JSONComparator

@pytest.fixture
def compare():
    return JSONComparator()

def test_compare_json_with_data_modification(compare):
    dict_old = {
        "project_name": "Alpha",
        "budget": 5000,
        "team": ["Alice", "Bob"],
        "manager": ["Mark", "Tim"],
        "product": ["PDF", "Text", "Font"],
        "settings": {
            "status": "planning",
            "version": 1.0
        }
    }
    dict_new = {
        "project_name": "Alpha-Beta",  # CHANGED (Value modified)
        "team": ["Alice", "Bob", "Charlie"],  # CHANGED (Element added to list)
        "manager": ["Mark"],  #[DELETED] (Element deleted to list)
        "product": ["Word", "Email", "Digital"],
        "settings": {
            "status": "active",  # CHANGED (Nested value modified)
            "version": 1.0,
            "environment": "production"  # ADDED (Nested key added)
        },
        "launch_date": "2026-09-01"  # ADDED (Top-level key added)
        # "budget" has been DELETED
    }
    diff = compare.compare_json(dict_old, dict_new)

    expected = [
        "[CHANGED] Value mismatch at: root -> project_name: Alpha -> Alpha-Beta",
        "[DELETED] Missing key in node B at: root -> budget",
        "[ADDED] Added key in node B at: root -> team -> [2]",
        "[DELETED] Missing key in node B at: root -> manager -> [1]",
        '[CHANGED] Value mismatch at: root -> product -> [2]: Font -> Digital',
        '[CHANGED] Value mismatch at: root -> product -> [1]: Text -> Email',
        '[CHANGED] Value mismatch at: root -> product -> [0]: PDF -> Word',
        "[CHANGED] Value mismatch at: root -> settings -> status: planning -> active",
        "[ADDED] Added key in node B at: root -> settings -> environment",
        "[ADDED] Added key in node B at: root -> launch_date"
    ]
    assert sorted(diff) == sorted(expected)

def test_compare_json_with_identical_input(compare):
    data_1 = {"a": {"x": 1}}
    data_2 = {"a": {"x": 1}}

    diff = compare.compare_json(data_1,data_2)
    expected = []

    assert diff == expected

def test_compare_json_with_type_mismatch(compare):
    data_1 = {}
    data_2 = []

    diff = compare.compare_json(data_1, data_2)
    expected = [
        "[CHANGED] Type mismatch at: root: dict -> list"
    ]

    assert diff == expected