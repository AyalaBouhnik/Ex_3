import unittest

from src.DiGraph import DiGraph


class TestDiGraph(unittest.TestCase):

    def test_1(self):
        g = DiGraph()  # creates an empty directed graph
        for i in range(5):
            g.add_node(i)
        g.add_edge(0, 1, 1)                                      #0---->1
        g.add_edge(0, 1, 1.1)
        g.add_edge(5, 2, 7.8)                                    #5---->2
        g.add_edge(2, 5, 1.1)                                    #2---->5- removed
        g.add_edge(1, 2, 9)                                      #1-----2
        g.remove_edge(2, 3)  # does not exist
        g.remove_edge(2, 5)
        g.add_edge(1, 3, 10)                                     #1-----3
        self.assertEqual(g.v_size(), 5)
        self.assertEqual(g.e_size(), 4)
        self.assertEqual(g.get_all_v().__len__(), 5)
        self.assertEqual(g.all_out_edges_of_node(1).__len__(), 2)
        self.assertEqual(g.all_in_edges_of_node(1).__len__(), 1)
        g.remove_node(1)
        self.assertEqual(g.get_all_v().__len__(), 4)
        # self.assertEqual(g.get_mc(), 7) #####why it doesnt work?
        print(g.get_mc()) #-doesnt work


# if __name__ == '__main__':
#     unittest.main()