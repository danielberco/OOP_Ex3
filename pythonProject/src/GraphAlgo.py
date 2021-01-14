from typing import List
import json
from json import JSONEncoder
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.NodeDS import NodeDS

import heapq
import queue
import math
import numpy as np
import matplotlib.pyplot as plt
import random


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, graph: DiGraph = DiGraph()):
        self.graph = graph
        self.string = "Graph"

    def get_graph(self) -> GraphInterface:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        if not self.is_json_file(file_name):
            return False
        try:
            with open(file_name, 'r') as out:
                self.json = json.load(out)
        except FileNotFoundError:
            return False
        self.get_graph().__dict__.update(self.json)
        self.change_key_to_int("node_obj", create_obj=True)
        self.change_key_to_int("nodes")
        return True

    def change_key_to_int(self, dict_name, create_obj=False) -> None:
        sub_dict = self.get_graph().__dict__[dict_name]
        tmp_dict = {}
        for k in sub_dict.keys():
            if create_obj:
                tmp_dict[ord(k) - 48] = NodeDS(self.get_graph().__dict__[dict_name][k])
            else:
                tmp_dict[ord(k) - 48] = sub_dict[k]
        del sub_dict
        self.get_graph().__dict__[dict_name] = {}
        self.get_graph().__dict__[dict_name].update(tmp_dict)

    def save_to_json(self, file_name: str) -> bool:
        """
        Saves the graph in JSON format to a file
        @param file_name: The path to the out file
        @return: True if the save was successful, Flase o.w.
        """
        self.json = self.get_graph().__dict__
        if not self.is_json_file(file_name):
            return False
        with open(file_name, 'w') as out:
            json.dump(self.json, out, cls=MyEncoder)
        return True

    @staticmethod
    def is_json_file(file_name: str) -> bool:
        if ".json" not in file_name:
            return False
        if file_name[-5:] not in ".json":
            return False
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        if id1 not in self.graph.node_obj.keys() or id2 not in self.graph.node_obj.keys():
            return float('infinity'), []
        self.Dijkstra(id1)
        ls = []
        if self.graph.node_obj.get(id2).tag == float('infinity'):
            return float('infinity'), ls
        form = id2
        ls.append(form)
        while id1 not in ls:
            ls.append(self.graph.node_obj.get(form).r_from.key)
            form = self.graph.node_obj.get(form).r_from.key
        ls.reverse()
        return self.graph.node_obj.get(id2).tag, ls

    def connected_component(self, id1: int):
        if id1 not in self.graph.node_obj.keys() or self.graph is None:
            return []
        l_ist = self.Kosaraju(id1)
        return l_ist

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        l_ist = []
        al_inScc = []
        for i in self.graph.node_obj.values():
            if i.key not in al_inScc:
                l = self.Kosaraju(i.key)
                for k in l:
                    al_inScc.append(k)
                l_ist.append(l)
        return l_ist

    def plot_graph(self) -> None:
        plt.title(self.string)
        x_vals = []
        y_vals = []
        if len(self.graph.get_all_v()) == 0:
            return

        for val in self.graph.nodes.values():
            if val is None:
                # xy.pos = (random.randrange(0, 100), random.randrange(0, 100), 0)
                x_vals.append(random.randrange(0, 100))
                y_vals.append(random.randrange(0, 100))
            else:
                x_vals.append(val[0])
                y_vals.append(val[1])

        plt.plot(x_vals, y_vals, 'o')
        # for v in self.graph.node_obj.values():
        #     v_x = float(v.pos[0])
        #     v_y = float(v.pos[1])
        #     plt.annotate(v.key, (v_x - 0.00015, v_y + 0.00015), color='red')
        #     for e in self.graph.EdgesSrc[v.key].values():
        #         x_e = float(self.graph.node_obj[e.dst].pos[0])
        #         y_e = float(self.graph.node_obj[e.dst].pos[1])
        #
        #         plt.arrow(v_x, v_y, x_e - v_x, y_e - v_y, length_includes_head=True, head_width=0.0001991599,
        #                   width=0.0000005, color='blue')

        plt.show()

    def Dijkstra(self, src):
        for vertex in self.graph.node_obj.values():
            vertex.tag = float('infinity')
        self.graph.node_obj.get(src).tag = 0
        pq = [self.graph.node_obj.get(src)]
        visited = [src]
        while len(pq) > 0:
            node = pq.pop(0)
            # for neighbor in self.graph.EdgesSrc[node.key].values():
            for neighbor, n_weight in node.get_neighbours().values():
                weight = node.tag + n_weight
                if weight < self.graph.node_obj.get(neighbor.dst).tag:
                    self.graph.node_obj.get(neighbor.dst).tag = weight
                    self.graph.node_obj.get(neighbor.dst).r_from = node
                    if neighbor.dst not in visited:
                        pq.append(self.graph.node_obj.get(neighbor.dst))
                        visited.append(neighbor.dst)

        return

    def Kosaraju(self, src):
        s = [src]
        visited = {}
        while len(s) > 0:  # DFS Graph
            v = s.pop()
            if v not in visited.keys():
                visited[v] = self.graph.node_obj[v]
                for edge in self.graph.EdgesSrc[v].values():
                    s.append(edge.dst)
        visited_2 = {}
        s_2 = [src]
        while len(s_2) > 0:
            v = s_2.pop()
            if v not in visited_2.keys():
                visited_2[v] = self.graph.node_obj[v]
                for edge in self.graph.EdgesDst[v].values():
                    s_2.append(edge.dst)

        x = set(visited).intersection(visited_2)
        return list(x)
