from Singleton import Singleton
from Op import Op

class Fac:
    
    def __init__(self):
        self.Op = None
        self.Fac = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        self.Op = Op()
        self.Op.parse()
        if pointer.getToken() == 24:
            self.altNo = 2
            pointer.skipToken()
            self.Fac = Fac()
            self.Fac.parse()
        else:
            self.altNo = 1

        
    def evaluate(self):
        if self.altNo == 1:
            return self.Op.evaluate()
        else:
            return self.Op.evaluate() * self.Fac.evaluate()

    def pprint(self):
        self.Op.pprint()
        if self.altNo == 2:
            print("*", end = "")
            self.Fac.pprint()
            