from ClasePersonal import Personal

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
                            '8':self.opcion7,
                            }

    def opcion(self,op, listaPersonal):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(listaPersonal)
        else:
            func()
        
    def opcion1(self,op, listaPersonal):
        
        elemento = Personal()
        listaPersonal.agregarElemento(elemento)

    def opcion2(self,op, listaPersonal):
        pass

    def opcion3(self,op, listaPersonal):
        pass

    def opcion4(self,op, listaPersonal):
        pass

    def opcion5(self,op, listaPersonal):
        pass

    def opcion6(self,op, listaPersonal):
        pass

    def opcion7(self,op, listaPersonal):
        pass

    def opcion8(self,op, listaPersonal):
        pass


    