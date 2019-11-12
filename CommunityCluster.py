from RandomWalks import RandomWalks
from DataReader import DataReader
from Graph import Graph
import os
import numpy as np 
'''
    Parameters:
        graph file: graph file 
        community_record: list of communities recorded with nodes
        std_Q: actual Q with real communities over graph file
'''

class CommunityCluster(object):
    def __init__(self, graph_file):
        self.graph_file = graph_file
        self.graph = graph_file.graph
        self.community_record = graph_file.community_record
        self.std_Q = graph_file.std_Q
        self.part_Q = None
        self.partition = None
        self.deltaC = None
        self.adj_C = None

    # compute modularity Q with current partition
    def compute_Q(self):
        # init partition, each partition is a single node
        if self.partition == None:
            self.partition = [[x] for x in range(self.graph_file.num_nodes)]

        Q = 0.0
        for community in self.partition:
            intern_edge, bound_edge = self.compute_edges(community)
            Q = Q + (intern_edge - bound_edge ** 2)

        self.part_Q = Q
        return Q

    '''
        community record is used
    '''

    # main algorithm for community cluster program
    def cluster_on_graph(self, rwfile):
        if not os.path.exists(rwfile):
            print("no random walk file provided, exit...")
            exit(1)

        dreader = DataReader(rwfile)
        rwList = dreader.readRWFile();

        Clusters = [[x] for x in range(self.graph_file.num_nodes)]


        self.community_cluster = Clusters
        return Clusters

    # 可以提出去单独运算Pi. 这样会减少很多运算，
    def comm_dis(self, C1, C2, matP, degree, num_nodes):
        rC1C2 = 0.0

        for node in range(num_nodes):
            PC1k = 0.0
            for nc1 in C1:
                PC1k += matP[nc1][node]
            PC1k /= len(C1)

            PC2k = 0.0
            for nc2 in C2:
                PC2k += matP[nc2][node]
            PC2k /= len(C2)

            rC1C2 += ((PC1k - PC2k) ** 2) / degree[node]
        
        rC1C2 = math.sqrt(rC1C2)
        return rC1C2

    def merge_comm(self, C1, C2):
        # merge and change deltaC
        pass
    
    def calculate_deltaC(self, partition, matP, degree, node_num, adj_C):
        deltaC = np.zeros((node_num, node_num), dtype=np.float64)
        for C1, C in enumerate(partition):
            if C == None:
                for idx in range(node_num):
                    deltaC[C1][idx] = deltaC[idx][C1] = -1
            else:
                sC1 = len(C)
                for C2 in adj_C[C1]:
                    if C2 <= C1:
                        continue
                    sC2 = len(partition[C2])
                    deltaC[C1][C2] = deltaC[C2][C1] = (sC1 * sC2) / (SC1 + SC2) + self.comm_dis(partition[C1], partition[C2], matP, degree, node_num)
        self.deltaC = deltaC
        return deltaC

    def record_adj_C(self, partition, graph):
        pass


    # edges include internal edges and bounding edges
    # return (internal edges, bounding edges)
    def compute_edges(self, single_community):
        cnt_intern = 0
        cnt_bound = 0
        for node in single_community:
            for edgeto in self.graph[node]:
                if edgeto in single_community:
                    cnt_intern += 1
                else:
                    cnt_bound += 1

        return (cnt_intern / 2, cnt_bound)

    def valueInit(self, graph, partition, matP, degree, node_num):
        adj_C = self.record_adj_C(partition, graph)
        self.calculate_deltaC(partition, matP, degree, node_num, adj_C)
        


if __name__ == "__main__":
    file_path = './graphfile'
    rwout_file = './rwout'
    graph = Graph(file_path)
    rw = RandomWalks(graph, rwout_file, 10, 100)
    commCluster = CommunityCluster()

    node_num = graph.num_nodes
    walk_t = 5
    num_walks = 100

    matP = np.zeros((node_num, node_num), dtype=np.float64)
    for node in range(node_num):
        matP[node] = rw.calc_Pi(node, walk_t, num_walks).copy()

    commCluster.valueInit(graph, commCluster.partition, matP, graph.degree, node_num)

    



    

