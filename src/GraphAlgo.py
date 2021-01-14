import json
import math

from collections import defaultdict
from src import GraphInterface
from src.DiGraph import DiGraph
from src.GraphAlgoInterface import GraphAlgoInterface
from src.geoLocation import geoLocation
import random
import matplotlib.pyplot as plt


class GraphAlgo(GraphAlgoInterface):
    My_graph = DiGraph()
    weights = {}


    def __init__(self, My_graph=DiGraph()):
        self.V = {} # No. of vertices
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


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    # I need to change it. I returned a DiGraph- needs to be GraphInterface.
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
            # if n.__contains__("pos"):
            if "pos" in n: #was contain
                p = n.get("pos").split(',')
                f_x = float(p[0])
                f_y = float(p[1])

                # if self.y_max is None | f_y > self.y_max:
                #     self.y_max = f_y
                # if self.y_min is None | f_y < self.y_min:
                #     self.y_min = f_y
                # if self.x_max is None | f_x > self.x_max:
                #     self.x_max = f_x
                # if self.x_min is None | f_x < self.x_min:
                #     self.x_min = f_x

                pos = geoLocation(f_x, f_y, float(p[2]))
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

    def connected_component(self, id1: int) -> list:
        answer = []
        if (self.My_graph is None) | (id1 not in self.My_graph.vertex_dict):
            return answer  # returns an empty list.

        for node in self.My_graph.vertex_dict.values():
            if (self.shortest_path(id1, node.id)[1].__len__() > 0) & (self.shortest_path(node.id, id1)[1].__len__() > 0):
                answer.append(node)
        return answer


    def connected_components(self):
        result = []
        if self.My_graph is None: return result
        added = {}

        for nodeKey in self.My_graph.get_all_v().keys():
            if not added.__contains__(nodeKey):
                tempList = self.connected_component(nodeKey)
                for nodeList in tempList:
                    added.update({nodeList.id: nodeList})
                result.append(tempList)  # adds a list to the answer list
        return result

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

            # the next node is the destination with the lowest weight
            current_node = min(next_dest, key=lambda k: next_dest[k][1])

        # work back through dest in shortest path
        path = []
        while current_node is not None:
            path.append(current_node)
            next_node = all_shortest_paths[current_node][0]
            current_node = next_node
        # reverse path
        path = path[::-1]
        return all_shortest_paths[id2][1], path

    def plot_graph(self) -> None:
        if self.My_graph.get_all_v().get(0).get_position() is None:
            f = plt.figure() #figsize=(100.0, 100.0
            axis = plt.axes(xlim=(0, 9.7), ylim=(0, 9.7))
            ax = f.gca()
            x_positions = []
            y_positions = []
            arr_keys = []
            for i in self.My_graph.get_all_v():
                if i not in arr_keys:
                    x_random = random.uniform(0.3, 9.7)
                    y_random = random.uniform(0.3, 9.7)
                    self.My_graph.get_all_v()[i].set_position(geoLocation(x_random, y_random))
                    arr_keys.append(i)
                    arr_position = []

                    while self.My_graph.get_all_v()[i].get_position() in arr_position:
                        y_random = random.uniform(0.3, 999998.7)
                    self.My_graph.get_all_v()[i].set_position(geoLocation(x_random, y_random))
                    arr_position.append(self.My_graph.get_all_v()[i].get_position())
                    x_positions.append(x_random)
                    y_positions.append(y_random)
                    ax.scatter(x_positions, y_positions, c='blue', s=50)
                    plt.annotate(i, (x_random, y_random))

                for j in self.My_graph.all_out_edges_of_node(i):
                    if j not in arr_keys:
                        x_random = random.uniform(0.3, 9.7)
                        y_random = random.uniform(0.3, 9.7)
                        self.My_graph.get_all_v()[j].set_position(geoLocation(x_random, y_random))
                        arr_keys.append(j)
                        arr_position = []

                        while self.My_graph.get_all_v()[j].get_position in arr_position:
                            y_random = random.uniform(0.3, 9.7)
                        self.My_graph.get_all_v()[j].set_position(geoLocation(x_random, y_random))
                        arr_position.append(self.My_graph.get_all_v()[j].get_position())
                        x_positions.append(x_random)
                        y_positions.append(y_random)
                        ax.scatter(x_positions, y_positions, c='blue', s=30)
                        plt.annotate(j, (x_random, y_random))
                    plt.annotate(text='', xy=(self.My_graph.get_all_v()[i].get_position().x,self.My_graph.get_all_v()[i].get_position().y),
                                     xytext=(self.My_graph.get_all_v()[j].get_position().x,
                                             self.My_graph.get_all_v()[j].get_position().y),
                                     arrowprops=dict(arrowstyle='<-'))
                    # ax.arrow(self.My_graph.get_all_v()[i].get_position().x,self.My_graph.get_all_v()[i].get_position().y,
                    #              self.My_graph.get_all_v()[j].get_position().x-self.My_graph.get_all_v()[i].get_position().x,
                    #              self.My_graph.get_all_v()[j].get_position().y-self.My_graph.get_all_v()[i].get_position().y,
                    #              head_width =0.3, head_length=0.3, fc='k', ec='k')++
        else:
            x_positions = []
            y_positions = []
            f = plt.figure()
            ax = f.gca()
            if (self.My_graph.y_max is None) | (self.My_graph.x_max is None) | (self.My_graph.x_min is None) | (self.My_graph.y_min is None):
                plt.axes(xlim = (-2 ,2) , ylim = (-2, 2))
            else:
                ax.axis([(self.My_graph.x_min - 0.005), (self.My_graph.x_max + 0.002),(self.My_graph.y_min - 0.008), (self.My_graph.y_max + 0.001)])
                arr_keys = []
                for i in self.My_graph.get_all_v():
                    if i not in arr_keys:
                        x_positions.append(self.My_graph.get_all_v()[i].get_position().x)
                        y_positions.append(self.My_graph.get_all_v()[i].get_position().y)
                        ax.scatter(self.My_graph.get_all_v()[i].get_position().x,
                                   self.My_graph.get_all_v()[i].get_position().y, c='blue', s=50)
                        plt.annotate(i, (
                            self.My_graph.get_all_v()[i].get_position().x, self.My_graph.get_all_v()[i].get_position().y))
                        arr_keys.append(i)
                    for j in self.My_graph.all_out_edges_of_node(i):
                        if j not in arr_keys:
                            x_positions.append(self.My_graph.get_all_v()[j].get_position().x)
                            y_positions.append(self.My_graph.get_all_v()[j].get_position().y)
                            arr_keys.append(j)
                            ax.scatter(self.My_graph.get_all_v()[j].get_position().x,
                                       self.My_graph.get_all_v()[j].get_position().y, c='blue', s=50)
                            plt.annotate(j, (
                                self.My_graph.get_all_v()[j].get_position().x,
                                self.My_graph.get_all_v()[j].get_position().y))
                        plt.annotate(text='', xy=(self.My_graph.get_all_v()[i].get_position().x,
                                                  self.My_graph.get_all_v()[i].get_position().y),
                                     xytext=(self.My_graph.get_all_v()[j].get_position().x,
                                             self.My_graph.get_all_v()[j].get_position().y),
                                     arrowprops=dict(arrowstyle='<-'))
                        # ax.arrow(self.My_graph.get_all_v()[i].get_position().x,
                    #          self.My_graph.get_all_v()[i].get_position().y,
                    #          self.My_graph.get_all_v()[j].get_position().x - self.My_graph.get_all_v()[
                    #              i].get_position().x,
                    #          self.My_graph.get_all_v()[j].get_position().y - self.My_graph.get_all_v()[
                    #              i].get_position().y,
                    #          head_width=0.3, head_length=0.3, fc='k', ec='k')


        plt.show()



