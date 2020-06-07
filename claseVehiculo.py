class Vehiculo:
    __Modelo = ''
    __CantPuertas = 0
    __Color = ''
    __PrecioBase = 0.0

    def __init__ (self,modelo,cantP,color,precioB):
        self.__Modelo = modelo
        self.__CantPuertas = cantP
        self.__Color = color
        self.__PrecioBase = precioB

    def __str__ (self):
        return 'Modelo: {} Cant Puertas: {} Color: {} Precio Base: {}'.format(self.__Modelo,self.__CantPuertas,self.__Color,self.__PrecioBase)

    def getModelo (self):
        return self.__Modelo

    def getCantPuertas (self):
        return self.__CantPuertas

    def getColor (self):
        return self.__Color

    def getPrecioBase (self):
        return self.__PrecioBase

    def setPrecioB (self, nuevoPrecio):
        self.__PrecioBase = nuevoPrecio                    
