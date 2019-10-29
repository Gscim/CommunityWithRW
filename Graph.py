import os
import numpy as np 
import random
from DataReader import DataReader

class Graph(object):
    def __init__(self, graph_file_path):
        self.graph_file_path = graph_file_path

        dr = DataReader(graph_file_path)
        self.graph = dr.readGraphFile()
        self.num_nodes = len(self.graph)

    def __init__(self):
        self.graph_file_path = None
        self.graph = None
        self.num_nodes = None


    '''
    To make random graph with communities
    randomly organize clusters and link them with limited edges
    '''
    def make_graph_with_community(self, comm_nodes_list: list, comm_edges_list: list) -> bool:
        startid = 0
        comm_size = 0
        endid = 0
        graph_file = []
        for (nodes, edges) in zip(comm_nodes_list, comm_edges_list):
            endid += nodes
            graph_file.extend(self.make_community(startid, endid, edges=edges))
        
        return self.rand_link_community(graph_file, comm_nodes_list)

    def rand_link_community(self, graph_file, comm_nodes_list):
        num_comm = len(comm_nodes_list)
        # randomly choose 2 communities
        node1, node2 = random.sample(range(num_comm), 2)
        # randomly choose nodes from selected 2 communities

        
            
    def add_edge(self, graph_file, node1, node2):
        if node1 not in graph_file[node2]:
            graph_file[node1].append(node2)
            graph_file[node2].append(node1)
        

    def make_community(self, startid, endid, edges=None):
        if edges == None:
            # num of nodes should >= 5
            edges = 2 * (endid - startid)
        comm_size = endid - startid
        community = [[] for x in range(comm_size)]
        node_set = list(range(startid, endid))

        edge_cnt = 0

        while edge_cnt < edges:
            random.sample(node_set, 2)




        return community



if __name__ == "__main__":
    graph = Graph("./testgraph.formu")
    print(graph.num_nodes)
    print(graph.graph)

