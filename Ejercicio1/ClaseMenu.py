from ManejaFacultades import ManejaFacultades
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            }
    def opcion(self,op, manejador):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2':
            func(manejador)
        else:
            func()
    
    def opcion1(self, manejador):
        manejador.listarCarrerasFacultad()
        
    def opcion2(self, manejador):
        manejador.mostrarDatosCarrera()