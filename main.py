import numpy as np 
import os 

from RandomWalks import RandomWalks
from CommunityCluster import CommunityCluster
from Graph import Graph
from DataReader import DataReader

GRAPH_FILE_PATH = './randgraph.npy'
RANDOM_WALK_FILE = './rwfile.rw'

comm_nodes_list = np.array([], dtype=np.int)
comm_edges_list = np.array([], dtype=np.int)
modularity_Q = 0.1

if os.path.exists(GRAPH_FILE_PATH):
    graph_file = Graph(GRAPH_FILE_PATH)
else:
    graph_file = Graph()
    comm_nodes_list = np.array([], dtype=np.int)
    comm_edges_list = np.array([], dtype=np.int)
    graph_file.make_graph_with_community(comm_nodes_list, comm_edges_list, modularity_Q)

cluster_class = CommunityCluster(graph_file, std_Q=modularity_Q)




