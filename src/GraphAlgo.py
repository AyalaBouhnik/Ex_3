import json
import math

from collections import defaultdict
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface

class GraphAlgo(GraphAlgoInterface):
    My_graph = DiGraph()  # is there need?
    weights = {}

    def __init__(self, My_graph=DiGraph(), vertices=0):
        # self.result = self.graph.get_all_v()
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.graphs = {}
        self.My_graph = My_graph
        self.edges = defaultdict(list)
        self.weights = {}
        # self.vertices = vertices

    def get_graph(self) -> GraphInterface:
        if self.My_graph is None:
            return {}
        return self.My_graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as f:
            g = json.load(f)
        a = g.get("Edges")
        b = g.get("Nodes")
        graph_load = DiGraph()

        for n in b:
            graph_load.add_node(n.get("id"))
        for p in a:
            graph_load.add_edge(p.get("src"), p.get("dest"), p.get("w"))
        self.My_graph = graph_load
        return True

    def save_to_json(self, file_name: str) -> bool:
        allN = []
        allE = []
        all = {}
        vertex = self.My_graph.get_all_v()
        for v in vertex:
            for e in self.My_graph.all_out_edges_of_node(v):
                informationE = {"src": vertex[v].id, "w": self.My_graph.all_out_edges_of_node(v)[e],
                                "dest": e}
                allE.append(informationE)

                informationN = {"id": vertex[v].id}
                allN.append(informationN)

        edges = [allE]
        nodes = [allN]

        all.update({"Nodes": nodes})
        all.update({"Edges": edges})

        with open(file_name, 'w') as f:
            json.dump(all, f)

        return True

    # add an edge to graph without the weight- for the connected_components (the weight is irrelevant.)
    def add_edge_without_weight(self, u, v):
        self.graph[u].append(v)
        self.My_graph.changes = self.My_graph.changes+1
##add an edge mc

    # a function used by DFS
    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        # print(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.dfs_util(i, visited)

    def put_by_order(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if not visited[i]:
                self.put_by_order(i, visited, stack)
        stack = stack.append(v)

    # returns reverse of this graph
    def graph_reverse(self):
        g = GraphAlgo(self.V)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge_without_weight(j, i)
        return g

    # The main function that finds and prints all strongly connected components:
    def connected_components(self):
        stack = []
        # Mark all the vertices as not visited (For first DFS):
        visited = [False] * self.V
        # Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if not visited[i]:
                self.put_by_order(i, visited, stack)

        # Create a reversed graph:
        reverse_g = self.graph_reverse()

        # Mark all the vertices as not visited (For second DFS):
        visited = [False] * self.V

        # process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                reverse_g.dfs_util(i, visited)
                print("")
                # print() #checking

    # def connected_component(self, id1: int) -> list:  # does it works?
    #     return id1.connected_components(self)

    def plot_graph(self) -> None:
        pass

    def shortest_path(self, id1, id2):
        if (id1 not in self.My_graph.vertex_dict.keys()) | (id2 not in self.My_graph.vertex_dict.keys()):
            return "not in the graph"
        # shortest paths is a dict of nodes
        # whose value is a tuple of (previous node, weight)
        all_shortest_paths = {id1: (None, 0.0)}
        current_node = id1
        visited = set()
        self.weights.update({(current_node, current_node): 0.0})

        while current_node != id2:
            visited.add(current_node)
            dest = self.My_graph.all_out_edges_of_node(current_node)
            weight_to_current_node = all_shortest_paths[current_node][1]

            for next_node in dest:
                self.weights.update(
                    {(current_node, next_node): self.My_graph.all_out_edges_of_node(current_node).get(next_node)})
                weight = self.weights[(current_node, next_node)] + weight_to_current_node
                if next_node not in all_shortest_paths:
                    all_shortest_paths[next_node] = (current_node, weight)
                else:
                    current_shortest_weight = all_shortest_paths[next_node][1]
                    if current_shortest_weight > weight:
                        all_shortest_paths[next_node] = (current_node, weight)

            next_dest = {node: all_shortest_paths[node] for node in all_shortest_paths if node not in visited}
            if not next_dest:
                return math.inf, []
                # return math.inf, []
                # next node is the destination with the lowest weight

            current_node = min(next_dest, key=lambda k: next_dest[k][1])

            # Work back through dest in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = all_shortest_paths[current_node][0]
            current_node = next_node
        # Reverse path
        path = path[::-1]
        return all_shortest_paths[id2][1], path
