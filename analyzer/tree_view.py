# Generates the visual terminal branch tree structural view
"""
├──  (Middle Branch)
│    (Vertical Connector Space Guide)
└──  (Final Corner Branch)
"""

class JSONTreeGenerator:

    def generate_tree(self, data):
        print(".")
        self._paint_node(data,"")


    def _paint_node(self,current_node, prefix):
        if isinstance(current_node,dict):
            pairs_list = list(current_node.items())
            

