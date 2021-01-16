from typing import List
import json
from json import JSONEncoder
import GraphInterface
from DiGraph import DiGraph
from GraphAlgoInterface import GraphAlgoInterface
from NodeDS import NodeDS

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
        # if 'Edges' in self.json.keys():
        #     pass
            # edges = self.json['Edges']
            # nodes = self.json['Nodes']
            # nodes_moded = {}
            # edges_moded = {}
            # for line in nodes:
            #     nodes_moded[line['id']] = (* line['pos'].split(',')[:2], )
            # self.get_graph().__dict__['nodes'] = nodes_moded
            # for line in edges:
            #     tmp = {}
            #     tmp['key'] = line['src']
            #     tmp['']
            #     edges_moded[line['src']] = tmp
            #     "1": {"key": 1, "neighbours": {"2": 5}, "tag": 5, "r_from": {"key": 0, "neighbours": {"9": 51, "1": 5, "8": 1}, "tag": 0}}
        # else:
        self.get_graph().__dict__.update(self.json)
        # self.change_key_to_int("node_obj", create_obj=True)
        # self.change_key_to_int("nodes")
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
        node_dict1 = self.graph.get_dict(self.graph.Nodes, 'id', id1)
        node_dict2 = self.graph.get_dict(self.graph.Nodes, 'id', id2)
        if node_dict1 is None or node_dict2 is None:
            return float('inf'), None
        taged_nodes = []
        for node in self.graph.Nodes:
            taged_nodes.append({'id': node['id'], 'tag': -1})

        src_node = self.graph.get_dict(taged_nodes, 'id', id1)
        stack = [src_node]
        prev = {}

        # for node_key in self.graph.nodes:
        #     self.graph.nodes.get(node_key).tag = -1
        src_node['tag'] = 0
        while len(stack) > 0:
            node = stack.pop(0)
            for neighbor in self.graph.all_out_edges_of_node(node['id']).keys():
                neighbor_dict = self.graph.get_dict(taged_nodes, 'id', neighbor)
                edge_weight = self.graph.all_out_edges_of_node(node['id'])[neighbor]
                if neighbor_dict['tag'] == -1:
                    taged_nodes.remove(neighbor_dict)
                    neighbor_dict['tag'] = node['tag'] + edge_weight
                    taged_nodes.append(neighbor_dict)
                    prev[neighbor] = node['id']
                    stack.append(neighbor_dict)
                    stack.sort(key=lambda x: x['tag'], reverse=False)
                else:
                    if neighbor_dict['tag'] > node['tag'] + edge_weight:
                        taged_nodes.remove(neighbor_dict)
                        neighbor_dict['tag'] = node['tag'] + edge_weight
                        taged_nodes.append(neighbor_dict)
                        prev[neighbor] = node['id']
                        if neighbor_dict in stack:
                            stack.remove(neighbor_dict)
                        stack.append(neighbor_dict)
                        stack.sort(key=lambda x: x['tag'], reverse=False)
        if id2 not in prev:
            return None
        path = [id2]
        temp_key = id2
        while prev[temp_key] != id1:
            path.append(prev[temp_key])
            temp_key = prev[temp_key]
        path.append(id1)
        path.reverse()
        return self.graph.get_dict(taged_nodes, 'id', id1)['tag'], path

    def connected_component(self, id1: int):
        node_dict = self.graph.get_dict(self.graph.Nodes, 'id', id1)
        if node_dict is None:
            return []
        l_ist = self.Kosaraju(id1)
        return l_ist

    def connected_components(self) -> List[list]:
        if self.graph is None:
            return []
        l_ist = []
        al_inScc = []
        for i in self.graph.Nodes:#.values():
            if i['id'] not in al_inScc:
                l = self.Kosaraju(i['id'])
                for k in l:
                    al_inScc.append(k)
                l_ist.append(l)
        return l_ist

    def plot_graph(self) -> None:
        if len(self.graph.get_all_v()) == 0:
            return

        plt.title("direction weighted graph V={} E={}".format(self.graph.v_size(), self.graph.e_size()))
        x_val = []
        y_val = []
        graph_nodes = {}

        for node in self.graph.Nodes:
            pos = node['pos']
            graph_nodes[node['id']] = (pos[0], pos[1])
            x_val.append(pos[0])
            y_val.append(pos[1])

        plt.plot(x_val, y_val, 'o')
        for key in graph_nodes.keys():
            val = graph_nodes[key]
            x_src = val[0]
            y_src = val[1]
            plt.annotate(key, (x_src - .5, y_src + .5), color='black')
            for neighbour in self.graph.all_out_edges_of_node(key):
                x_e = graph_nodes[neighbour][0]
                y_e = graph_nodes[neighbour][1]
                cmap = plt.cm.get_cmap("hsv", len(graph_nodes))
                plt.arrow(x_src, y_src, x_e-x_src, y_e-y_src, length_includes_head=True, head_width=2,
                          width=.0005, color=cmap(key))
        plt.show()

    def Kosaraju(self, src):
        s = [src]
        visited = {}
        while len(s) > 0:  # DFS Graph
            v = s.pop()
            if v not in visited.keys():
                node_dict = self.graph.get_dict(self.graph.Nodes, 'id', v)
                visited[v] = node_dict
                for edge in self.graph.all_out_edges_of_node(v).keys():
                    s.append(edge)
        visited_2 = {}
        s_2 = [src]
        while len(s_2) > 0:
            v = s_2.pop()
            if v not in visited_2.keys():
                visited_2[v] = self.graph.get_dict(self.graph.Nodes, 'id', v)
                for edge in self.graph.all_in_edges_of_node(v).keys():
                    s_2.append(edge)

        x = set(visited).intersection(visited_2)
        return list(x)
