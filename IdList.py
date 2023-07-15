from Singleton import Singleton
from Id import Id
from DataReader import DataReader

class IdList:
    
    def __init__(self):
        self.Id = None
        self.IdList = None
        self.altNo = None

    def parse(self, alt):
        pointer = Singleton()
        if alt == 1:
            self.Id = Id.parseDeclare()
        else:
            self.Id = Id.parseAssign()    
        if pointer.getToken() == 13:
            pointer.skipToken()
            self.altNo = 2
            self.IdList = IdList()
            self.IdList.parse(alt)                
        else:
            self.altNo = 1
    
    def executeDecl(self):
        self.Id.declareId()
        if self.altNo == 2:
            self.IdList.executeDecl()
        
    def executeRead(self):
        DR = DataReader()
        num = DR.nextNum()
        self.Id.setIdVal(int(num))
        if self.altNo == 2:
            self.IdList.executeRead()
            
    def executePrint(self):
        print(self.Id.getIdName(), "=", self.Id.getIdVal())
        if self.altNo == 2:
            self.IdList.executePrint()        
        
    def pprint(self):
        print(self.Id.getIdName(), end = "")
        if self.altNo == 2:
            print(",", end = " ")
            self.IdList.pprint()