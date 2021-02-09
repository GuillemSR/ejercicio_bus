class billete:

    def __init__(self, pName = None, pStatusCompra = False):
        self.name = pName
        self.statusCompra = pStatusCompra

    def SetName(self, pName):
        self.name = pName
    
    def GetName(self):
        return self.name

    def SetStatusCompra(self, pStatusCompra):
        self.statusCompra = pStatusCompra

    def GetStatusCompra(self):
        return self.statusCompra