from node import Node
from collections import defaultdict
i = 0
class Graph(object):
	def __init__(self):
		self.graph = defaultdict(list)

	def add_node(self, new_node):
		global i 
		if isinstance(new_node, Node):
			self.graph[new_node] = i
			i += 1
		else:
			raise NameError("Not a node!")
	
	def print_graph(self):
		for node in self.graph:
			print node + ":" + str(self.graph[node])

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
my_node1 = Node("I_am_node_and_I_love_u")
my_graph = Graph()
my_graph.add_node(my_node)
my_graph.add_node(my_node1)
my_graph.print_graph()
