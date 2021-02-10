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
            
            num_bus = int(input('Cual es el número del bus que deseas crear? '))
            plazas = int(input('Cuantas plazas tiene el bus? '))

            E.crear_bus(num_bus, plazas)
            print('Bus creado!')
            
        elif operacion == "2" or operacion.casefold().capitalize() == "Venta de billetes":
            
            id_bus = int(input('Cual es el número del bus? '))
            if E.BusExist(id_bus):
                plazas_compra = int(input('Cuantas plazas quieres comprar? '))
                nombre = input('Introduce tu nombre: ')
                if E.GetBus(id_bus).venta(nombre, plazas_compra) == 0:
                    print('Billetes comprados!')
                else:
                    print('No se han podido comprar los billetes.')

        elif operacion == "3" or operacion.casefold().capitalize() == "Devolucion de billetes":

            id_bus = int(input('Cual es el número del bus? '))
            if E.BusExist(id_bus):
                plazas_devolver = int(input('Cuantas plazas quieres devolver? '))
                nombre = input('Introduce tu nombre: ')
                if E.GetBus(id_bus).vuelta(nombre, plazas_devolver) == 0:
                    print('Billetes han sido devueltos!')
                else:
                    print('La devolucion no es posible')

        elif operacion == "4" or operacion.casefold().capitalize() == "Estado de la venta":
            
            id_bus = int(input('De que bus quieres comprobar el estado? '))
            bus = E.GetBus(id_bus)
            plazas_totales = bus.GetPlazas()
            plazas_vendidas = bus.estadoVenta(id_bus)

            print(f'El bus {id_bus} tiene {plazas_totales} plazas y se han vendido {plazas_vendidas} billetes.')

        elif operacion == "0" or operacion.casefold().capitalize() == "Salir":
            salir = True



main()    