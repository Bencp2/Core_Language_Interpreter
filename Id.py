from Singleton import Singleton


class Id:
    
    _IdList = list()
    
        
        
    def __init__(self, n):
        self.Name = n
        self.Decl = False
        self.Init = False
        self.Val = None

    @staticmethod
    def parseAssign():
        pointer = Singleton()
        if pointer.getToken() != 32:
            print("Invalid Token:", pointer.getToken())
            print("Should be an identifier but was", pointer.tokenString())
            quit() 
        if len(Id._IdList) == 0:
            print("Error: Nothing has not been declared")
            quit()
        else:
            for elm in Id._IdList:
                if elm.Name == pointer.idName():
                    pointer.skipToken()
                    return elm
            print("Error:", pointer.tokenString(),"has not been declared")
            quit()
            
    @staticmethod
    def parseDeclare():
        pointer = Singleton()
        if pointer.getToken() != 32:
            print("Invalid Token:", pointer.getToken())
            print("Should be an identifier but was", pointer.tokenString())
            quit()        
        if len(Id._IdList) == 0:
            x = Id(pointer.idName())
            Id._IdList.append(x)
        else:
            for elm in Id._IdList:
                if elm.Name == pointer.idName():
                    print("Error: Double Declaration of", pointer.tokenString())
                    quit()
            x = Id(pointer.idName())
            Id._IdList.append(x)
        pointer.skipToken()
        return x

    def declareId(self):
        self.Decl = True
        
    def setIdVal(self, value):
        
        if not self.Decl:
            print("Error:",self.Name,"has not been declared")
            quit()  
        else:
            self.Init = True
            self.Val = value
    
    def getIdVal(self):
        if not self.Decl:
            print("Error:",self.Name,"has not been declared")
            quit() 
        elif not self.Init:
            print("Error:",self.Name,"has not been initialized")
            quit()  
        else:
            return self.Val
    
    def getIdName(self):
        return self.Name
        