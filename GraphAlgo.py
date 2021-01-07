import json
import math

from collections import defaultdict
import numpy as np
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.geoLocation import geoLocation
import random
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    My_graph = DiGraph()
    weights = {}

    def __init__(self, My_graph=DiGraph(), vertices=My_graph.get_all_v()):
        self.V = vertices  # No. of vertices
        # self.My_graph=DiGraph
        # self.My_graph = defaultdict(list)  # default dictionary to store graph
        self.graphs = {}
        self.My_graph = My_graph
        self.edges = defaultdict(list)
        # self.graph = self.My_graph  # default dictionary to store graph
        self.graph = self.My_graph  # default dictionary to store graph
        self.weights = {}
        # self.vertices = vertices
        self.print_list = []

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
            if (n.__contains__("pos")):
                p = n.get("pos").split(',')
                pos = geoLocation(p.get(0), p.get(1), g.get(2))
                graph_load.add_node(n.get("id"), pos)
            else:
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

    # A function used by dfs
    def dfs(self, v, visited):
        # Mark the current node as visited and print it

        visited[v] = True
        self.print_list.append(visited[v])
        # print
        # v,
        # print(self.graph.all_out_edges_of_node(v))
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph.all_out_edges_of_node(v):
            if not visited[i]:
                self.dfs(i, visited)

    def fillOrder(self, v, visited, stack):
        # Mark the current node as visited
        visited[v] = True
        # Recur for all the vertices adjacent to this vertex
        for i in self.graph.all_out_edges_of_node(v):
            if not visited[i]:
                self.fillOrder(i, visited, stack)
        stack = stack.append(v)

    # Function that returns reverse (or transpose) of this graph
    def get_reverse(self):
        g = GraphAlgo(DiGraph(), self.V)
        # Recur for all the vertices adjacent to this vertex
        for i in g.V:
            for j in g.graph.all_out_edges_of_node(i):
                g.graph.add_edge(j, i, None)
        return g

    # The main function that finds and prints all strongly connected components
    # The main function + that finds and prints all strongly connected components
    def connected_components(self):
        stack = []
        # mark all the vertices as not visited (For first DFS)
        visited = []
        for i in self.V:
            visited.append(i)
            visited[i] = False
        # fill vertices in stack according to their finishing times
        for i in self.V:
            if not visited[i]:
                self.fillOrder(i, visited, stack)

        # create a reversed graph
        gr = self.get_reverse()

        # mark all the vertices as not visited (For second DFS)
        visited = []
        for i in self.V:
            visited.append(i)
            visited[i] = False
        # now process all vertices in order defined by Stack
        while stack:
            i = stack.pop()
            if not visited[i]:
                gr.dfs(i, visited)
                print
                self.print_list
        # self.print_list

    # def connected_component(self, id1: int) -> list:  # does it works?
    #     return id1.connected_components(self)

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


if __name__ == '__main__':
    g = GraphAlgo(5)
    g.add_edge(1, 0)
    g.add_edge(0, 2)
    g.add_edge(2, 1)
    g.add_edge(0, 3)
    g.add_edge(3, 4)

    print("Following are strongly connected components " +
          "in given graph")
    g.connected_components()
