from Singleton import Singleton
from IdList import IdList
import Id
from Tabs import Tabs


class In:
    
    def __init__(self):
        self.IdList = None
    
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 10:
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
        self.IdList.executeRead()
            

    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "")      
        print("read", end = " ")
        self.IdList.pprint()
        print(";")
            
        