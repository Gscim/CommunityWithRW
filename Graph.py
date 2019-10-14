import os
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



if __name__ == "__main__":
    graph = Graph("./testgraph.formu")
    print(graph.num_nodes)
    print(graph.graph)

