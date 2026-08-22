# Computes line-by-line differences between two separate JSON files
"""This feature examines two separate parsed dictionaries side-by-side to
figure out exactly what changed between File A and File B.
extracts all keys from both objects and compares them across three distinct
checks:
Keys present in A, but missing in B (Representing data that was Deleted).
Keys missing in A, but present in B (Representing data that was Added).
Keys present in both files but containing different data (Representing data
that was Changed).
"""
import json


class JSONComparator:  

    def compare_json(self, json_a, json_b):
        return  self._diff_tracker(json_a,json_b,path=["root"])

    def _diff_tracker(self,node_a, node_b, path):
        differences = []

        # Case A: both nodes are DICTIONARIES
        if isinstance(node_a,dict) and isinstance(node_b,dict):
            # Extract a unified list of ALL unique keys from BOTH objects combined the set union operator '|'
            unified_keys = set(node_a.keys()) | set(node_b.keys())
            for key in unified_keys:
                fresh_path = path + [str(key)]
                pretty_path = " -> ".join(fresh_path)

                # --- COMPARISON SCENARIOS ---
                #SUB-CASE A: Keys present in A, but missing in B (Representing data that was Deleted).
                if key in node_a and key not in node_b:
                    diff_str = f"[DELETED] Missing key in node B at: {pretty_path}"
                    differences.append(diff_str)

                #SUB-CASE B: Keys missing in A, but present in B (Representing data that was Added).
                elif key not in node_a and key in node_b:
                    diff_str = f"[ADDED] Added key in node B at: {pretty_path}"
                    differences.append(diff_str)

                #SUB-CASE C: Keys present in both files but containing different data (Representing data that was Changed).
                else:
                    val_a = node_a.get(key)
                    val_b = node_b.get(key)
                    if val_a != val_b:
                        if type(val_a) == type(val_b) and isinstance(val_a,(dict,list)) and isinstance(val_b,(dict,list)):
                            # Recurse deeper!
                            differences += self._diff_tracker(val_a,val_b,fresh_path)

                        else:
                            diff_str = f"[CHANGED] Value mismatch at: {pretty_path}: {val_a} -> {val_b}"
                            differences.append(diff_str)

        #  CASE B: Both nodes are LISTS
        elif isinstance(node_a,list) and isinstance(node_b,list):
            max_length = max(len(node_a),len(node_b))

            for index in range(max_length):
                fresh_path = path + [f"[{index}]"]
                pretty_path = " -> ".join(fresh_path)

                # --- COMPARISON SCENARIOS ---
                #SUB-CASE A: Index exists in list A, but is missing in list B (Representing data that was Deleted).
                if len(node_a) > index >= len(node_b):
                    diff_str = f"[DELETED] Missing key in node B at: {pretty_path}"
                    differences.append(diff_str)

                #SUB-CASE B: Index exists in list B but is missing in list A (Representing data that was Added).
                elif len(node_b) > index >= len(node_a):
                    diff_str = f"[ADDED] Added key in node B at: {pretty_path}"
                    differences.append(diff_str)

                #SUB-CASE C: Index exists in both but values do not match (Representing data that was Changed).
                else:
                    item_a = node_a[index]
                    item_b = node_b[index]

                    if item_a != item_b:
                        if type(item_a) == type(item_b) and isinstance(item_a,(dict,list)) and isinstance(item_b,(dict,list)):
                            # Recurse deeper!
                            differences += self._diff_tracker(item_a,item_b,fresh_path)
                        else:
                            diff_str = f"[CHANGED] Value mismatch at: {pretty_path}: {item_a} -> {item_b}"
                            differences.append(diff_str)

        # Case C: Structure Mismatch (One is a dict, one is a list, or a primitive changed to an object)
        elif node_a != node_b:
            pretty_path = " -> ".join(path)
            diff_str = f"[CHANGED] Type mismatch at: {pretty_path}: {type(node_a).__name__} -> {type(node_b).__name__}"
            differences.append(diff_str)

        return differences


