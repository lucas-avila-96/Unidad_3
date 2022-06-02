from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo



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
        
    def opcion1(self, listaPersonal):
        elemento = None
        tipo = input('Tipo: ')
        tipo.lower()
        if tipo == type(Docente).__name__.lower():
            #inputs
            #elemento = Docente()
            pass
        elif tipo == type(Investigador).__name__.lower():
            #inputs
            #elemento = Invesigador()
            pass
        elif tipo == type(DocenteInvestigador).__name__.lower():
            #inputs
            #elemento = DocenteInvesigador()
            pass
        elif tipo == type(PersonalApoyo).__name__.lower():
            #inputs
            #elemento = PersonalApoyo()
            pass
        listaPersonal.agregarElemento(elemento)

    def opcion2(self, listaPersonal):
        elemento = None
        tipo = input('Tipo: ')
        tipo.lower()
        pos = int(input('Posicion: '))
        if tipo == type(Docente).__name__.lower():
            #inputs
            #elemento = Docente()
            pass
        elif tipo == type(Investigador).__name__.lower():
            #inputs
            #elemento = Invesigador()
            pass
        elif tipo == type(DocenteInvestigador).__name__.lower():
            #inputs
            #elemento = DocenteInvesigador()
            pass
        elif tipo == type(PersonalApoyo).__name__.lower():
            #inputs
            #elemento = PersonalApoyo()
            pass
        listaPersonal.insertarElemento(elemento, pos)

    def opcion3(self, listaPersonal):
        print('Ingresar nombre de la carrera')
        carrera = input('Carrera: ')
        l = listaPersonal.listarDocentesInvestigadores(carrera)
        for pers in l:
            print(pers)
            
    def opcion4(self, listaPersonal):
        pass

    def opcion5(self, listaPersonal):
        pass

    def opcion6(self, listaPersonal):
        pass

    def opcion7(self, listaPersonal):
        pass

    def opcion8(self, listaPersonal):
        pass


    