from RandomWalks import RandomWalks
from DataReader import DataReader

a = [[1, 2 , 3, 4, 5], [0, 2, 3, 4, 5], [0, 1, 3, 4, 5], [0, 1, 2, 4, 5], [0, 1, 2, 3, 5], [0, 1, 2, 3, 4]]
rw = RandomWalks(a, "trialout.rw", 3, 1)
rw.generate_rw([0, 1, 2, 3, 4, 5])