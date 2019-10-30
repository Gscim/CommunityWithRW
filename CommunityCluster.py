from RandomWalks import RandomWalks
from DataReader import DataReader
from Graph import Graph
import os

class CommunityCluster(object):
    def __init__(self, graph_file):
        self.community_num = None
        self.community_cluster = None
        self.intern_edges = None
        self.bound_edges = None
        self.modularity_Q = None
        self.graph_file = graph_file
    
    def __init__(self, community_num, community_cluster, 
            intern_edges, bound_edges, modularity_Q):
        self.community_num = community_num
        self.community_cluster = community_cluster
        self.intern_edges = intern_edges
        self.bound_edges = bound_edges
        self.modularity_Q = modularity_Q
        self.graph_file = None
    
    # return value of nodularity Q
    def compute_Q(self, my_community_clusters):
        if self.graph_file == None:
            print("cannot compute Q of graph, no graph file provided...")
            exit(1);

        Q = 0.0
        for community in my_community_clusters:
            edge_info = self.compute_edges(community)
            Q = Q + (edge_info[0] - edge_info[1] ** 2)

        self.modularity_Q = Q
        return Q

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



    # edges include internal edges and bounding edges
    # return (internal edges, bounding edges)
    def compute_edges(self, single_community):
        cnt_intern = 0
        cnt_bound = 0
        for node in single_community:
            for edgeto in graph_file[node]:
                if edgeto in single_community:
                    cnt_intern += 1
                else:
                    cnt_bound += 1

        return (cnt_intern / 2, cnt_bound)


if __name__ == "__main__":
    a = [[1, 2 , 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]]
    gf = Graph()
    gf.graph = a
    rw = RandomWalks(gf, "trialout.rw", 3, 1)
    rw.generate_rw([0, 1, 2, 3, 4, 5])

    ccluster = CommunityCluster(3, [1], [1], [1], [2])
    ccluster.genGraphWithCommunities(3, [3, 4 ,5], [2, 3 ,4])

