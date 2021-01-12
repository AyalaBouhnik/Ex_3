import networkx as net

from src.DiGraph import DiGraph
from src.GraphAlgo import GraphAlgo


class nx:

    def __init__(self):
        self.graph = self.init_graph()
        self.dx_net_graph = self.init_dx_graph(self.graph)

    def init_dx_graph(self, graph=DiGraph(), dx_graph=net.DiGraph()):
        for node in graph.get_all_v():
            dx_graph.add_node(node)  # id or get_id?
        edge = []
        for node in graph.get_all_v().keys():
            for edgeout in graph.all_out_edges_of_node(node).keys():
                temp = (node, graph.vertex_dict[edgeout].id, graph.all_out_edges_of_node(node)[edgeout])
                edge.append(temp)
        dx_graph.add_weighted_edges_from(edge)
        return dx_graph

    def init_graph(self):
        graph_algo = GraphAlgo()
        graph_algo.load_from_json("C:\\Users\\Ayala\\Desktop\\G_30000_240000_0.json")
        return graph_algo.get_graph()


if __name__ == '__main__':
    g_nx = nx()  # init an empty graph for the GraphAlgo
    net_graph = net.DiGraph()
    net_graph.add_node(2)
    net_graph.add_node(3)
    list = [(3,2,2.0)]
    net_graph.add_weighted_edges_from(list)
    print(net_graph.get_edge_data( 3))
    g_nx.dx_net_graph.copy(g_nx.dx_net_graph)

    n = net
    n.DiGraph.copy(g_nx.dx_net_graph)
    # print(n.Graph.nodes)
    print("this is networkx")
    print(n.shortest_path(G=g_nx.dx_net_graph, source=0, target=20000, weight='weight'))
    short_list = n.shortest_path(G=g_nx.dx_net_graph, source=0, target=20000, weight='weight')
    print(n.DiGraph.edges)
    # print(n.all_shortest_paths(g_nx.dx_net_graph, 0, 1600))
    # print(n.shortest_path(g_nx.dx_net_graph, 0, 2))
    # print(n.connected_components(g_nx.dx_net_graph))
    # list = n.connected_components(g_nx.dx_net_graph)
    # for i in list:
    #     print([])
    #     for j in i:
    #         print(j)

    our_graph = GraphAlgo()
    our_graph.__init__(g_nx.graph)
    print(our_graph.shortest_path(0, 20000))
    # print(our_graph.shortest_path(0,2))
    # print(our_graph.connected_components())

    # list = our_graph.connected_components()
    # for i in list:
    #     print([])
    #     for j in i:
    #         print(j.id)
