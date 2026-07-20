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
        # CASE A: If the node is a DICTIONARY
        if isinstance(current_node,dict):
            # Convert the dictionary items into a list of pairs so we can count them
            pairs_list = list(current_node.items())
            total_items = len(pairs_list)
            # Loop through each key-value pair using its index position
            for index,(key, value) in enumerate(pairs_list):
                # Determine if this pair is the absolute LAST item in the dictionary
                is_last = (index == total_items-1)
                # Assign branches and prefixes based on position
                if is_last:
                    branch = "└── "  #(Final Corner Branch)
                    child_prefix_extension = "    "
                else:
                    branch = "├── " #(Middle Branch)
                    child_prefix_extension = "│   "#(Vertical Connector Space Guide)
                # Check the type of the child 'value'
                # If the child 'Value' is a primitive (string, number, boolean, null):
                if isinstance(value,(str,int,float,bool,type(None))):
                    print(prefix + branch + key + ": " + str(value))
                # If the child 'Value' is another dictionary or list:
                elif isinstance(value, (dict,list)):
                    print(prefix + branch + key)
                    # Recurse! Call _paint_node
                    self._paint_node(value,prefix + child_prefix_extension)

        # CASE B: If the node is a LIST
        elif isinstance(current_node,list):
            total_items = len(current_node)
            # Loop through every element using its index number
            for index, element in enumerate(current_node):
                # Determine if this element is the absolute LAST item in the list
                is_last = (index == total_items-1)
                # Pick the correct branch shape and child prefix extension
                if is_last:
                    branch = "└── "  #(Final Corner Branch)
                    child_prefix_extension = "    "
                else:
                    branch = "├── " #(Middle Branch)
                    child_prefix_extension = "│   "#(Vertical Connector Space Guide)
                # Format the item name as an index enclosed in brackets, e.g., "[0]"
                item_name = f"[{index}]"
                # if The element is a simple piece of data
                if isinstance(element, (str, int, float, bool, type(None))):
                    print(prefix + branch + item_name + ": " + str(element))
                # if The element is a nested dictionary or list
                elif isinstance(element, (dict, list)):
                    print(prefix + branch + item_name)
                    # Recurse! Pass the accumulated prefix down
                    self._paint_node(element,prefix + child_prefix_extension)