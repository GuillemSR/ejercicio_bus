from ClaseBillete import Billete

class Bus:

    def __init__(self, id, plazas):
        self.__plazas = plazas
        self.__billetes = [None]*self.__plazas
        self.__id = id


    def GetPlazas(self):
        return self.__plazas

    def GetBilletes(self):
        return self.__billetes

    def GetId(self):
        return self.__id

    def venta(self, name, cnt):
        contador = 0
        if self.__billetes.count(None) >= cnt:
            for i, billete in enumerate(self.__billetes):
                if billete is None:
                    self.__billetes[i] = Billete(name)
                    contador += 1
                    if contador >= cnt:
                        return 0
                else:
                    continue
            return 1

    def vuelta(self, name, cnt):
        list_names = []
        for i, billete in enumerate(self.__billetes):
            try:
                old = billete.GetName()
                if old == name:
                    list_names.append(i)
            except:
                pass
            
        
        if len(list_names) >= cnt:
            for i in range(cnt):
                self.__billetes[list_names[i]] = None
            return 0
        else:
            return 1

    def estadoVenta(self, id):
        cnt = 0
        for bus in self.__billetes:
            if bus is not None:
                cnt += 1
        return cnt