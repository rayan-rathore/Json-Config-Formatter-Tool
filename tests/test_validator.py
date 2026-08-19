"""
tests for analyzer/validator.py(JSONValidator).
"""
import pytest

from analyzer.validator import JSONValidator

# --- check_duplicate_keys() -------------------------------------------

def test_check_duplicate_key_returns_true_for_clean_json():
    validator = JSONValidator()
    raw_text = '{"a":1, "b":2}'

    is_valid,message = validator.check_duplicate_keys(raw_text)

    assert is_valid is True
    assert "No syntax errors" in message

def test_check_duplicate_key_detects_duplicate():
    validator = JSONValidator()
    raw_text = '{"a":1, "a":2}'

    is_valid,message = validator.check_duplicate_keys(raw_text)

    assert is_valid is False
    assert "DATA ERROR" in message
    assert "Duplicate key detected" in message

def test_check_duplicate_key_detects_broken_syntax():
    validator = JSONValidator()
    raw_text = '{"a":1, "a":2'

    is_valid,message = validator.check_duplicate_keys(raw_text)

    assert is_valid is False
    assert "SYNTAX ERROR" in message

# --- validate_schema() --------------------------------------------------

def test_validate_schema_when_all_required_fields_present():
    validator = JSONValidator()
    data = {"a":1, "b":2}
    schema = {"required":["a","b"]}

    is_valid,message = validator.validate_schema(data,schema)

    assert is_valid is True

def test_validate_schema_fails_and_lists_missing_field():
    validator = JSONValidator()
    data = {"a":1, "b":2}
    schema = {"required": ["a","b","z"]}

    is_valid,message = validator.validate_schema(data,schema)

    assert is_valid is False
    assert "z" in message

def test_validate_schema_raises_typeerror_for_non_dict_schema():
    validator = JSONValidator()
    data = {"a":1}

    with pytest.raises(TypeError):
        validator.validate_schema(data,"not a dict")