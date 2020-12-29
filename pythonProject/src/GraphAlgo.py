from typing import List
import json
from json import JSONEncoder
from src.GraphAlgoInterface import GraphAlgoInterface
from src.DiGraph import DiGraph


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
        return True

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
