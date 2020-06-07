from claseVehiculo import Vehiculo

class Nuevo(Vehiculo):
    Marca = ''
    __Version = ''

    @classmethod
    def getMarca (self):
        return self.Marca

    @classmethod
    def setMarca(self,marca):
        self.Marca = marca

    def __init__ (self,modelo,cantP,color,precioB,version):
        super().__init__(modelo,cantP,color,precioB)
        self.__Version = version.lower()

    def __str__ (self):
        print(super().__str__())
        return 'Marca = {} Version = {}'.format(self.Marca,self.__Version)

    def calcularImporte (self):
        resultado = self.getPrecioBase() + 0.1*self.getPrecioBase()
        if self.__Version == 'full':
            resultado += 0.02*self.getPrecioBase()
        return resultado

    def getTipo (self):
        return 'Nuevo'

    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __Marca__ = self.Marca,
            __atributos__ = dict(
                modelo = self.getModelo(),
                cantP = self.getCantPuertas(),
                color = self.getColor(),
                precioB = self.getPrecioBase(),
                version = self.__Version
                )
            )
        return d
