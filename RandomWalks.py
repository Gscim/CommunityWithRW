'''
Generate random walks from a given graph file 
walk input file of type [[adj1, adj2, ...],...,[adj1, adj2, ...]]
'''

from random import choice
import math
import os
import numpy as np 
from DataReader import DataReader
from Graph import Graph

class RandomWalks(object):
    def __init__(self, graph_on, walk_output, walk_length, num_walks, walk_mode=None):
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
        

    def walk_forward(self, start_point, walk_length=None):
        if walk_length == None:
            walk_length = self.walk_length

        if self.walk_mode == 0:
            return self.walk_forward_0(start_point, walk_length)
        else:
            return self.walk_forward_1(start_point, walk_length)

    # ordinary random walk forward
    def walk_forward_0(self, start_point, walk_length=None):
        if walk_length == None:
            walk_length = self.walk_length

        current_node = start_point
        # walkOneRun = [start_point]
        walkOneRun = np.zeros(walk_length + 1, dtype=np.int)
        walkOneRun[0] = start_point

        for step in range(1, 1 + walk_length):
            # print(current_node)
            # print(self.walk_input[current_node])
            next_step = choice(self.walk_input[current_node])
            walkOneRun[step] = next_step
            current_node = next_step
        return walkOneRun
    
    # second order random walk forward
    def walk_forward_1(self, start_point, walk_length=None):
        if walk_length == None:
            walk_length = self.walk_length

        prev_node = start_point
        current_node = choice(self.walk_input[prev_node])
        # walkOneRun = [prev_node, current_node]
        walkOneRun = np.zeros(walk_length + 1, dtype=np.int)
        walkOneRun[0] = prev_node
        walkOneRun[1] = current_node

        for step in range(2, 1 + walk_length):
            next_step = self.secOrderNodeDecision(prev_node, current_node)
            walkOneRun[step] = next_step
            prev_node = current_node
            current_node = next_step

        return walkOneRun

    def secOrderNodeDecision(self, prev_node, current_node):
        
        

        return 0;

    '''
    Parameters:
        start_list: list of start nodes
        binary: save rw file in binary format with numpy
    Returns:
        write to file, no return value

    Raises:
        IOError
    '''
    def generate_rw(self, start_list, binary=False):
        if binary == True:
            pass
        else:
            try:
                wkout = open(self.walk_output, mode='w')
                for start_point in start_list:
                    for nwk in range(self.num_walks):
                        walk_str = map(lambda x:str(x), self.walk_forward(start_point))
                        wkout.write(' '.join(walk_str) + '\n')
            except IOError:
                print("fail to open output file..")
            else:
                print("write random walk file succeeded.")
                wkout.close()

    '''
    Parameters:
        start_node : start node of random walks
        walk_t : length of walks, for Pt calculation
        num_starts : number of walks with start node start_node 
    
    Returns:
        array of numbers of walks that ended with node i

    Raises:

    '''
    def count_Ni(self, start_node, walk_t, num_starts):
        # Ni = [0 for i in range(self.graph_on.num_nodes)]
        Ni = np.zeros(self.graph_on.num_nodes， dtype=np.int)
        for t in range(num_starts):
            Ni[self.walk_forward(start_node, walk_length=walk_t)[-1]] += 1

        return Ni

    def calc_Pi(self, start_node, walk_t, num_starts):
        # Pi = [0.0 for i in range(self.graph_on.num_nodes)]
        Pi = np.zeros(self.graph_on.num_nodes, dtype=np.float)
        Ni = self.count_Ni(start_node, walk_t, num_starts)
        for i, Nik in enumerate(Ni):
            Pi[i] = float(Nik) / float(num_starts)

        return Pi


if __name__ == "__main__":
    a = np.array([[1, 2, 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]])
    gfile = open("./testgraph.bin", 'w')

    for node in a:
        gfile.write(' '.join(map(lambda x: str(x), node)) + '\n')

    gfile.close()
    rw = RandomWalks(a, "trialout.rw", 3, 1)
    rw.generate_rw([0, 1, 2, 3, 4, 5])




