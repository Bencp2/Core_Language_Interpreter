from Singleton import Singleton
from Cond import Cond
import SS
from Tabs import Tabs


class Loop:

    def __init__(self):
        self.Cond = None
        self.SS = None

    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 8:
            print("Invalid Token:", pointer.getToken())
            print("Should be while but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.Cond = Cond()
        self.Cond.parse()
        if pointer.getToken() != 9:
            print("Invalid Token:", pointer.getToken())
            print("Should be loop but was", pointer.tokenString())
            quit()        
        pointer.skipToken()
        self.SS = SS.SS()
        self.SS.parse()
        if pointer.getToken() != 3:
            print("Invalid Token:", pointer.getToken())
            print("Should be end but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        if pointer.getToken() != 12:
            print("Invalid Token:", pointer.getToken())
            print("Should be ; but was", pointer.tokenString())
            quit()
        pointer.skipToken()      
            
    def execute(self):
        while self.Cond.evaluate():
            self.SS.execute()
            
    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "") 
        print("while", end = " ")
        self.Cond.pprint()
        print(" loop")
        tabs.addTab()
        self.SS.pprint()
        tabs.removeTab()
        for i in range(0, tabsCount):
            print("\t", end = "")         
        print("end;")