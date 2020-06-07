import json
from pathlib import Path
from claseManejaColeccion import ManejaColeccion
from claseNuevo import Nuevo
from claseUsado import Usado

class ObjectEncoder():

    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
            if class_name == 'ManejaColeccion':
                vehiculos = d['vehiculos']
                Nuevo.setMarca(d['__Marca__'])
                manejador = class_()
                for i in range(len(vehiculos)):
                    dVehiculo = vehiculos[i]
                    class_name = dVehiculo.pop('__class__')
                    class_ = eval(class_name)
                    atributos = dVehiculo['__atributos__']
                    unVehiculo = class_(**atributos)
                    manejador.agregarVehiculoDesdeArch(unVehiculo)
            return manejador

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)
            destino.close()

    def leerJSONArchivo(self,archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario=json.load(fuente)
            fuente.close()
            return diccionario
