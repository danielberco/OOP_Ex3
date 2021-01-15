from unittest import TestCase
from NodeDS import NodeDS
from DiGraph import DiGraph


class TestDiGraph(TestCase):
    def test_v_size(self):
        g = DiGraph()
        self.assertEqual(0, g.v_size())

        g.add_node(0, (0, 0))
        self.assertEqual(1, g.v_size())

        g.remove_node(1)
        self.assertEqual(1, g.v_size())
        g.remove_node(0)
        self.assertEqual(0, g.v_size())

    def test_e_size(self):
        g = DiGraph()
        self.assertEqual(0, g.e_size())

        g.add_edge(0, 1, 5)
        self.assertEqual(0, g.e_size())

        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 5)
        self.assertEqual(1, g.e_size())

        g.remove_edge(1, 0)
        self.assertEqual(1, g.e_size())

        g.remove_edge(0, 1)
        self.assertEqual(0, g.e_size())

    def test_get_all_v(self):
        g = DiGraph()
        self.assertEqual({}, g.get_all_v())

        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual(3, len(g.get_all_v()))

        g.remove_node(2)
        self.assertEqual(2, len(g.get_all_v()))

    def test_all_in_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual({}, g.all_in_edges_of_node(0))
        g.add_edge(1, 0, 5)
        g.add_edge(2, 0, 10)
        g.add_edge(0, 1, 5)
        self.assertEqual({1: 5, 2: 10}, g.all_in_edges_of_node(0))
        g.remove_edge(1, 0)
        self.assertEqual({2: 10}, g.all_in_edges_of_node(0))

    def test_all_out_edges_of_node(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        self.assertEqual({}, g.all_out_edges_of_node(0))
        g.add_edge(1, 0, 2)
        g.add_edge(0, 2, 10)
        g.add_edge(0, 1, 5)
        self.assertEqual({1: 5, 2: 10}, g.all_out_edges_of_node(0))
        g.remove_edge(0, 1)
        self.assertEqual({2: 10}, g.all_out_edges_of_node(0))

    def test_get_mc(self):
        g = DiGraph()
        self.assertEqual(0, g.get_mc())
        g.add_node(0)
        self.assertEqual(1, g.get_mc())
        g.add_node(1)
        self.assertEqual(2, g.get_mc())
        g.add_edge(0, 1, 5)
        self.assertEqual(3, g.get_mc())
        g.remove_node(0)
        self.assertEqual(4, g.get_mc())
        g.add_node(0)
        g.add_edge(0, 1, 5)
        g.remove_edge(0, 1)
        self.assertEqual(7, g.get_mc())

    def test_add_edge(self):
        g = DiGraph()
        self.assertEqual(False, g.add_edge(0, 1, 5))

        g.add_node(0)
        g.add_node(1)
        self.assertEqual(True, g.add_edge(0, 1, 5))
        self.assertEqual(False, g.add_edge(0, 1, 5))
        self.assertEqual(False, g.add_edge(0, 0, 5))

        g.remove_edge(0, 1)
        self.assertEqual(True, g.add_edge(0, 1, 5))

    def test_add_node(self):
        """
        This function tests the addition of a new node
        :return:
        """

        g = DiGraph()
        self.assertEqual(True, g.add_node(0))
        self.assertEqual(False, g.add_node(0))

        g.remove_node(0)
        self.assertEqual(True, g.add_node(0))
        self.assertEqual(False, g.add_node(0))

    def test_remove_node(self):
        g = DiGraph()
        self.assertEqual(False, g.remove_node(0))

        g.add_node(0)
        self.assertEqual(True, g.remove_node(0))
        self.assertEqual(False, g.remove_node(0))

    def test_remove_edge(self):
        g = DiGraph()
        self.assertEqual(False, g.remove_edge(0, 1))

        g.add_node(0)
        g.add_node(1)
        g.add_edge(0, 1, 5)
        self.assertEqual(False, g.remove_edge(1, 0))
        self.assertEqual(True, g.remove_edge(0, 1))
        self.assertEqual(False, g.remove_edge(0, 1))

    def test_remove_node_from_neighbours(self):
        g = DiGraph()
        self.assertEqual(False, g.remove_node_from_neighbours(0))
        g.add_node(0)
        self.assertEqual(True, g.remove_node_from_neighbours(0))
        g.add_node(1)
        g.add_edge(0, 1, 5)
        self.assertEqual(True, g.get_node(0).has_neighbour(1))
        g.remove_node(0)
        self.assertEqual(False, g.remove_node_from_neighbours(0))

    def test_advance_mc(self):
        g = DiGraph()
        self.assertEqual(0, g.mc)

        g.add_node(0)
        g.add_node(1)
        self.assertEqual(2, g.mc)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 5)
        self.assertEqual(3, g.mc)

        g.remove_edge(1, 0)
        g.remove_edge(0, 1)
        g.remove_edge(0, 1)
        self.assertEqual(4, g.mc)

    def test_get_node(self):
        g = DiGraph()
        self.assertIsNone(g.get_node(0))

        g.add_node(0)
        self.assertIsNotNone(g.get_node(0))

        g.remove_node(0)
        self.assertIsNone(g.get_node(0))

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
