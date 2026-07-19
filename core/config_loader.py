# Defensive configuration system manager

import json


class ConfigLoader:
    def __init__(self, filepath = "config.json"):
        self.filepath = filepath
        self._indent_spaces = 4
        self._default_mode = "pretty"
        self.config_file(filepath)

    def config_file(self, target_path):
        try:
            with open(target_path, "r") as file:
                temp_dict = json.load(file)
                self._indent_spaces = temp_dict.get("indent_spaces",4)
                self._default_mode = temp_dict.get("default_mode", "pretty")
            print(f"[SUCCESS] Settings loaded successfully from '{target_path}'.")

        except FileNotFoundError:
            print( f"Error: {target_path} not found. System using default fallback settings.")

        except json.JSONDecodeError:
            print( f"Error: {target_path} contains invalid JSON formatting."
                   f" System using default fallback settings.")

    @property
    def indent_spaces(self):
        return self._indent_spaces
    @property
    def default_mode(self):
        return self._default_mode