from unittest import TestCase
from src.GraphAlgo import GraphAlgo
from src.DiGraph import DiGraph


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(True, ga.g == DiGraph())

        ga.g.add_node(0)
        ga.save_to_json("out_file.json")
        self.assertEqual(False, ga.load_from_json("out_file"))
        self.assertEqual(True, ga.load_from_json("out_file.json"))

        self.assertEqual(True, ga.g != DiGraph())

    def test_save_to_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(False, ga.save_to_json("out_file"))
        self.assertEqual(False, ga.save_to_json("out_.json_file"))
        self.assertEqual(True, ga.save_to_json("out_file.json"))

        g.add_node(0)
        self.assertEqual(True, ga.save_to_json("out_file.json"))

    # def test_shortest_path(self):
    #     self.fail()
    #
    # def test_connected_component(self):
    #     self.fail()
    #
    # def test_connected_components(self):
    #     self.fail()
    #
    # def test_plot_graph(self):
    #     self.fail()
