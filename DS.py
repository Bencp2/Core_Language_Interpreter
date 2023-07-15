from Singleton import Singleton
from Decl import Decl

class DS:
    
    def __init__(self):
        self.Decl = None
        self.DS = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        self.Decl = Decl()
        self.Decl.parse()
        if pointer.getToken() == 4:
            self.altNo = 2
            self.DS = DS()
            self.DS.parse()
        else:
            self.altNo = 1    
        
    def execute(self):
        self.Decl.execute()
        if self.altNo == 2:
            self.DS.execute()
            

    def pprint(self):
        self.Decl.pprint()
        if self.altNo == 2:
            self.DS.pprint()
            