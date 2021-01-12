import unittest

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class TestGraphAlgo(unittest.TestCase):

    def test_1(self):
        g = DiGraph()  # creates an empty directed graph
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)                                      #0---->1
        g.add_edge(0, 1, 1.1)
        g.add_edge(5, 2, 7.8)                                    #5---->2
        g.add_edge(2, 5, 1.1)                                    #2---->5- removed
        g.add_edge(1, 2, 9)                                      #1-----2
        g.add_edge(1, 3, 10)                                     #1----_>3
        g = GraphAlgo()
        self.assertEquals(None, g.shortestPath(0, 1))
        self.assertEquals(0, g.shortestPath(0, 0).get(0).getKey())
        self.assertEquals(1, g.shortestPath(0, 0).size())
        self.assertEquals(0, g.shortestPathDist(0, 0))
        self.assertEquals(-1, g.shortestPathDist(1, 1))

        self.assertEqual(g.shortest_path(0, 1).__len__(), g.shortest_path(0, 1)[1].__len__())
        # self.assertEqual(g.shortest_path(0, 1).__len__(), g.shortest_path(0, 1)[1].__len__())
        # self.assertEqual(g.shortest_path(5, 2).__len__(), g.shortest_path(5, 2)[1].__len__())


