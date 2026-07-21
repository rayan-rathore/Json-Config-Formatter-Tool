# Recursively searches across data for specific keys or values
"""This module implements two powerful search features that allow developers to extract
targeted entries out of multi-thousand-line JSON log strings:
1.Search for Key: Finding and returning every nested pathway where a matching key exists.
2.Search for Value: Searching across the whole structure for specific raw data values.
To allow users to find where the data sits, your search methods should not just return
the object—they should trace out a professional structural trail string showing the exact
path to get there, like: root -> records -> [2] -> target_key."""

class JSONSearcher:
    def search_key(self, current_node, target_key):
        return self._json_crawl(current_node,target_key,current_path=[],search_mode="key")

    def search_value(self, current_node, target_value):
        return self._json_crawl(current_node, target_value, current_path=[], search_mode="value")

    def _json_crawl(self,node, target, current_path, search_mode):
        matches = []

        # CASE A: If the node is a DICTIONARY
        if isinstance(node, dict):
            for key, value in node.items():
                # Build a fresh path list copy adding this 'key' to it
                fresh_path = current_path + [str(key)]

                # Check 1: if search_mode is "key" AND the current key matches our target
                if search_mode == "key" and str(key) == str(target):
                    pretty_path = "root -> " + " -> ".join(fresh_path)
                    matches.append(pretty_path)

                # Check 2: if search_mode is "value" AND the current value directly equals our target
                elif search_mode == "value" and not isinstance(value,(dict,list)) and value == target:
                    pretty_path = "root -> " + " -> ".join(fresh_path)
                    matches.append(pretty_path)

                # Check 3: if this value is another structured object, keep digging recursively!
                if isinstance(value,(dict,list)):
                    matches += self._json_crawl(value,target,fresh_path,search_mode)

        # CASE B: If the node is a LIST
        elif isinstance(node, list):
            for index, element in enumerate(node):
                # Build a fresh path list copy adding the bracket index notation
                fresh_path = current_path + [f"[{index}]"]

                # Check 1: if search_mode is "value" AND this element directly equals our target
                if search_mode == "value" and not isinstance(element,(dict,list)) and element == target:
                    pretty_path = "root -> " + " -> ".join(fresh_path)
                    matches.append(pretty_path)

                # Check 2: if this value is another structured object, keep digging recursively!
                if isinstance(element,(dict,list)):
                    matches += self._json_crawl(element,target,fresh_path,search_mode)

        return matches
