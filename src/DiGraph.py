from collections import defaultdict


class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    # def get_connections(self):
    #   return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]


from GraphInterface import GraphInteface
from DiGraph import Vertex


class DiGraph(GraphInteface):
    vertex_dict = {}  # list of nodes
    out_ni = {}
    in_ni = {}
    changes = 0

    def __init__(self, edge_size=0, vertex_size=0, changes=0, out_ni={}, in_ni={},vertex_dict={}):  # check if needs to be None
        self.vertex_dict = vertex_dict
        self.out_ni = out_ni
        self.in_ni = in_ni
        self.vertex_size = vertex_size
        self.edge_size = edge_size
        self.changes = changes
        # self.graph = defaultdict(list)  # default dictionary to store graph


    # def __iter__(self):
    #   return iter(self.vert_dict.values())

    def add_node(self, node_id: int, pos: tuple = None) -> bool:  # what with the position??
        if self.vertex_dict.keys().__contains__(node_id):
            return False
            """if the id is not here yet"""
        else:
            new_vertex = Vertex(node_id)  # needs also pos
            self.vertex_dict[node_id] = new_vertex
            self.in_ni[node_id] = {}
            self.out_ni[node_id] = {}
            self.vertex_size = self.vertex_size + 1
            self.changes = self.changes + 1
            return True

    def add_edge(self, id1: int, id2: int, weight: float):
        if (self.vertex_dict.__contains__(id1)) & (self.vertex_dict.__contains__(id2)):
            self.out_ni[id1].update({id2: weight})
            self.in_ni[id2].update({id1: weight})
            # self.in_ni[id1].add_neighbour(self.in_ni[id2].id, weight)
            self.changes = self.changes + 1
            self.edge_size = self.edge_size + 1
            return True
        return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        if self.in_ni.__contains__(id1):
            return self.in_ni[id1]
        else:
            return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if self.out_ni.__contains__(id1):
            return self.out_ni[id1]
        else:
            return None

    def remove_node(self, node_id: int) -> bool:
        if node_id not in self.vertex_dict:
            return False
        # remove the node
        del self.vertex_dict[node_id]
        del self.in_ni[node_id]
        del self.out_ni[node_id]
        ## to delete node_id from all the other nodes

        self.vertex_size = self.vertex_size - 1
        self.changes = self.changes + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (self.vertex_dict.__contains__(node_id1)) & (self.vertex_dict.__contains__(node_id2)):
            if (node_id1 in self.in_ni[node_id2]): # & (self.out_ni[node_id1].__contains__(node_id2)):
                del self.in_ni[node_id2][node_id1]
                del self.out_ni[node_id1][node_id2]
                self.changes = self.changes + 1
                self.edge_size = self.edge_size-1
                return True
        return False

    def get_all_v(self) -> dict:
        return self.vertex_dict

    def v_size(self) -> int:
        return self.vertex_size #was .__sizeof__()

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.changes
