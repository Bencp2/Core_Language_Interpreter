from Singleton import Singleton
from Int import Int
from Id import Id
import Exp

class Op:
    
    def __init__(self):
        self.Int = None
        self.Id = None
        self.Exp = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() == 31:
            self.altNo = 1
            self.Int = Int()
            self.Int.parse()
        elif pointer.getToken() == 32:
            self.altNo = 2
            self.Id = Id.parseAssign()
        else:
            self.altNo = 3
            if pointer.getToken() != 20:
                print("Invalid Token:", pointer.getToken())
                print("Should be ( but was", pointer.tokenString())
                quit()
            pointer.skipToken()    
            self.Exp = Exp.Exp()
            self.Exp.parse()
            if pointer.getToken() != 21:
                print("Invalid Token:", pointer.getToken())
                print("Should be ) but was", pointer.tokenString())
                quit()        
            pointer.skipToken()
        
        
    def evaluate(self):
        match self.altNo:
            case 1:
                return self.Int.getIntVal()
            case 2:
                return self.Id.getIdVal()
            
            case 3:
                return self.Exp.evaluate()
            
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
        

    def pprint(self):
        match self.altNo:
            case 1:
                self.Int.pprint()
            case 2:
                print(self.Id.getIdName(), end = "")
            case 3:
                print("(", end = "")
                self.Exp.pprint()
                print(")", end = "")
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
                                           