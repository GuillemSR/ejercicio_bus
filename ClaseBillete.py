class Billete:

    def __init__(self, pName):
        self.__name = pName

    def SetName(self, pName):
        self.__name = pName
    
    def GetName(self):
        return self.__name