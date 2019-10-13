import os
'''
'''
class DataReader:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def readRWFile(self) -> list:
        if not os.path.exists(self.file_path):
            print("no random walk file exists, please check file path...")

        rwfile = open(self.file_path, 'r')
        rwList = []
        for line in rwfile:
            linetrip = line.strip().split(" ")
            rwList.append(list(map(eval, linetrip)))
        
        rwfile.close()
        return rwList

    def readGraphFile(self):
        if not os.path.exists(self.file_path):
            print("no random graph file exists, please check file path...")
        if self.file_path.endswith('.formu'):
            return self.readFormulatedGraph()
        else:
            portion = os.path.splitext(self.file_path)
            formu_file = portion[0] + '.formu'
            if os.path.exists(formu_file):
                return self.readFormulatedGraph(form_file=formu_file)
            else:
                return self.formulateGraphFile()

    def readFormulatedGraph(self, form_file=None) -> list:
        if form_file == None:
            form_file = self.file_path
            
        if not os.path.exists(form_file):
            print("no formulated graph file exists, please check file path...")
        
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
    def formulateGraphFile(self) -> list:
        if not os.path.exists(self.file_path):
            print("no graph file exists, please check file path...")
        
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