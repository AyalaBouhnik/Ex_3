# Ex_3
# Directed Weighted Graph-
# About the project
In this assignment (-'3') we will implement directed weighted graph in python program, by using the data structure we have developed so far, in Java program. Including the ability to save and restore the graph from a file in Json format, calculate the shortest directed route, find the strongly connected component and more. 
In the third part of this assignment we compared the run time of some function in our graph VS NetworkX package VS Java.
(you can read more about the compactions in the wiki page).

An example of directed weighted graph:
 <img src=https://reasonabledeviations.com/assets/images/weighted_digraph.png> 


in the src package we have two main classes- DiGraph and GraphAlgo.
DiGraph class- This class represents a directional weighted graph based on a dict.

**The main methods we have in the DiGraph class are:**

* def add_node(self, node id, pos)- this method adds a node to the graph. It will return true if the node was added successfully, otherwise- false. If the edge already exists or one of the nodes dose not exists the functions will do nothing.

* def remove_node(self, node_id: int) – this method removes a node from the graph. . It will return true if the node was removed successfully, otherwise- false.

* def remove_edge(self, node_id1: int, node_id2: int) – this method removes an edge from the graph. It will return true if the edge was removed successfully, otherwise- false.

* def get_all_v(self) -this method return a dictionary of all the nodes in the graph, each node is represented using a pair  (key, node_data).

* def all_in_edges_of_node(self, id1: int) – this method return a dictionary of all the nodes connected to (into) node_id , each node is represented using a pair (key, weight).

* def all_out_edges_of_node(self, id1: int) – this method return a dictionary of all the nodes connected from node_id , each node is represented using a pair (key, weight).

* def v_size(self) – this method returns the number of vertices in this graph.

* def e_size(self) – this method returns the number of edges in this graph.

* def get_mc(self) -this method returns the current version of this graph,  on every change in the graph state - the 'changes' variable should be increased.

An example of plot graph:

<img src=https://user-images.githubusercontent.com/74878247/104622101-81a52180-5699-11eb-8024-580a3221d24f.PNG> 


**GraphAlgo class- This class have the main algorithms:**

* def get_graph(self)- this method return the directed graph on which the algorithm works on.

* def load_from_json(self, file_name: str)- this method loads a graph from a json file. It will return true if the loading was successful, otherwise- false. 

 * def save_to_json(self, file_name: str)-this method saves the graph in JSON format to a file. It will return true if the save was successful, otherwise false.
 
* def shortest_path(self, id1: int, id2: int)- this method returns the shortest path from node id1 to node id2 using Dijkstra's Algorithm. It will return the distance of the path, a list of the nodes ids that the path goes through. If there is no path between id1 and id2, or one of them does not exist the function returns (float('inf'),[])

* def connected_component(self, id1: int)-this method finds the Strongly Connected Component(SCC) that node id1 is a part of.  If the graph is None or id1 is not in the graph, the function should return an empty list [].

* def connected_components(self)-this method  finds all the Strongly Connected Component(SCC) in the graph. It will return the list all SCC.  If the graph is None the function should return an empty list [].

* def plot_graph(self) -this method plots the graph.
If the nodes have a position, the nodes will be placed there.
Otherwise, they will be placed in a random but elegant manner.

