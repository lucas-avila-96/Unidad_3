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
        '''
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
        '''
        elemento1 = Docente()
        elemento2 = Investigador()
        elemento3 = DocenteInvestigador()
        elemento4 = PersonalApoyo()
        listaPersonal.agregarElemento(elemento1)
        listaPersonal.agregarElemento(elemento2)
        listaPersonal.agregarElemento(elemento3)
        listaPersonal.agregarElemento(elemento4)

    def opcion2(self, listaPersonal):
        elemento = None
        tipo = input('Tipo: ')
        tipo.lower()
        pos = int(input('Posicion: '))
        elemento5 = Docente()
        try:
            listaPersonal.insertarElemento(elemento5, pos)
        except IndexError:
            print('Error de indice')
            
        '''
        if tipo == type(Docente).__name__.lower():
            inputs
            pass
        elif tipo == type(Investigador).__name__.lower():
            inputs
            pass
        elif tipo == type(DocenteInvestigador).__name__.lower():
            inputs
            pass
        elif tipo == type(PersonalApoyo).__name__.lower():
            inputs
            pass
        '''


    def opcion3(self, listaPersonal):
        print('Ingrese posicion')
        pos = int(input('Posicion'))
        try:
            pers = listaPersonal.consultarTipoPersonal(pos)
        except IndexError:
            print('Posicion no encontrada')
        
        print(f'El agente en la posicion {pos} es {type(pers).__name__}')


    def opcion4(self, listaPersonal):
        print('Ingrese carrera')
        carrera = input('Carrera: ')
        pers = listaPersonal.generarLista(carrera)
        lo = self.ordenarLista(pers)
        for pers in lo:
            print(pers)

    def opcion5(self, listaPersonal):
        pass

    def opcion6(self, listaPersonal):
        pass

    def opcion7(self, listaPersonal):
        pass

    def opcion8(self, listaPersonal):
        pass


    