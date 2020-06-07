from claseManejaColeccion import ManejaColeccion
from claseObjectEncoder import ObjectEncoder
from claseMenu import Menu

if __name__ == '__main__':
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('vehiculos.json')
    vehiculos = jsonF.decodificarDiccionario(diccionario)

    menu=Menu()
    salir = False
    while not salir:
        print("""
              0 Salir
              1 Insertar vehiculo en una posicion.
              2 Agregar vehiculo
              3 Por posicion mostrar tipo de vehiculos
              4 Modificar precio base por medio de la patente (mostrar nuevo precio de venta)
              5 Mostrar Datos del vehiculo mas económino
              6 Mostrar modelo, cantidad de puertas e importe de venta de cada vehiculo
              7 Almacenar vehiculos en vehiculos.json""")
        op = int(input('Ingrese una opcion: '))
        menu.opcion(op,jsonF,vehiculos)
        salir = op == 0
