from Singleton import Singleton
from Scanner import Tokenizer

class Int:
    
    def __init__(self):
        self.Int = None

    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 31:
            print("Invalid Token:", pointer.getToken())
            print("Should be an unsigned integer but was", pointer.tokenString())
            quit()            
        self.Int = pointer.intVal()
        pointer.skipToken()
        
    def getIntVal(self):
        return self.Int
        
    def pprint(self):
        print(self.Int, end = "")