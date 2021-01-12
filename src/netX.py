import networkx as net

from networkx.readwrite import json_graph
from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class nx:

    def __init__(self):
        # self.g = self.init_graph()
        self.graph = self.init_graph()
        self.dx_net_graph = self.init_dx_graph(self.graph)
        # self.net_graph = net.Graph()
        # self.init_dx_graph(self.g, self.net_graph)

    def init_dx_graph(self, graph=DiGraph(), dx_graph=net.Graph()):
        for node in graph.get_all_v():
            dx_graph.add_node(node)  # id or get_id?
        edge = []
        for node in graph.get_all_v().keys():
            for edgeout in graph.all_out_edges_of_node(node).keys():
                temp = (node, graph.vertex_dict[edgeout].id, graph.all_out_edges_of_node(node)[edgeout])
                edge.append(temp)
                # edge.update(node.id, edgeout[0], edgeout[1])
                # edge = (node, edgeout[0], edgeout[1])
        dx_graph.add_weighted_edges_from(edge)

        return dx_graph

    def init_graph(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("C:\\Users\\Ayala\\Desktop\\file.json")
        # print(graph_algo.get_graph())  # an address
        return graph_algo.get_graph()

        # print(nx.our_load_nx().connected_components)

    # ver = nx
    # My_graph= DiGraph()
    #
    # def __init__(self):
    #     self.vertax = {}
    #     self.in_ni={}
    #     self.out_ni={}
    #     self.My_graph= DiGraph()
    #
    # def load(self):
    #     for i in self.My_graph.get_all_v():
    #         self.vertax.update(i)
    #         for j in self.My_graph.get_all_v().:
    #             self.out_ni.update(i)


if __name__ == '__main__':
    g_nx = nx()  # init an empty graph for the GraphAlgo
    net_graph = net.Graph()
    net_graph.add_node(2)
    net_graph.add_node(3)
    list = [(2,3,0.5)]
    net_graph.add_weighted_edges_from(list)
    print(net_graph.get_edge_data(2,3))
    print(g_nx.dx_net_graph.edges)
    print(g_nx.dx_net_graph.nodes)
    g_nx.dx_net_graph.copy(g_nx.dx_net_graph)

    n = net
    n.Graph.copy(g_nx.dx_net_graph)
    # print(n.Graph.nodes)
    print(n.shortest_path(g_nx.dx_net_graph, 0, 3))
    print(n.shortest_path(g_nx.dx_net_graph, 0, 2))
    print(n.connected_components(g_nx.dx_net_graph))
    list = n.connected_components(g_nx.dx_net_graph)
    for i in list:
        print([])
        for j in i:
            print(j)


    our_graph=GraphAlgo()
    our_graph.__init__(g_nx.graph)
    print(our_graph.shortest_path(0,3))
    print(our_graph.shortest_path(0,2))
    print(our_graph.connected_components())

    list = our_graph.connected_components()
    for i in list:
        print([])
        for j in i:
            print(j.id)



