from collections import defaultdict

from src.GraphInterface import GraphInterface
from src.geoLocation import geoLocation


class Vertex:
    def __init__(self, node, position=geoLocation()):
        self.id = node
        self.adjacent = {}
        self.position = position

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_position(self, other):
        self.position = other

    def get_position(self):
        return self.position


# from GraphInterface import GraphInterface
# from DiGraph import Vertex


class DiGraph(GraphInterface):
    vertex_dict = {}  # list of nodes
    out_ni = {}
    in_ni = {}
    changes = 0
    ###Gilad- please think of another way!!!
    x_min = 2147483648.0
    y_min = 2147483648.0
    x_max = -2147483648.0
    y_max = -2147483648.0

    def __init__(self, edge_size=0, vertex_size=0, changes=0, out_ni={}, in_ni={}, vertex_dict={}, x_min=2147483648.0,
                 y_min=2147483648.0,
                 x_max=-2147483648.0, y_max=-2147483648.0):
        self.vertex_dict = vertex_dict
        self.out_ni = out_ni
        self.in_ni = in_ni
        self.vertex_size = vertex_size
        self.edge_size = edge_size
        self.changes = changes
        self.y_min = y_min
        self.y_max = y_max
        self.x_max = x_max
        self.x_min = x_min

    def add_node(self, node_id: int, pos: tuple = None) -> bool:
        if node_id in self.vertex_dict.keys():
            return False
            """if the id is not here yet"""
        else:
            new_vertex = Vertex(node_id, pos)
            self.vertex_dict[node_id] = new_vertex
            self.in_ni[node_id] = {}
            self.out_ni[node_id] = {}
            if pos is not None:
                f_x = pos.x
                f_y = pos.y

                ##to change
                if (f_y > self.y_max):
                    self.y_max = f_y
                    if (f_y < self.y_min):
                        self.y_min = f_y
                    if (f_x > self.x_max):
                        self.x_max = f_x
                    if (f_x < self.x_min):
                        self.x_min = f_x
            self.vertex_size = self.vertex_size + 1
            self.changes = self.changes + 1
            return True

    # if the edge already exists or one of the nodes dose not exists the functions will do nothing
    def add_edge(self, id1: int, id2: int, weight: float):
        if (id1 in self.vertex_dict) &  (id2 in self.vertex_dict) & (id1!=id2) : #was contain
            if id2 in self.out_ni[id1]: #was contain
                return False
            self.out_ni[id1].update({id2: weight})
            self.in_ni[id2].update({id1: weight})
            self.changes = self.changes + 1
            self.edge_size = self.edge_size + 1
            return True
        return False

    def all_in_edges_of_node(self, id1: int) -> dict:
        if id1 in self.in_ni : #was contain
            return self.in_ni[id1]
        else:
            return None

    def all_out_edges_of_node(self, id1: int) -> dict:
        if id1 in self.out_ni:
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
        ## to delete node_id from all the other nodes!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

        self.vertex_size = self.vertex_size - 1
        self.changes = self.changes + 1
        return True

    def remove_edge(self, node_id1: int, node_id2: int) -> bool:
        if (node_id1 in self.vertex_dict) & (node_id2 in self.vertex_dict):
            if (node_id1 in self.in_ni[node_id2]):  # & (self.out_ni[node_id1].__contains__(node_id2)):
                del self.in_ni[node_id2][node_id1]
                del self.out_ni[node_id1][node_id2]
                self.changes = self.changes + 1
                self.edge_size = self.edge_size - 1
                return True
        return False

    def get_all_v(self) -> dict:
        return self.vertex_dict

    def v_size(self) -> int:
        return self.vertex_size

    def e_size(self) -> int:
        return self.edge_size

    def get_mc(self) -> int:
        return self.changes
