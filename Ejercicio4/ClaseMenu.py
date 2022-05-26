
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
        pass

    def opcion2(self, manejadorCalefactor):
        pass

    def opcion3(self, manejadorCalefactor):
        pass