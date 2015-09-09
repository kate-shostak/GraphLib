
class Node(object):
    AUTO_INCREMENTED_ID = 0

    def __init__(self):
        Node.AUTO_INCREMENTED_ID += 1
        self.id = Node.AUTO_INCREMENTED_ID 

    def __add__(self, other):
        return str(self.id) + other

    def __repr__(self):
        return self.id

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other_node):
        return isinstance(other_node, Node) and self.id == other_node.id