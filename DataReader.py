import sys


#This is used to read the data file
class DataReader:    
    dataFile = open(sys.argv[2], "r")
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance =  super().__new__(cls)
        return cls.instance
    
    #reads next line and returns the number from that line
    def nextNum(self):
        line = self.dataFile.readline()
        if line == "":
            print("Error: next line is empty in", sys.argv[2])
            quit()
        return line.strip()
        