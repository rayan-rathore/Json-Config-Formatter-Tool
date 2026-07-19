# Counts objects, arrays, keys, values, and max nesting depth
class JSONAnalyzer:

    def __init__(self):
        self._reset_trackers()

    def _reset_trackers(self):
        self.total_objects = 0
        self.total_arrays = 0
        self.total_keys = 0
        self.total_values = 0
        self.max_depth = 0

    def analyze_structure(self, data):
        self._reset_trackers()
        self.traverse_explorer(data,current_depth=1)
        return {
            "total_objects" : self.total_objects,
            "total_arrays" : self.total_arrays,
            "total_keys" : self.total_keys,
            "total_values" : self.total_values,
            "max_depth" : self.max_depth
        }

    def traverse_explorer(self, current_node, current_depth):
        if current_depth > self.max_depth:
            self.max_depth = current_depth

        # ---Case A: SIMPLE VALUE---
        primitives = (str, int, float, bool, type(None))
        if isinstance(current_node, primitives):
            self.total_values += 1

        #---Case B: DICTIONARY---
        elif isinstance(current_node, dict):
            self.total_objects += 1
            for key,value in current_node.items():
                self.total_keys += 1
                self.traverse_explorer(value,current_depth+1)

        #---Case C: AN ARRAY---
        elif isinstance(current_node, list):
            self.total_arrays += 1
            for element in current_node:
                self.traverse_explorer(element,current_depth+1)

