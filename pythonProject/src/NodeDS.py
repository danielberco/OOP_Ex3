class NodeDS:
    neighbours = {}  # key is int, value is float
    key_counter = 0

    def __init__(self):
        self.key = NodeDS.key_counter
        NodeDS.key_counter = NodeDS.key_counter + 1

    def get_key(self):
        return self.key

    def get_weight(self, node: int):
        if node not in self.neighbours:
            return -1
        return self.neighbours[node]

    def has_neighbour(self, key: int) -> bool:
        return key in self.neighbours

    def add_neighbour(self, key: int, weight: float) -> bool:
        if self.has_neighbour(key):  # change to update weight?
            return False
        self.neighbours[key] = weight
        return True

    def remove_neighbour(self, key: int) -> bool:
        if not self.has_neighbour(key):
            return False
        del self.neighbours[key]
        return True

    def get_neighbours(self) -> dict:
        return self.neighbours
