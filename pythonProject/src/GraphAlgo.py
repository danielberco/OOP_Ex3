from typing import List
from src import GraphInterface


class GraphAlgo(GraphInterface.GraphInteface):

    def get_graph(self) -> GraphInterface:
        raise NotImplementedError

    def load_from_json(self, file_name: str) -> bool:
        raise NotImplementedError

    def save_to_json(self, file_name: str) -> bool:
        raise NotImplementedError

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        raise NotImplementedError

    def connected_component(self, id1: int) -> list:
        raise NotImplementedError

    def connected_components(self) -> List[list]:
        raise NotImplementedError

    def plot_graph(self) -> None:
        raise NotImplementedError
