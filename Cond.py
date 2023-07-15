from Singleton import Singleton
from Comp import Comp


class Cond:

    def __init__(self):
        self.Comp = None
        self.Cond1 = None
        self.Cond2 = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        match pointer.getToken():
            case 20:
                self.altNo = 1
                self.Comp = Comp()
                self.Comp.parse()
            case 15:
                self.altNo = 2
                pointer.skipToken()
                self.Cond1 = Cond()
                self.Cond1.parse()
            case 16:
                pointer.skipToken()
                self.Cond1 = Cond()
                self.Cond1.parse()
                if pointer.getToken() == 18:
                    self.altNo = 3
                elif pointer.getToken() == 19:
                    self.altNo = 4
                else:
                    print("Invalid Token:", pointer.getToken())
                    quit()                    
                pointer.skipToken()
                self.Cond2 = Cond()
                self.Cond2.parse()
                if pointer.getToken() != 17:
                    print("Invalid Token:", pointer.getToken())
                    print("Should be ] but was", pointer.tokenString())
                    quit()
                pointer.skipToken()
            case default:
                    print("Invalid Token:", pointer.getToken())
                    quit()

    def evaluate(self):
        match self.altNo:
            case 1:
                return self.Comp.evaluate()
                
            case 2:
                return not self.Cond1.evaluate()
                
            case 3:
                return self.Cond1.evaluate() and self.Cond2.evaluate()

            case 4:
                return self.Cond1.evaluate() or self.Cond2.evaluate()

            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
                                        
        
    def pprint(self):
        match self.altNo:
            case 1:
                self.Comp.pprint()
                
            case 2:
                print("!", end = "")
                self.Cond1.pprint()
                
            case 3:
                print("[", end = "")
                self.Cond1.pprint()
                print(" && ", end = "")
                self.Cond2.pprint()
                print("]", end = "")
                
            case 4:
                print("[", end = "")
                self.Cond1.pprint()
                print(" || ", end = "")
                self.Cond2.pprint()
                print("]", end = "")   
                
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
                                