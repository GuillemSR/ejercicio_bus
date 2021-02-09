class Billete:

    def __init__(self, pName):
        self.name = pName

    def SetName(self, pName):
        self.name = pName
    
    def GetName(self):
        return self.name