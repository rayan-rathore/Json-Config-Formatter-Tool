import pytest

from core.engine import JSONEngine

@pytest.fixture
def engine():
    """provides fresh instance of JSONEngine for each test."""
    return JSONEngine()

def test_validate_json_checks_for_valid_json_formatting(engine):
    raw_text = '{"a":1, "b":2}'
    result_data = engine.validate_json(raw_text)

    assert isinstance(result_data,dict)

def test_validate_json_checks_for_invalid_formatting(engine):
    raw_text = '{"a":1, "b":2'
    result_data = engine.validate_json(raw_text)

    assert isinstance(result_data, str)

def test_format_json_checks_for_formatting(engine):
    data = {"a": 1, "b": 2}
    result = engine.format_json(data,sort_keys=False)
    expected = (
        "{\n"
        "        \"a\": 1,\n"
        "        \"b\": 2\n"
        "}"
    )
    assert result == expected

def test_format_json_checks_for_sort_keys_on(engine):
    data = {"c": 3, "b": 2, "a": 1}
    result = engine.format_json(data,sort_keys=True)
    expected = (
        "{\n"
        "        \"a\": 1,\n"
        "        \"b\": 2,\n"
        "        \"c\": 3\n"
        "}"
    )
    assert result == expected

def test_compact_json_checks_for_compacting(engine):
    data = {"a": 1, "b": 2}
    result = engine.compact_json(data,sort_keys=False)

    assert result == '{"a":1,"b":2}'

def test_compact_json_checks_for_sort_keys_on(engine):
    data = {"c": 3, "b": 2, "a": 1}
    result = engine.compact_json(data, sort_keys=True)

    assert result == '{"a":1,"b":2,"c":3}'
