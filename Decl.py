from Singleton import Singleton
from IdList import IdList
from Tabs import Tabs


class Decl:
    
    def __init__(self):
        self.IdList = None
        
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 4:
            print("Invalid Token:", pointer.getToken())
            print("Should be int but was", pointer.tokenString())
            quit()        
        pointer.skipToken()
        self.IdList = IdList()
        self.IdList.parse(1)
        if pointer.getToken() != 12:
            print("Invalid Token:", pointer.getToken())
            print("Should be ; but was", pointer.tokenString())
            quit()          
        pointer.skipToken()
        
        
    def execute(self):
        self.IdList.executeDecl()

    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "")
        print("int", end=" ")
        self.IdList.pprint()
        print(";")