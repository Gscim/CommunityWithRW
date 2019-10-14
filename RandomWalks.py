'''
Generate random walks from a given graph file 
walk input file of type {{node1:adjnode1, adjnode2,...},...}
'''

from random import choice
import math
import os
from DataReader import DataReader
from Graph import Graph

class RandomWalks(object):
    def __init__(self, graph_on: Graph, walk_output, walk_length:int, num_walks:int, walk_mode=None):
        self.walk_length = walk_length
        self.graph_on = graph_on
        self.walk_input = graph_on.graph
        self.walk_output = walk_output
        self.num_walks = num_walks

        # walk mode 0 for ordinary random walk, 1 for second order random walk
        if (walk_mode == None):
            self.walk_mode = 0
        else:
            self.walk_mode = 1

    # ordinary random walk forward
    def walk_forward_0(self, start_point:int) -> list:
        current_node = start_point
        walkOneRun = [str(start_point)]
        for step in range(self.walk_length):
            # print(current_node)
            # print(self.walk_input[current_node])
            next_step = choice(self.walk_input[current_node])
            walkOneRun.append(str(next_step))
            current_node = next_step
        return walkOneRun
    
    # second order random walk forward
    def walk_forward_1(self, start_point:int) -> list:
        prev_node = start_point
        current_node = choice(self.walk_input[prev_node])
        walkOneRun = [str(prev_node), str(current_node)]
        for step in range(1, self.walk_length):
            next_step = self.secOrderNodeDecision(prev_node, current_node)
            walkOneRun.append(str(next_step))
            prev_node = current_node
            current_node = next_step

        return walkOneRun

    def secOrderNodeDecision(self, prev_node, current_node):
        


        return 0;

    def generate_rw(self, start_list : list):
        wkout = open(self.walk_output, mode='w')
        if self.walk_mode == 0:  
            for start_point in start_list:
                for nwk in range(self.num_walks):
                    wkout.write(' '.join(self.walk_forward_0(start_point)) + '\n')
        else:
            for start_point in start_list:
                for nwk in range(self.num_walks):
                    wkout.write(' '.join(self.walk_forward_1(start_point)) + '\n')

        wkout.close()

if __name__ == "__main__":
    a = [[1, 2, 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]]
    gfile = open("./testgraph.bin", 'w')

    for node in a:
        gfile.write(' '.join(map(lambda x: str(x), node)) + '\n')

    gfile.close()
    rw = RandomWalks(a, "trialout.rw", 3, 1)
    rw.generate_rw([0, 1, 2, 3, 4, 5])




