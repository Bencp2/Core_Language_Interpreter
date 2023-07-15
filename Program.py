from Singleton import Singleton
from DS import DS
from SS import SS
from Tabs import Tabs

class Program:


    def __init__(self):
        self.DS = None
        self.SS = None
        
    
    def parse(self):
        pointer = Singleton()
        if pointer.getToken() != 1:
            print("Invalid Token:", pointer.getToken())
            print("Should be program but was", pointer.tokenString())
            quit()
        pointer.skipToken()
        self.DS = DS()
        self.DS.parse()
        if pointer.getToken() != 2:
            print("Invalid Token:", pointer.getToken())
            print("Should be begin but was", pointer.tokenString())
            quit()        
        pointer.skipToken()
        self.SS = SS()
        self.SS.parse()
        if pointer.getToken() != 3:
            print("Invalid Token:", pointer.getToken())
            print("Should be end but was", pointer.tokenString())
            quit()            
        pointer.skipToken()
        
        
    def execute(self):
        self.DS.execute()
        self.SS.execute()
        
    def pprint(self):
        print("program")
        tabs = Tabs()
        tabs.addTab()
        self.DS.pprint()
        print("begin")
        self.SS.pprint()
        tabs.removeTab()
        print("end")