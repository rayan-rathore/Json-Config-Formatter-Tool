import json
from config_loader import ConfigLoader

class JSONEngine:
    def __init__(self):
        self.config = ConfigLoader()


    def validation(self, raw_text):
        try:
            data = json.loads(raw_text)
            return data
        except json.JSONDecodeError:
            return f"Error: {raw_text} contains invalid JSON formatting."


    def modify(self, data_dict):
         json_strings = json.dumps(data_dict, indent=self.config.indent_spaces)
         return json_strings

    def minify(self,data_dict):
        comp_strings = json.dumps(data_dict, separators=(',',':'))
        return comp_strings