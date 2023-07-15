from Singleton import Singleton
from IdList import IdList
from Tabs import Tabs

class Out:
    
    def __init__(self):
        self.IdList = None
    
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 11:
            print("Invalid Token:", pointer.getToken())
            print("Should be read but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.IdList = IdList()
        self.IdList.parse(2)
        if pointer.getToken() != 12:
            print("Invalid Token:", pointer.getToken())
            print("Should be ; but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        
        
    def execute(self):
        self.IdList.executePrint()

    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "")   
        print("write", end = " ")
        self.IdList.pprint()
        print(";")                    
            
        