from unittest import TestCase
from src.NodeDS import NodeDS


class TestNodeDS(TestCase):
    def test_reset(self):
        NodeDS.reset()
        n1 = NodeDS()
        self.assertEqual(0, n1.get_key())
        NodeDS.reset()
        n2 = NodeDS()
        self.assertEqual(0, n1.get_key())

    def test_get_key(self):
        NodeDS.reset()
        n1 = NodeDS()
        self.assertEqual(0, n1.get_key())
        n2 = NodeDS()
        self.assertEqual(0, n1.get_key())
        self.assertEqual(1, n2.get_key())

    # def test_get_weight(self):
    #     self.fail()

    def test_has_neighbour(self):
        NodeDS.reset()
        n1 = NodeDS()
        n2id = 1
        n1.add_neighbour(n2id, 1)
        self.assertEqual(True, n1.has_neighbour(n2id))
        n1.add_neighbour(n2id, 1)
        self.assertEqual(True, n1.has_neighbour(n2id))
        n1.add_neighbour(n2id, 2)
        self.assertEqual(True, n1.has_neighbour(n2id))
        n1.remove_neighbour(n2id)
        n1.add_neighbour(n2id, 1)
        self.assertEqual(True, n1.has_neighbour(n2id))

    def test_add_neighbour(self):
        NodeDS.reset()
        n1 = NodeDS()
        n2id = 1
        self.assertEqual(True, n1.add_neighbour(n2id, 1))
        self.assertEqual(False, n1.add_neighbour(n2id, 1))
        self.assertEqual(False, n1.add_neighbour(n2id, 2))
        n1.remove_neighbour(n2id)
        self.assertEqual(True, n1.add_neighbour(n2id, 1))

    def test_remove_neighbour(self):
        NodeDS.reset()
        n1 = NodeDS()
        self.assertEqual(False, n1.remove_neighbour(n1.get_key()))
        self.assertEqual(False, n1.remove_neighbour(n1.get_key()+1))

        n1.add_neighbour(1, 1)
        self.assertEqual(True, n1.remove_neighbour(1))
        self.assertEqual(False, n1.remove_neighbour(1))

    # def test_get_neighbours(self):
    #     self.fail()
