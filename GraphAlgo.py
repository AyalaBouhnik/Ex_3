import heapq
import json
import queue
from collections import defaultdict
from inspect import stack
from math import floor

from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):
    graph = DiGraph()  # is there need?

    def __init__(self, vertices):
        self.result = self.graph.get_all_v()
        self.V = vertices  # No. of vertices
        self.graph = defaultdict(list)  # default dictionary to store graph
        self.graphs = {}

    def save_to_json(self, file_name: str) -> bool:
        all = []

        vertex = self.graph.get_all_v()
        for v in vertex:
            for e in self.graph.all_out_edges_of_node(v):
                informationE = {"src": vertex[v].id, "w": self.graph.all_out_edges_of_node(v)[e],
                                "dest": self.graph.all_out_edges_of_node(v).values()[e]}
                informationE.__add__()

                informationN = {"pos": vertex[v].pos, "id": vertex[v].id}
                informationN.__add__()

                edges = ["Edges"]
                nodes = ["Nodes"]

                all.__add__(edges, informationE)
                all.__add__(nodes, informationN)

        return True

    def load_from_json(self, file_name: str) -> bool:
        new_graph_dict = {}
        with open(file_name, "r") as f:
            g = json.load(f)
            for k, v in g():
                graph = DiGraph(**v)
                new_graph_dict[k] = graph
        self.graphs = new_graph_dict

        return True

        # add an edge to graph without the weight- for the connected_components (the weight is irrelevant.)

    def add_edge_without_weight(self, u, v):
        self.graph[u].append(v)

        # A function used by DFS

    def dfs_util(self, v, visited):
        # Mark the current node as visited and print it
        visited[v] = True
        print(v)
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
                self.dfs_util(i, visited)

    def put_by_order(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph[v]:
            if visited[i] == False:
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

        # The main function that finds and prints all strongly connected components

    def connected_components(self):

        stack = []
        # Mark all the vertices as not visited (For first DFS)

        visited = [False] * (self.V)
        # Fill vertices in stack according to their finishing times
        for i in range(self.V):
            if visited[i] == False:
                self.put_by_order(i, visited, stack)

                # Create a reversed graph
        reverse_g = self.graph_reverse()

        # Mark all the vertices as not visited (For second DFS)
        visited = [False] * (self.V)

        # process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if visited[i] == False:
                reverse_g.dfs_util(i, visited)
                print("")
                # print() #checking

    def connected_component(self, id1: int) -> list:  # does it works?
        return id1.connected_components(self)

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        heap = []
        heapq.heappush(heap,(0,id1))
        while(len(heap)!=0):
            current_cost, current_vertex = heapq.heappop(heap)
            if current_vertex == id2:
                print("The path {} cost {}".format(id1, id2, current_cost))
                break
            for neighbor, neighbor_cost in self.graph[current_vertex]:
                heapq.heappush(heap,(current_cost+neighbor_cost, neighbor))
                #I need to defind what is mean current_cost and neighbor_cost?

