import unittest
from random import sample

import networkx

from src.DiGraph import DiGraph, Vertex
from src.GraphAlgo import GraphAlgo
from src.netX import nx


class test_algoGraph_vs_netGraph(unittest.TestCase):
    net = nx()  # our_graph and net_graph
    net.init_graph("C:\\Users\\Ayala\\Downloads\\Graphs_no_pos (1)\\G_10000_80000_0.json")
    # net.graph.add_node(-1)
    net.init_dx_graph(net.graph)
    graph_algo = GraphAlgo(net.graph)

    def test_connected_component_our_graph_runTime(self):
        # self.graph_algo.graph.add_node(-2)
        self.print_list_of_lists_2(self.graph_algo.connected_components())

    def test_connected_component_net_graph_runTime(self):
        # self.graph_algo.graph.add_node(-1)  # adding a new node for checking the connected components
        # self.net.init_dx_graph(self.graph_algo.graph)

        self.print_list_of_lists_2(networkx.strongly_connected_components(self.net.dx_net_graph))

        # print(min(networkx.strongly_connected_components(self.net.dx_net_graph), key=len))

    def test_equals_connectedComponents_our_vs_net_graphs(self):
        len_our = self.graph_algo.connected_components().__len__()
        len_net = (list(networkx.strongly_connected_components(self.net.dx_net_graph))).__len__()
        self.assertEqual(len_our, len_net)
        list_our = sorted(self.graph_algo.connected_components(), key=lambda x: len(x))
        # print(list_our)
        # self.print_list_of_lists(list_our)
        list_net = sorted(networkx.strongly_connected_components(self.net.dx_net_graph), key=lambda x: len(x))

        # print(list_net)
        # this function could be problematic.
        # in case there are two connected components unit with the same length

        for i in range(len_our):
            sub_list_our = list_our[i]
            sub_list_net = list_net[i]
            for j in range(len(sub_list_our)):
                # print(sub_list_our[j].get_id())
                # print(list(sub_list_net)[0])
                self.assertEqual(sub_list_our[j].get_id(), list(sub_list_net)[j])

    # equals between the two path of shortest_path function
    # src = n1
    # dest = n2
    n1 = 1
    n2 = 3

    def test_shortest_equals(self):
        our_path = self.graph_algo.shortest_path(self.n1, self.n2)[1]
        net_path = networkx.shortest_path(self.net.dx_net_graph, self.n1, self.n2, 'weight')
        # print(our_path)
        # print(net_path)

        self.assertEqual(our_path.__len__(), net_path.__len__())
        for i in range(len(our_path)):
            self.assertEqual(our_path[i], net_path[i])

    # checking time of shortest_path our and net functions between two rand nodes:
    two_rand_numbers = sample(graph_algo.graph.get_all_v().keys(), 2)  # list of two random node key from graph

    def test_our_shortest_runTime(self):
        self.graph_algo.shortest_path(self.two_rand_numbers[0], self.two_rand_numbers[1])

    def test_net_shortest_runTime(self):
        networkx.shortest_path(self.net.dx_net_graph, self.two_rand_numbers[0], self.two_rand_numbers[1], 'weight')

    tree_rand_nodes = sample(graph_algo.graph.get_all_v().keys(), 3) # list of tree random key's node from graph
    def test_RunTime_connected_componenet_3nodes(self):
        self.graph_algo.connected_component(self.tree_rand_nodes[0])
        self.graph_algo.connected_component(self.tree_rand_nodes[1])
        self.graph_algo.connected_component(self.tree_rand_nodes[2])

    def test_another_graph(self):
        g = DiGraph()
        self.graph_algo.__init__(g)
        for i in range(5):
            g.add_node(i)
        # self.net.init_graph(g)
        self.net.init_dx_graph(self.graph_algo.get_graph())

        self.test_connected_component_our_graph_runTime()
        self.test_connected_component_net_graph_runTime()
        self.test_equals_connectedComponents_our_vs_net_graphs()

    # print list inside list {[ 2, 3, 5], [6, 7, 9 ]}
    def print_list_of_lists(self, alist):
        print("{ [", '], ['.join(', '.join(map(str, a)) for a in alist), "] }")

    # print list of list [['0', '1', '3'],['4', '5']]
    def print_list_of_lists_2(self, list_of_lists_of_nodes):
        big_list = []
        for grup in list_of_lists_of_nodes:
            list = []
            for node in grup:
                list.append(node.__str__())
            big_list.append(list)
        print(big_list)
