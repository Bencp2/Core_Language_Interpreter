from Singleton import Singleton
from Id import Id
from Exp import Exp
from Tabs import Tabs

class Assign:
    
    def __init__(self):
        self.Id = None
        self.Exp = None
    
    def parse(self):
        pointer = Singleton()
        self.Id = Id.parseAssign()
        if pointer.getToken() != 14:
            print("Invalid Token:", pointer.getToken())
            print("Should be = but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.Exp = Exp()
        self.Exp.parse()
        if pointer.getToken() != 12:
            print("Invalid Token:", pointer.getToken())
            print("Should be ; but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        
    def execute(self):
        value = self.Exp.evaluate()
        self.Id.setIdVal(value)

    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "") 
        print(self.Id.getIdName(), end = "")
        print("=", end = "")
        self.Exp.pprint()
        print(";")        