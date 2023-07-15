from Singleton import Singleton
from Assign import Assign
from If import If
from Loop import Loop
from In import In
from Out import Out

class Stmt:
    
    def __init__(self):
        self.Assign = None
        self.If = None
        self.Loop = None
        self.In = None
        self.Out = None
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        match pointer.getToken():
            case 5:
                self.If = If()
                self.If.parse()
                self.altNo = 2
            case 8:
                self.Loop = Loop()
                self.Loop.parse()
                self.altNo = 3
            case 10:
                self.In = In()
                self.In.parse()
                self.altNo = 4
            case 11:
                self.Out = Out()
                self.Out.parse()
                self.altNo = 5
            case 32:
                self.Assign = Assign()
                self.Assign.parse()
                self.altNo = 1
            case default:
                print("Invalid Token:", pointer.getToken())
                quit()
        
        
        
        
    def execute(self):
        match self.altNo:
            case 1:  
                self.Assign.execute()
            case 2:
                self.If.execute()
            case 3:
                self.Loop.execute()
            case 4:
                self.In.execute()
            case 5:
                self.Out.execute()
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
        
                
        
    def pprint(self):
        match self.altNo:
            case 1:  
                self.Assign.pprint()
            case 2:
                self.If.pprint()
            case 3:
                self.Loop.pprint()
            case 4:
                self.In.pprint()
            case 5:
                self.Out.pprint()
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
                