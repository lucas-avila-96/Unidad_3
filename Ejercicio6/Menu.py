from ClaseHeladera import Heladera

class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,

                            }

    def opcion(self,op, listaAparatos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(listaAparatos)
        else:
            func()
    
    def opcion1(self, listaAparatos):
        elemento = Heladera('philips', 'mod1', 'blano', 'arg', '99999', '200L', True, True)
        pos = input('Posicion: ')
        listaAparatos.insertarElemento(elemento, pos)

    def opcion2(self, listaAparatos):
        pass 
    
    def opcion3(self, listaAparatos):
        pass

    def opcion4(self, listaAparatos):
        pass

    def opcion5(self, listaAparatos):
        pass

    def opcion6(self, listaAparatos):
        pass

    def opcion7(self, listaAparatos):
        pass