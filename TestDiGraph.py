import unittest

from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_1(self):
        g = DiGraph()  # creates an empty directed graph
        for i in range(6):
            g.add_node(i)
        g.add_edge(0, 1, 1)
        g.add_edge(0, 1, 1.1)
        g.add_edge(5, 2, 7.8)
        g.add_edge(2, 5, 1.1)
        g.add_edge(1, 2, 9)
        g.remove_edge(2, 3)  # does not exist
        g.remove_edge(2, 5)
        g.add_edge(1, 3, 10)
        g.remove_node(1)
        print(g)  # prints the __repr__ (func output)
        self.assertEqual(g.vertex_size, 6)
        #print(g.vertex_size)
        #print(g.edge_size)
        self.assertEqual(g.edge_size, 6)
        print(g.get_all_v())  # prints a dict with all the graph's vertices.
        print(g.all_in_edges_of_node(1))
        print(g.all_out_edges_of_node(1))
        print(g.all_in_edges_of_node(0))
        print(g.all_out_edges_of_node(5))
        print(g.get_mc())


if __name__ == '__main__':
    unittest.main()