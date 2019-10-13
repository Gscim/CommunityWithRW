'''
Generate random walks from a given graph file 
walk input file of type {{node1:adjnode1, adjnode2,...},...}
'''

from ramdom import choice
import math

class RandomWalks:
    def __init__(self, walk_length, walk_input, walk_output):
        self.walk_length = walk_length
        self.walk_input = walk_input
        self.walk_output = walk_output

    def walk_forward(self, start_point:int) -> list:
        current_node = start_point
        walkOneRun = []
        for step in range(self.walk_length):
            next_step = choice(walk_input[current_node])
            walkOneRun.add(next_step)
        return walkOneRun
    
    

