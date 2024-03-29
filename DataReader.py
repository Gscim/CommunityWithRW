import os
import numpy as np 
'''
'''
class DataReader(object):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def readRWFile(self):
        if not os.path.exists(self.file_path):
            print("no random walk file exists, please check file path...")
            exit(1)
        try:
            rwfile = open(self.file_path, 'r')
            rwList = []
            for line in rwfile:
                linetrip = line.strip().split(" ")
                rwList.append(list(map(eval, linetrip)))
        except IOError:
            print('fail to open rw file.')
        else:
            print('rw file read.')
            rwfile.close()
        return rwList

    def readGraphFile(self):
        if not os.path.exists(self.file_path):
            print("no random graph file exists, please check file path...")
            exit(1)
        if self.file_path.endswith('.formu'):
            return self.readFormulatedGraph()
        else:
            portion = os.path.splitext(self.file_path)
            formu_file = portion[0] + '.formu'
            if os.path.exists(formu_file):
                return self.readFormulatedGraph(form_file=formu_file)
            else:
                return self.formulateGraphFile()

    def readFormulatedGraph(self, form_file=None):
        if form_file == None:
            form_file = self.file_path
            
        if not os.path.exists(form_file):
            print("no formulated graph file exists, please check file path...")
            exit(1)
        
        graphList = []
        gfile = open(form_file, 'r')
        for line in gfile:
            linetrip = line.strip().split(" ")
            graphList.append(list(map(eval, linetrip)))

        gfile.close()
        return graphList
    
    '''
    to make formulated graph files
    origin graph file may not good for computing
    to be continued...
    '''
    def formulateGraphFile(self):
        if not os.path.exists(self.file_path):
            print("no graph file exists, please check file path...")
            exit(1)
        
        portion = os.path.splitext(self.file_path)
        formu_path = portion[0] + '.formu'
        graph_file = open(self.file_path, 'r')
        formu_file = open(formu_path, 'w')
        reList = []











        graph_file.close()
        formu_file.close()
        return reList


   
if __name__ == "__main__":
    dr = DataReader("trialout.rw")
    print(dr.readRWFile())