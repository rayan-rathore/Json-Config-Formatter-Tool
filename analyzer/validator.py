# Handles schema validation & duplicate key detection
"""This module is responsible for implementing two advanced data verification
features:Duplicate Key Detection: Catching when a raw JSON string repeats a
key name inside an object (e.g., {"id": 1, "id": 2}).
Schema Validation: Verifying that a JSON file matches a blueprint dictionary
containing required fields."""
import json


class JSONValidator:

    def _detect_duplicates(self, pairs_list):
        seen_keys = set()
        for key, value in pairs_list:
            if key in seen_keys:
                raise ValueError(f"Duplicate key detected: {key}")
            else:
                seen_keys.add(key)

        return dict(pairs_list)

    def check_duplicate_keys(self, raw_text):
        try:
            json.loads(raw_text,object_pairs_hook=self._detect_duplicates)
            return True, "No syntax errors or duplicate keys found."
        except json.JSONDecodeError as e:
            return False, f"[SYNTAX ERROR] Invalid JSON structure. {str(e)}"
        except ValueError as e:
            return False, f"[DATA ERROR] {str(e)}"

    def validate_schema(self,data_dict, schema_dict):
        missing_fields = []
        if not isinstance(schema_dict, dict):
            raise TypeError("schema_dict must be dictionary.")

        # Extract the list of 'required_keys' from the blueprint dictionary
        required_keys = schema_dict.get("required",[])

        for key in required_keys:
            if key not in data_dict:
                missing_fields.append(key)
        if len(missing_fields) > 0:
            field_str = ", ".join(missing_fields)
            return False, f"Validation failed. Missing required fields: {field_str}"
        else:
            return True, "Schema validation successful! All required fields are present."
