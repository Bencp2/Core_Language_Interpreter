from Singleton import Singleton
from Cond import Cond
import SS
from Tabs import Tabs

class If:

    def __init__(self):
        self.Cond = None
        self.SS1 = None
        self.SS2 = None
        self.altNo = None

    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 5:
            print("Invalid Token:", pointer.getToken())
            print("Should be if but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.Cond = Cond()
        self.Cond.parse()
        if pointer.getToken() != 6:
            print("Invalid Token:", pointer.getToken())
            print("Should be then but was", pointer.tokenString())
            quit()        
        pointer.skipToken()
        self.SS1 = SS.SS()
        self.SS1.parse()
        if pointer.getToken() == 3:
            self.altNo = 1
            pointer.skipToken()
            if pointer.getToken() != 12:
                print("Invalid Token:", pointer.getToken())
                print("Should be ; but was", pointer.tokenString())
                quit()
            pointer.skipToken()
        elif pointer.getToken() == 7:
            self.altNo = 2
            pointer.skipToken()
            self.SS2 = SS.SS()
            self.SS2.parse()
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
        if self.Cond.evaluate():
            self.SS1.execute()
            
        elif self.altNo == 2:
            self.SS2.execute()
            
    def pprint(self):
        tabs = Tabs()
        tabsCount = tabs.getTabCount()
        for i in range(0, tabsCount):
            print("\t", end = "") 
        print("if", end = " ")
        self.Cond.pprint()
        print(" then")
        tabs.addTab()
        self.SS1.pprint()
        tabs.removeTab()
        for i in range(0, tabsCount):
            print("\t", end = "") 
        if self.altNo == 2:
            print("else")
            tabs.addTab()
            self.SS2.pprint()
            tabs.removeTab()
            for i in range(0, tabsCount):
                print("\t", end = "") 
        print("end;")