import unittest
from graph import Graph
from node import Node
import pdb

class TestGraph(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.node_1_id = 1
        self.node_2_id = 2
        self.node_to_test_1 = Node()
        self.node_to_test_2 = Node()

    def test_init_without_args(self):
        self.assertEqual(self.node_to_test_1.id, self.node_1_id)

    def test_id_incrementation(self):
        self.assertEqual(self.node_to_test_1.id, self.node_1_id)
        self.assertEqual(self.node_to_test_2.id, self.node_2_id)
        
    def test_ad(self):
        string_to_add = "potato"
        resulting_sting = "1 potato"

        self.assertEqual(self.node_to_test_1 + " " + string_to_add, resulting_sting)



if __name__ == '__main__':
    unittest.main()
        

