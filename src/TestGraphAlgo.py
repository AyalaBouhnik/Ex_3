import unittest
from random import sample

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo
from src.netX import nx


class TestGraphAlgo(unittest.TestCase):

    net = nx()  # our_graph and net_graph
    file = "C:\\Users\\Ayala\\Desktop\\G_30000_240000_0.json"
    net.init_graph("C:\\Users\\Ayala\\Desktop\\G_30000_240000_0.json")
    # net.graph.add_node(-1)
    net.init_dx_graph(net.graph)
    graph_algo = GraphAlgo(net.graph)
    print(file)
    two_rand_numbers = sample(graph_algo.graph.get_all_v().keys(), 2)  # list of two random node key from graph
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
        # self.assertEquals(None, g.shortestPath(0, 1))
        # self.assertEquals(0, g.shortestPath(0, 0).get(0).getKey())
        # self.assertEquals(1, g.shortestPath(0, 0).size())
        # self.assertEquals(0, g.shortestPathDist(0, 0))
        # self.assertEquals(-1, g.shortestPathDist(1, 1))
        #
        # self.assertEqual(g.shortest_path(0, 1).__len__(), g.shortest_path(0, 1)[1].__len__())
        # self.assertEqual(g.shortest_path(0, 1).__len__(), g.shortest_path(0, 1)[1].__len__())
        # self.assertEqual(g.shortest_path(5, 2).__len__(), g.shortest_path(5, 2)[1].__len__())

    def test_connected_component_our_graph_runTime(self):
        # self.graph_algo.graph.add_node(-2)
        self.print_list_of_lists_2(self.graph_algo.connected_components())

    def test_our_shortest_runTime(self):
        self.graph_algo.shortest_path(self.two_rand_numbers[0], self.two_rand_numbers[1])

    # print list of list [['0', '1', '3'],['4', '5']]
    def print_list_of_lists_2(self, list_of_lists_of_nodes):
        big_list = []
        for grup in list_of_lists_of_nodes:
            list = []
            for node in grup:
                list.append(node.__str__())
            big_list.append(list)
        print(big_list)




