import unittest
from src.services import DijkstraAlgorithm

class TestServices(unittest.TestCase):
    def test_basic(self):
        dijkstra = DijkstraAlgorithm(3, [[0,1,100],[1,2,100],[0,2,500]])
        self.assertEqual(dijkstra.priority_queue(0, 2, 1), 200)

    def test_zero_stops(self):
        dijkstra = DijkstraAlgorithm(3, [[0,1,100],[1,2,100],[0,2,500]])
        self.assertEqual(dijkstra.priority_queue(0, 2, 0), 500)

    def test_no_path(self):
        dijkstra = DijkstraAlgorithm(3, [[0,1,100],[1,0,100]])
        self.assertEqual(dijkstra.priority_queue(0, 2, 1), -1)
