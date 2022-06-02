
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op, manejadorCalefactor):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(manejadorCalefactor)
        else:
            func()
    
    def opcion1(self, manejadorCalefactor):
        print('Ingresar costo m^3')
        costo = input('Costo: ')
        print('Ingresar cantidad estimada en m^3')
        cantidad = input('Cantidad: ')
        c = manejadorCalefactor.buscarMenorCostoGas(costo, cantidad)
        print (c)

    def opcion2(self, manejadorCalefactor):
        print('Ingrese costo de el kilowatt/h')
        costo = input('Costo: ')
        print('Ingresar cantidad')
        cantidad = input('Cantidad: ')
        c = manejadorCalefactor.buscarMenorCostoElectrico(costo, cantidad)
        print(c)
        
    def opcion3(self, manejadorCalefactor):
        manejadorCalefactor.buscarMenorCosto()