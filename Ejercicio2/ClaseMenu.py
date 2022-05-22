from ClaseRamo import Ramo
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            }

    def opcion(self,op, manejadorFlores, manejadorRamos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(manejadorFlores, manejadorRamos)
        else:
            func()
    
    def opcion1(self, manejadorFlores, manejadorRamos):
        print('ingresar tamaño del ramo')
        tamaño = input('Tamaño: ')
        unRamo = Ramo(tamaño)
        print('ingrese nombre de la flor para agregar o fin para finalizar')
        nombre = input('Nombre: ')
        while nombre != 'fin':
            unaFlor = manejadorFlores.buscarFlor(nombre)
            if unaFlor != None:
                unRamo.agregarFlor(unaFlor)
                print('Flor agregada con exito')
            else:
                print('Flor no encontrada. Reintente')
            nombre = input('Nombre: ')
        manejadorRamos.agregarVenta(unRamo)

    def opcion2(self, manejadorFlores, manejadorRamos):
        manejadorRamos.floresMasVendidas()

    def opcion3(self, manejadorFlores, manejadorRamos):
        tipo = input('Tipo de ramo: ')

        manejadorRamos.floresVendidasTipo(tipo)