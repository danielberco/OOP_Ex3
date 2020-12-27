from unittest import TestCase
from src.NodeDS import NodeDS
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo

class TestDiGraph(TestCase):
    def test_graph(self):
        """
            This function tests the naming (main methods of the DiGraph class, as defined in GraphInterface.
            :return:
            """
        g = DiGraph()  # creates an empty directed graph
        size = 4
        for n in range(size):
            g.add_node(n)
        self.assertEqual(size, g.v_size())
        self.assertIsNone(g.get_node(size))
        g.add_edge(0, 1, 1)
        self.assertEqual(False, g.add_edge(0, 1, 1))
        self.assertEqual(False, g.add_edge(0, 1, 2))
        g.add_edge(1, 0, 1.1)
        g.add_edge(1, 2, 1.3)
        g.add_edge(2, 3, 1.1)
        g.add_edge(1, 3, 1.9)
        g.remove_edge(1, 3)

        g.add_edge(1, 3, 10)
        print(g)  # prints the __repr__ (func output)
        print(g.get_all_v())  # prints a dict with all the graph's vertices.
        print(g.all_in_edges_of_node(1))
        print(g.all_out_edges_of_node(1))
        # g_algo = GraphAlgo(g)
        # print(g_algo.shortest_path(0, 3))

    def test_add_node(self):
        """
        This function tests the addition of a new node
        :return:
        """
        n1 = NodeDS()
        self.assertEqual(0, n1.get_key())
        n2 = NodeDS()
        self.assertEqual(0, n1.get_key())
        self.assertEqual(1, n2.get_key())
