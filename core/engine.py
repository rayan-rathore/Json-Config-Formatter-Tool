# Validates, pretty-prints, minifies, and sorts keys

import json
from .config_loader import ConfigLoader

class JSONEngine:
    def __init__(self):
        self.config = ConfigLoader()


    def validate_json(self, raw_text):
        try:
            data = json.loads(raw_text)
            return data
        except json.JSONDecodeError:
            return f"Error: {raw_text} contains invalid JSON formatting."

    #---action 1: format the raw data into readable way.
    def format_json(self, data_dict, sort_keys):
         json_strings = json.dumps(data_dict, indent=self.config.indent_spaces,sort_keys=sort_keys)
         return json_strings


    #---action 2: compact the data through removing extra spaces etc...
    def compact_json(self,data_dict,sort_keys):
        comp_strings = json.dumps(data_dict, separators=(',',':'), sort_keys=sort_keys)
        return comp_strings