from ClaseBillete import Billete

class Bus:

  def __init__(self, id, plazas):
    self.plazas = plazas
    self.billetes = [None]*self.plazas
    self.id = id

  def venta(self, name, cnt):
    contador = 0
    if self.billetes.count(None) <= cnt:
      while contador < cnt:
        for i, billete in enumerate(self.billetes):
          if billete is None:
            self.billetes[i] = Billete(name)
            contador += 1
    else:
      print('La venta no es posible')

  def vuelta(self, canti, name):
    list_names = []
    for i in range(len(self.billetes)):
      old = self.billetes[i].GetName()
      if old == name:
        list_names.append(i)
    if len(list_names) >= canti:
      for i in canti:
        self.billetes[list_names[i]] = None
    else:
      print('La devolucion no es posible')