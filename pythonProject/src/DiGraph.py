import random
from typing import List
import GraphInterface


class DiGraph(GraphInterface.GraphInteface):

    def __init__(self):
        self.Edges = []
        self.Nodes = []
        self.mc = 0

    """
    code from https://stackoverflow.com/questions/390250/elegant-ways-to-support-equivalence-equality-in-python-classes
    """

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def nodeAsObj(self, other) -> bool:
        return True in set(isinstance(v, NodeDS) for v in other.__dict__["node_obj"].values())

    def __ne__(self, other):
        return not self.__eq__(other)

    def v_size(self) -> int:
        return len(self.Nodes)

    def e_size(self) -> int:
        return len(self.Edges)

    def get_all_v(self) -> dict:
        # return { self.Nodes : 5 for i in listOfStr }
        return {node['id']: node for node in self.Nodes}
        # return self.Nodes  # {id, pos}

    def all_in_edges_of_node(self, id1: int) -> dict:
        tmp = {}
        for edge in self.Edges:
            if edge['dest'] == id1:
                tmp.update({edge['src']: edge['w']})
        return tmp

    def all_out_edges_of_node(self, id1: int) -> dict:
        tmp = {}
        for edge in self.Edges:
            if edge['src'] == id1:
                tmp.update({edge['dest']: edge['w']})
        return tmp

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 == id2:
            return False
        node_dict1 = self.get_dict(self.Nodes, 'id', id1)
        node_dict2 = self.get_dict(self.Nodes, 'id', id2)
        if node_dict1 is None or node_dict2 is None:
            return False
        edge_dict = self.get_dict(self.Edges, 'src', id1, 'dest', id2)
        if edge_dict is not None:
            return False
        self.Edges.append({'src': id1, 'w': weight, 'dest': id2})

        self.advance_mc()
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        dict_entry = self.get_dict(self.Nodes, 'id', node_id)
        if dict_entry is not None:
            return False
        if pos is None:
            pos = (random.randrange(0, 100), random.randrange(0, 100))
        self.Nodes.append({'id': node_id, 'pos': pos})
        self.advance_mc()
        return True

    def remove_node(self, node_id: int) -> bool:
        dict_entry = self.get_dict(self.Nodes, 'id', node_id)
        if dict_entry is None:
            return False
        self.remove_node_from_neighbours(node_id)
        self.Nodes.remove(dict_entry)
        self.advance_mc()
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        node_dict1 = self.get_dict(self.Nodes, 'id', node_id1)
        node_dict2 = self.get_dict(self.Nodes, 'id', node_id2)
        if node_dict1 is None or node_dict2 is None:
            return False
        edge_dict = self.get_dict(self.Edges, 'src',  node_id1, 'dest', node_id2)
        if edge_dict is None:
            return False
        self.Edges.remove(edge_dict)
        self.advance_mc()
        return True

    def remove_node_from_neighbours(self, node_id: int) -> bool:
        node_dict = self.get_dict(self.Nodes, 'id', node_id)
        if node_dict is None:
            return False
        to_remove = []
        for edge in self.Edges:
            if edge['src'] == node_id or edge['dest'] == node_id:
                to_remove.append(edge)
        for edge in to_remove:
            self.Edges.remove(edge)
        return True

    def advance_mc(self):
        self.mc += 1

    # def get_node(self, node_id: int) -> NodeDS:
    #     return self.get_dict(self.Nodes, 'id', node_id)

    @staticmethod
    def get_dict(list_name: List, key: str, val: int, key2=None, val2=None):
        if key2 is None:
            key2 = key
        if val2 is None:
            val2 = val
        for dict_entry in list_name:
            if dict_entry[key] == val and dict_entry[key2] == val2:
                return dict_entry
        return None

    def has_edge(self, src: int, dest: int):
        if self.get_dict(self.Edges, 'src', src, 'dest', dest) is None:
            return False
        return True
