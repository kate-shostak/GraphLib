from node import Node

class Graph(object):
    def __init__(self):
        self.graph = dict()

    def add_node(self, new_node): 
        if isinstance(new_node, Node):
            self.graph.setdefault(new_node, list())
        else:
            raise NameError("Not a node!")

    def add_incident_vertice(self, node_name, incident_vertice):
        if isinstance(node_name, Node) and isinstance(incident_vertice, Node):
            self.graph[node_name].append(incident_vertice)
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

my_graph.add_incident_vertice(my_node, my_node)
#my_graph.graph["I_am_node_and_I_love_u"]
my_graph.print_graph()