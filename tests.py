import unittest
from graph import Graph
from node import Node

class TestGraph(unittest.TestCase):

	def test_init(self):
		node_name  = "Tux"
		node_id = 1

		node = Node(node_name)
		self.assertEqual(node.node_name, node_name)
		self.assertEqual(node.id, node_id)

if __name__ == '__main__':
    unittest.main()
		

