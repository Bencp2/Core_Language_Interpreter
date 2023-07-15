from Singleton import Singleton
from Stmt import Stmt

class SS:
    
    def __init__(self):
        self.SS = None
        self.Stmt = None
        self.altNo = None
    
    def parse(self):
        pointer = Singleton()
        self.Stmt = Stmt()
        self.Stmt.parse()
        if pointer.getToken() in [5, 8, 10, 11, 32]:
            self.altNo = 2
            self.SS = SS()
            self.SS.parse()
        else:
            self.altNo = 1  
            
    def execute(self):
        self.Stmt.execute()
        if self.altNo == 2:
            self.SS.execute()

    def pprint(self):
        self.Stmt.pprint()
        if self.altNo == 2:
            self.SS.pprint()            