from ClasePersonal import Personal
from ClaseDocente import Docente
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from ClasePersonalApoyo import PersonalApoyo
import json
from ClaseObjectEncoder import ObjectEncoder

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
                            '8':self.opcion8,
                            }

    def opcion(self,op, listaAgentes):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3' or op == '4' or op == '5' or op == '6' or op == '7' or op == '8':
            func(listaAgentes)
        else:
            func()
    
    def opcion1(self, listaAgentes):
        elemento5 = None
        tipo = input('Tipo: ')
        tipo.lower()
        pos = int(input('Posicion: '))
        elemento5 = Docente()
        try:
            listaAgentes.insertarElemento(elemento5, pos)
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
        
    def opcion2(self, listaAgentes):
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
        elemento1 = DocenteInvestigador(41223444, 'Diaz', 'Martin',150000, 5, 'LCC', 'Profesor','POO', 'area2', 'tipo2', 'incentivo', 20000)
        #elemento2 = Docente(31455451, 'Lopez', 'Matias',140000, 5, 'LCC', 'Profesor','Discreta')
        #elemento3 = Investigador(41223444, 'Juarez', 'Roberto',150000, 5, 'area1', 'tipo1')
        #elemento4 = PersonalApoyo(41223444, 'Perez', 'Pablo',150000, 5, 'categoria1')
        listaAgentes.agregarElemento(elemento1)
        #listaAgentes.agregarElemento(elemento2)
        #listaAgentes.agregarElemento(elemento3)
        #listaAgentes.agregarElemento(elemento4)



    def opcion3(self, listaAgentes):
        print('Ingrese posicion')
        pos = int(input('Posicion'))
        pers = None
        try:
            pers = listaAgentes.consultarTipoPersonal(pos)
        except IndexError:
            print('Posicion no encontrada')

        print(f'El aparato en la posicion {pos} es {type(pers).__name__}')


    def opcion4(self, listaAgentes):
        print('Ingrese carrera')
        carrera = input('Carrera: ')
        pers = listaAgentes.generarListaPorCarrera(carrera)
        lo = self.ordenarLista(pers)
        for pers in lo:
            print(pers)

    def opcion5(self, listaAgentes):
        print('Ingrese area de investigacion')
        area = int(input('Area'))
        listaAgentes.mostrarAgentesPorArea(area)
        
    def opcion6(self, listaAgentes):
        pers = listaAgentes.obtenerListado()
        lo = self.ordenarLista(pers)
        for agente in lo:
            print(f'Tipo de agente: {type(agente).__name__}')
            print(f'Sueldo: {agente.getSueldoBasico()}')

    def opcion7(self, listaAgentes):
        print('Ingrese categoria')
        categoria = input('Categoria: ')
        pers = listaAgentes.generarListaPorCategoria(categoria)
        for agente in pers:
            print(f'{agente.getApellido()}')
            print(f'{agente.getNombre()}')
            print(f'{agente.getImporteExtra()}')

    def opcion8(self, listaAgentes):
        jsonF = ObjectEncoder()
        d = listaAgentes.toJSON()
        jsonF.guardarJSONArchivo(d,'Ejercicio8\Personal.json')


    