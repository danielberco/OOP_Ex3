from typing import List
import json
from json import JSONEncoder
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph
from src.NodeDS import NodeDS


class MyEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


class GraphAlgo(GraphAlgoInterface):
    def __init__(self, g: DiGraph):
        self.g = g
        self.json = {}

    def load_from_json(self, file_name: str) -> bool:
        try:
            with open(file_name, 'r') as out:
                self.json = json.load(out)
        except FileNotFoundError:
            return False
        self.g.__dict__.update(self.json)
        self.change_key_to_int("node_obj", create_obj=True)
        self.change_key_to_int("nodes")
        return True

    def change_key_to_int(self, dict_name, create_obj=False) -> None:
        sub_dict = self.g.__dict__[dict_name]
        tmp_dict = {}
        for k in sub_dict.keys():
            if create_obj:
                tmp_dict[ord(k) - 48] = NodeDS(self.g.__dict__[dict_name][k])
            else:
                tmp_dict[ord(k) - 48] = sub_dict[k]
        del sub_dict
        self.g.__dict__[dict_name] = {}
        self.g.__dict__[dict_name].update(tmp_dict)

    def save_to_json(self, file_name: str) -> bool:
        self.json = self.g.__dict__
        if ".json" not in file_name:
            return False
        if file_name[-5:] not in ".json":
            return False
        with open(file_name, 'w') as out:
            json.dump(self.json, out, cls=MyEncoder)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        """
        implementation of Dijkstra's algorithm
        """
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
