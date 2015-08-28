import node

class Graph():
	def __init__(self):
		self.graph = {}

	def add_node(self, new_node, incident_nodes):
		self.graph[new_node] = incident_nodes
		for node in incident_nodes:
			self.graph.setdefault(node, list()).append(new_node)
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


testGraph = Graph()
testGraph.add_node('a', ['b','c'])
testGraph.add_node('f', 'b')
testGraph.add_node('')