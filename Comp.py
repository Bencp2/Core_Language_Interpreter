from Singleton import Singleton
from Op import Op
from CompOp import CompOp

class Comp:
    
    def __init__(self):
        self.OpOne = None
        self.OpTwo = None
        self.CompOp = None
        
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 20:
            print("Invalid Token:", pointer.getToken())
            print("Should be ( but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.OpOne = Op()
        self.OpOne.parse()
        self.CompOp = CompOp()
        self.CompOp.parse()
        self.OpTwo = Op()
        self.OpTwo.parse()
        if pointer.getToken() != 21:
            print("Invalid Token:", pointer.getToken())
            print("Should be ) but was", pointer.tokenString())
            quit()        
        pointer.skipToken()
        
        
    def evaluate(self):
        match self.CompOp.getCompOp():
            case 1:
                return self.OpOne.evaluate() != self.OpTwo.evaluate()
            case 2:
                return self.OpOne.evaluate() == self.OpTwo.evaluate()
            case 3:
                return self.OpOne.evaluate() < self.OpTwo.evaluate()
            case 4:
                return self.OpOne.evaluate() > self.OpTwo.evaluate()
            case 5:
                return self.OpOne.evaluate() <= self.OpTwo.evaluate()
            case default:
                return self.OpOne.evaluate() >= self.OpTwo.evaluate()


    def pprint(self):
        print("(", end = "")
        self.OpOne.pprint()
        self.CompOp.pprint()
        self.OpTwo.pprint()
        print(")", end = "")