from ClaseEmpresa import Empresa
from ClaseBus import Bus
from ClaseBillete import Billete

def main():
    E = Empresa('Empresa Buses')

    salir = False
    while salir != True:
        operacion = input("""--------------------------
                          1. Crear bus
                          2. Venta de billetes
                          3. Devolucion de billetes
                          4. Estado de la venta
                          0. Salir
                          --------------------------
                          """)

        if operacion == "1" or operacion.casefold().capitalize() == "Crear bus":
            
            res_compra = comprar_billetes(plazas_bus)
            plazas_bus = res_compra[1]

            if res_compra[0] == 1:
                print("Has comprado los billetes")
            elif res_compra[0] == 0:
                print("No hay plazas suficientes\n")
            
        elif operacion == "2" or operacion.casefold().capitalize() == "Venta de billetes":
            
            res_compra = comprar_billetes(plazas_bus)
            plazas_bus = res_compra[1]

            if res_compra[0] == 1:
                print("Has comprado los billetes")
            elif res_compra[0] == 0:
                print("No hay plazas suficientes\n")

        elif operacion == "3" or operacion.casefold().capitalize() == "Devolucion de billetes":

            res_devolucion = devolver_billetes(plazas_bus, plazas_bus_totales)
            plazas_bus = res_devolucion[1]

            if res_devolucion[0] == 1:
                print("Has devuelto los billetes") 
            elif res_devolucion[0] == 0:
                print("Cantidad de plazas a devolver errónea\n")

        elif operacion == "4" or operacion.casefold().capitalize() == "Estado de la venta":
            
            print(estado_billetes(plazas_bus, plazas_bus_totales))

        elif operacion == "0" or operacion.casefold().capitalize() == "Salir":
            salir = True



main()    