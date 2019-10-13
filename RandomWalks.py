'''
Generate random walks from a given graph file 
walk input file of type {{node1:adjnode1, adjnode2,...},...}
'''

from ramdom import choice
import math

class RandomWalks:
    def __init__(self, walk_input, walk_output, walk_length:int, num_walks:int):
        self.walk_length = walk_length
        self.walk_input = walk_input
        self.walk_output = walk_output
        self.num_walks = num_walks

    def walk_forward(self, start_point:int) -> list:
        current_node = start_point
        walkOneRun = []
        for step in range(self.walk_length):
            next_step = choice(walk_input[current_node])
            walkOneRun.append(next_step)
        return walkOneRun
    
    def generate_rw(self, start_list : list):
        open(walk_output, mode='wb') as wkout:
            for start_point in start_list:
                for nwk in range(self.num_walks):
                    wkout.write(walk_forward(start_point))
        
        wkout.close()
    


