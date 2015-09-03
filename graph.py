from node import Node

class Graph(object):
	def __init__(self):
		self.graph = list()

	def add_node(self, new_node): 
		if isinstance(new_node, Node):
			self.graph.append(new_node)
		else:
			raise NameError("Not a node!")
	
	def print_graph(self):
		print self.graph

	def delete_node(self):
		pass
	def find_node(self):
		pass
	def walk_graph(self, func):
		pass
	def show_graph(self):
		pass
	def show_nodes(self):
		pass
	def show_edeges(self, node):
		pass

my_node = Node("I_am_node_and_I_love_u")
my_graph = Graph()
my_graph.add_node(my_node)
my_graph.print_graph()
