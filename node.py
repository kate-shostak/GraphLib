
class Node(object):
	def __init__(self, name):
		self.node_name = name
		self.incident_vertices= ()

	def __eq__(self, other_node):
		return isinstance(other_node, self.__name__) and self.node_name == other_node.node_name






		