from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(True, ga.get_graph() == DiGraph())

        ga.get_graph().add_node(0)
        ga.save_to_json("out_file.json")
        self.assertEqual(False, ga.load_from_json("out_file"))
        self.assertEqual(True, ga.load_from_json("out_file.json"))
        self.assertEqual(True, g != DiGraph())

        g2 = DiGraph()
        g2.add_node(0)
        self.assertEqual(True, g == g2)

    def test_save_to_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(False, ga.save_to_json("out_file"))
        self.assertEqual(False, ga.save_to_json("out_.json_file"))
        self.assertEqual(True, ga.save_to_json("out_file.json"))

        g.add_node(0)
        self.assertEqual(True, ga.save_to_json("out_file.json"))

    def test_shortest_path(self):
        g = DiGraph()
        ga = GraphAlgo(g)

        w = 5
        r = 10

        g.add_edge(0, 9, w * r + 1)
        length, path = ga.shortest_path(0, 9)
        self.assertEqual((r - 1) * w, length)

        for i in range(0, r):
            g.add_node(i)
        for i in range(0, r - 1):
            g.add_edge(i, i + 1, w)


        length, path = ga.shortest_path(0, 9)
        self.assertEqual((r-1)*w, length)

        g.add_edge(0, 8, 1)
        self.assertEqual(w+1, length)

    def test_connected_component(self):
        return NotImplemented

    def test_connected_components(self):
        return NotImplemented

    def test_plot_graph(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1, (0, 0))
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)

        g.add_edge(0, 1, 5)
        g.add_edge(0, 2, 5)
        g.add_edge(0, 5, 5)
        g.add_edge(3, 4, 5)
        g.add_edge(4, 1, 5)
        # g.add_node(1, (1, -1))
        ga = GraphAlgo(g)

        ga.plot_graph()

