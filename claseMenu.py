class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 0:self.salir,
                            1:self.insertarVehiculoPos,
                            2:self.agregarVehiculo,
                            3:self.tipoVehiculoPos,
                            4:self.modificarPrecioPat,
                            5:self.vehiculoEconomico,
                            6:self.mostrarVehiculos,
                            7:self.almacenarVehiculos,
                         }
    def getSwitcher(self):
        return self.__switcher
    def opcion(self, op, jsonF, vehiculos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(jsonF, vehiculos)
    def salir(self, jsonF, vehiculos):
        print('Salir')

    def insertarVehiculoPos(self, jsonF, vehiculos):
        pos = input('Ingrese la posicion en la que quiere insertar el vehiculo: ')
        try:
            pos = int(pos)
            vehiculos.insertarVehi(pos)
        except ValueError:
            print('Posicion inválida.')

    def agregarVehiculo(self, jsonF, vehiculos):
        vehiculos.agregarVehiculoFinal()

    def tipoVehiculoPos(self, jsonF, vehiculos):
        pos = input('Ingrese la posicion de la que quiere saber el tipo de vehiculo almacenado en ella: ')
        try:
            pos = int(pos)
            vehiculos.tipoVehi(pos)
        except ValueError:
            print('Posicion inválida.')

    def modificarPrecioPat(self, jsonF, vehiculos):
        patente = input('Ingrese la patente a buscar: ')
        vehiculos.buscPatente_cambPrecio(patente)

    def vehiculoEconomico(self, jsonF, vehiculos):
        vehiculos.mostrarEconomico()

    def mostrarVehiculos(self, jsonF, vehiculos):
        vehiculos.mostrarTodos()

    def almacenarVehiculos(self, jsonF, vehiculos):
        d = vehiculos.toJSON()
        jsonF.guardarJSONArchivo(d,'vehiculos.json')
        print('Vehiculos almacenados.')
