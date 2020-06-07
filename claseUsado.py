from claseVehiculo import Vehiculo

class Usado(Vehiculo):
    __Marca = ''
    __Patente = ''
    __Anio = 0
    __Kilometraje = 0.0

    def __init__ (self,modelo,cantP,color,precioB,marca,patente,anio,kilometraje):
        super().__init__(modelo,cantP,color,precioB)
        self.__Marca = marca
        self.__Patente = patente
        self.__Anio = anio
        self.__Kilometraje = kilometraje

    def __str__ (self):
        print(super().__str__())
        return 'Marca = {} Patente = {} Año = {} Kilometraje = {}'.format(self.__Marca,self.__Patente,self.__Anio,self.__Kilometraje)

    def calcularImporte (self):
        resultado = self.getPrecioBase() - 0.01*self.getPrecioBase()*(2020 - self.__Anio)
        if self.__Kilometraje > 100000:
            resultado -= 0.02*self.getPrecioBase()
        return resultado

    def getTipo (self):
        return 'Usado'

    def getPatente (self):
        return self.__Patente            

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                modelo = self.getModelo(),
                cantP = self.getCantPuertas(),
                color = self.getColor(),
                precioB = self.getPrecioBase(),
                marca = self.__Marca,
                patente = self.__Patente,
                anio = self.__Anio,
                kilometraje = self.__Kilometraje
                )
            )
        return d
