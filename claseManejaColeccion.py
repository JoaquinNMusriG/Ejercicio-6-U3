from claseColeccion import Coleccion
from claseNuevo import Nuevo
from claseUsado import Usado

class ManejaColeccion:
    __vehiculos = None

    def __init__ (self):
        self.__vehiculos = Coleccion()

    def agregarVehiculoDesdeArch(self,unVehiculo):
        self.__vehiculos.agregarElemento(unVehiculo)

    def crearVehiculo (self):
        tipo = input('Ingrese la opcion de tipo de vehiculo(1 = Nuevo ; 2 = Usado): ')
        unVehiculo = None
        if (tipo == '1') or (tipo == '2'):
            modelo = input('Ingrese el modelo del auto: ')
            cantP = input('Ingrese la cantidad de puertas del vehiculo: ')
            if cantP.isdigit():
                cantP = int(cantP)
                color = input('Ingrese el color del vehiculo: ')
                if color.isalpha():
                    precioB = input('Ingrese el precio base del vehiculo: ')
                    try:
                        precioB = float(precioB)
                        if tipo == '1':
                            version = input('Ingrese la version del vehiculo (base o full): ')
                            if (version.lower() == 'base') or (version.lower() == 'full'):
                                unVehiculo = Nuevo(modelo,cantP,color,precioB,version)
                            else:
                                print('Version inválida.')
                        else:
                            marca = input('Ingrese la marca del vehiculo: ')
                            patente = input('Ingrese la patente del vehiculo: ')
                            anio = input('Ingrese el año del vehiculo: ')
                            if anio.isdigit():
                                anio = int(anio)
                                kilometraje = input('Ingrese el kilometraje del vehiculo: ')
                                try:
                                    kilometraje = float(kilometraje)
                                    unVehiculo = Usado(modelo,cantP,color,precioB,marca,patente,anio,kilometraje)
                                except ValueError:
                                    print('Kilometraje inválido.')
                            else:
                                print('Año inválido.')
                    except ValueError:
                        print('Precio inválido.')
                else:
                    print('Color inválido.')
            else:
                print('Cantidad de puertas inválida.')
        else:
            print('Opcion incorrecta.')
        return unVehiculo

    def insertarVehi (self,pos):
        unVehiculo = self.crearVehiculo()
        if unVehiculo != None:
            try:
                self.__vehiculos.insertarElemento(unVehiculo,pos)
                print('Vehiculo agregado.')
            except IndexError:
                print('No es posible agregar (list index out of range).')
        else:
            print('No se pudo agregar un vehiculo.')

    def agregarVehiculoFinal(self):
        unVehiculo = self.crearVehiculo()
        if unVehiculo != None:
            try:
                self.__vehiculos.agregarElemento(unVehiculo)
                print('Vehiculo agregado.')
            except IndexError:
                print('No es posible agregar (list index out of range).')
        else:
            print('No se pudo agregar un vehiculo.')

    def tipoVehi (self,pos):
        try:
            self.__vehiculos.mostrarElemento(pos)
        except IndexError:
            print('No es posible mostrar.')

    def buscPatente_cambPrecio (self, patente):
        band = False
        i = 0
        while (i < (self.__vehiculos.getTope())) & (not band):
            vehiculo = self.__vehiculos.getElemento(i)
            if isinstance(vehiculo,Usado):
                if vehiculo.getPatente() == patente:
                    band = True
                    nuevoPrecio = input('Ingrese el nuevo precio base del vehiculo: ')
                    try:
                        nuevoPrecio = float(nuevoPrecio)
                        vehiculo.setPrecioB(nuevoPrecio)
                        print('El nuevo precio de venta es: {}'.format(vehiculo.calcularImporte()))
                    except ValueError:
                        print('Precio inválido.')
            i += 1
        if (not band):
            print('No hay un vehiculo usado con esa patente.')

    def mostrarEconomico (self):
        min = 999999
        for vehiculo in self.__vehiculos:
            if (vehiculo.calcularImporte() < min):
                min = vehiculo.calcularImporte()
        print('Vehiculo mas economico: ')
        for vehiculo in self.__vehiculos:
            if (vehiculo.calcularImporte() == min):
                print(vehiculo)
                print('Precio de venta: {}'.format(min))
                print('-------------')

    def mostrarTodos (self):
        for vehiculo in self.__vehiculos:
            print('Modelo: {}'.format(vehiculo.getModelo()))
            print('Cantidad de puertas: {}'.format(vehiculo.getCantPuertas()))
            print('Importe de venta: {}'.format(vehiculo.calcularImporte()))
            print('----------')

    def mostrarDatos(self):
        for vehiculo in self.__vehiculos:
            print(vehiculo)

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __Marca__ = Nuevo.getMarca(),
            vehiculos = [vehiculo.toJSON() for vehiculo in self.__vehiculos]
            )
        return d
