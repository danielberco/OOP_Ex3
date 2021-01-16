from unittest import TestCase
from GraphAlgo import GraphAlgo
from DiGraph import DiGraph


class TestGraphAlgo(TestCase):
    def test_load_from_json(self):
        g = DiGraph()
        ga = GraphAlgo(g)
        self.assertEqual(True, ga.get_graph() == DiGraph())

        ga.get_graph().add_node(0)
        ga.save_to_json("out_file.json")
        self.assertEqual(False, ga.load_from_json("out_file"))
        # self.assertEqual(True, ga.load_from_json("out_file.json"))
        # self.assertEqual(True, g != DiGraph())

        # g2 = DiGraph()
        # g2.add_node(0)
        # self.assertEqual(True, g == g2)
        self.assertEqual(True, ga.load_from_json("C:/Users/mthee/repos/OOP_Ex3/Graphs_on_circle/G_20000_160000_1.json"))

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
        length, path = ga.shortest_path(0, 9)
        self.assertEqual(float('inf'), length)

        for i in range(0, r):
            g.add_node(i)
        l = w * r + 1
        g.add_edge(0, 9, l)
        length, path = ga.shortest_path(0, 9)
        self.assertEqual(l, length)

        for i in range(0, r):
            g.add_node(i)
        for i in range(0, r - 1):
            g.add_edge(i, i + 1, w)

        length, path = ga.shortest_path(0, 9)
        self.assertEqual((r-1)*w, length)

        g.add_edge(0, 8, 1)
        length, path = ga.shortest_path(0, 9)
        self.assertEqual(w+1, length)
        # ga.save_to_json("gg.json")

    def test_connected_component(self):
        """
        run by func2 and check the connected_component by each node in the graph.
        This functions tests the connected_component function for the class DiGraph
        """
        self.func2()
        my_list = [[0, 1, 2, 3, 4, 5, 6], [8], [9]]
        i = 0

        for x in self.list_graph[0].get_all_v().values():
            if i < 7:
                self.assertEqual(my_list[0], self.list_algo[0].connected_component(x['id']))
            if i == 7:
                self.assertEqual(my_list[1], self.list_algo[0].connected_component(x['id']))

            if i == 8:
                self.assertEqual(my_list[2], self.list_algo[0].connected_component(x['id']))
            i += 1

    def test_connected_components(self):
        """
                run by func2 and check the connected_components of the graph.
                This functions tests the connected_components function for the class DiGraph
                """
        self.func2()
        my_list = [[0, 1, 2, 3, 4, 5, 6], [8], [9]]
        self.assertEqual(my_list, self.list_algo[0].connected_components())

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

    def func2(self):
        """
        create specific graph for some tests.
        with 9 vertex.
        """
        graph = DiGraph()
        for x in range(7):
            graph.add_node(x)
        for x in graph.get_all_v().values(): #.get_all_values():
            graph.add_edge(x['id'], x['id'] + 1, x['id'] + 1)
            graph.add_edge(x['id'], x['id'] - 1, x['id'] + 1)

        graph.add_node(8)
        graph.add_node(9)
        algo = GraphAlgo(graph)
        algo.plot_graph()
        str1 = "{}".format(algo.get_graph())
        # str2 = "{}".format(graph.toStringInAndOut())
        print(str1)
        # print(str2)
        self.list_algo = []
        self.list_graph = []
        self.list_algo.append(algo)
        self.list_graph.append(algo.get_graph())

