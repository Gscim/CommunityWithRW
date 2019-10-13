'''
Generate random walks from a given graph file 
walk input file of type {{node1:adjnode1, adjnode2,...},...}
'''

from random import choice
import math
import os
import DataReader

class RandomWalks(object):
    def __init__(self, walk_input, walk_output, walk_length:int, num_walks:int):
        self.walk_length = walk_length
        self.walk_input = walk_input
        self.walk_output = walk_output
        self.num_walks = num_walks

    def walk_forward(self, start_point:int) -> list:
        current_node = start_point
        walkOneRun = [str(start_point)]
        for step in range(self.walk_length):
            # print(current_node)
            # print(self.walk_input[current_node])
            next_step = choice(self.walk_input[current_node])
            walkOneRun.append(str(next_step))
            current_node = next_step
        return walkOneRun
    
    def generate_rw(self, start_list : list):
        wkout = open(self.walk_output, mode='w')
        for start_point in start_list:
            for nwk in range(self.num_walks):
                wkout.write(' '.join(self.walk_forward(start_point)) + '\n')
        
        wkout.close()

if __name__ == "__main__":
    a = [[1, 2 , 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]]
    rw = RandomWalks(a, "trialout.rw", 3, 1)
    rw.generate_rw([0, 1, 2, 3, 4, 5])



