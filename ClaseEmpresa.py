from ClaseBus import Bus

class Empresa:
    def __init__(self, name):
      self.__buses = []
      self.__name = name

    def GetBuses(self):
        return self.__buses

    def GetBus(self, id):
        if self.BusExist(id):
            for bus in self.__buses:
                if bus.GetId() == id:
                    return bus      
  
    def crear_bus(self, id, plazas):
        bus = Bus(id, plazas)
        self.__buses.append(bus)

    def BusExist(self, id):
        for bus in self.__buses:
            if bus.GetId() == id:
                return True
            else:
                return False
         