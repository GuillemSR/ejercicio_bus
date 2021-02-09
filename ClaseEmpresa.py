from ClaseBus import Bus

class Empresa:
  def __init__(self, name):
    self.buses = []
    self.name = name
  
  def crear_bus(self, id, plazas):
    bus = Bus(id, plazas)
    self.buses.append(bus)