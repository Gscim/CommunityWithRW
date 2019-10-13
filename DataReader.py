import os

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
            linetrip
            rwList.append(list(map(eval, linetrip)))
        
        return rwList

if __name__ == "__main__":
    dr = DataReader("trialout.bin")
    print(dr.readRWFile())