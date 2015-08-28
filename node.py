
class Node(object):
	def __init__(self, name):
		self.node_name = name
		self.incident_vertices= ()

	def __hash__(self):
		return hash(self.node_name)

	def __eq__(self, other_node):
		return isinstance(other_node, Node) and self.node_name == other_node.node_name






				