from Singleton import Singleton

class CompOp:
    
    def __init__(self):
        self.altNo = None
        
    def parse(self):
        pointer = Singleton()
        match pointer.getToken():
            case 25:
                self.altNo = 1
            case 26:
                self.altNo = 2
            case 27:
                self.altNo = 3
            case 28:
                self.altNo = 4
            case 29:
                self.altNo = 5
            case 30:
                self.altNo = 6
            case default:
                print("Invalid Token:", pointer.getToken())
                quit()
        pointer.skipToken()        
        
    def getCompOp(self):
        return self.altNo
                                           

    def pprint(self):
        match self.altNo:
            case 1:
                print(" != ", end = "")
            case 2:
                print(" == ", end = "")
            case 3:
                print(" < ", end = "")
            case 4:
                print(" > ", end = "")
            case 5:
                print(" <= ", end = "")
            case 6:
                print(" >= ", end = "")
            case default:
                print("Error:", self.altNo,"is an invalid altNo")
                quit()
                                           