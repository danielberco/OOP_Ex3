from src import GraphInterface
from src.NodeDS import NodeDS


class DiGraph(GraphInterface.GraphInteface):
    nodes = {}  # key is int, value tuple of int and float
    node_obj = {}
    mc = 0
    v_size = 0
    edge_size = 0

    def v_size(self) -> int:
        # return self.v_size
        return len(self.nodes)

    def e_size(self) -> int:
        return self.e_size

    def get_all_v(self) -> dict:  # key int value obj
        return self.node_obj

    def all_in_edges_of_node(self, id1: int) -> dict:  # key int value float
        tmp = {}
        for val in self.node_obj.values():
            if val.has_neighbour(id1):
                tmp[val.get_key()] = val.get_weight(id1)
        return tmp

    def all_out_edges_of_node(self, id1: int) -> dict:  # key int value float
        return self.node_obj[id1].get_neighbours()

    def get_mc(self) -> int:
        return self.mc

    def add_edge(self, id1: int, id2: int, weight: float) -> bool:
        if id1 not in self.node_obj or id2 not in self.node_obj:
            return False
        if not self.node_obj[id1].add_neighbour(id2, weight):
            return False
        self.advance_e()
        return True

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.nodes:
            return False
        self.nodes[node_id] = pos
        self.node_obj[node_id] = NodeDS()
        self.advance_mc()
        return True

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        if not self.remove_node_from_neighbours(node_id):
            return False
        del self.nodes[node_id]
        del self.node_obj[node_id]
        self.advance_mc()
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if node_id1 not in self.nodes:
            return False
        if node_id2 not in self.nodes:
            return False
        self.node_obj[node_id1].remove_neighbour(node_id2)
        self.edge_size -= 1
        self.advance_mc()
        return True

    def remove_node_from_neighbours(self, node_id: int) -> bool:
        if node_id not in self.nodes:
            return False
        for val in self.node_obj.values():
            val.remove_neighbour(node_id)
        return True

    def advance_mc(self):
        self.mc += 1

    def advance_e(self):
        self.edge_size += 1
        self.advance_mc()

    def get_node(self, id: int) -> NodeDS:
        if id not in self.node_obj:
            return None
        return self.node_obj[id]