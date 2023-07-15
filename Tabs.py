
class Tabs:

    tabsCount = 0
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    
    def addTab(self):
        self.tabsCount += 1
        
    def removeTab(self):
        self.tabsCount -= 1
        
    def getTabCount(self):
        return self.tabsCount