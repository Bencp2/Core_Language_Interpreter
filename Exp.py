from Singleton import Singleton
from Fac import Fac

class Exp:
    
    def __init__(self):
        self.Fac = None
        self.Exp = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        self.Fac = Fac()
        self.Fac.parse()
        if pointer.getToken() == 22:
            self.altNo = 2
            pointer.skipToken()  
            self.Exp = Exp()
            self.Exp.parse()
        elif pointer.getToken() == 23:
            self.altNo = 3
            pointer.skipToken()
            self.Exp = Exp()
            self.Exp.parse()
        else:
            self.altNo = 1
            
    def evaluate(self):
        match self.altNo:
            case 1:
                return self.Fac.evaluate()
            case 2:
                return self.Fac.evaluate() + self.Exp.evaluate()
            case 3:
                return self.Fac.evaluate() - self.Exp.evaluate()

    def pprint(self):
        self.Fac.pprint()
        if self.altNo == 2:
            print("+", end = "")
            self.Exp.pprint()
        elif self.altNo == 3:
            print("-", end = "")
            self.Exp.pprint()