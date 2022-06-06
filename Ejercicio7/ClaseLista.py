
from zope.interface import implementer
from ClaseDocenteInvestigador import DocenteInvestigador
from ClaseInvestigador import Investigador
from Interfaz import ILista
from Nodo import Nodo



@implementer(ILista)
class Lista:
    __comienzo = None
    __actual = None
    __indice = 0
    __tope = 0
    
    def __init__(self):
        self.__comienzo = None
        self.__actual = None
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.__indice == self.__tope:
            self.__actual = self.__comienzo
            self.__indice = 0
            raise StopIteration
        else:
            self.__indice += 1
            dato = self.__actual.getDato()
            self.__actual = self.__actual.getSiguiente()
            return dato

    def size(self):
        cont = 0
        actual = self.__comienzo
        while actual != None:
            cont += 1
            actual = actual.getSiguiente()
        return cont

    def agregarElemento(self, item):
        nodo = Nodo(item)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def insertarElemento(self, pos, item):
        if pos > self.size() - 1:
            raise IndexError()
        actual = self.__comienzo
        anterior = None
        i = 0
        if pos == 0:
            self.agregarElemento(item)
        else:
            nuevo = Nodo(item)
            actual = self.__comienzo
            anterior = None
            i = 0
            while i < pos:
                i += 1
                anterior = actual
                actual = actual.getSiguiente()
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(actual)

    def mostrarElemento(self, pos):
        aux = self.__comienzo
        i = 0
        while aux != None and i < pos:
            aux=aux.getSiguiente()
            i += 1
        if aux is not None:
            print(aux.getDato())

    def mostrarAgentesPorArea(self, area):
        aux = self.__comienzo
        contDocInv = 0
        contInv = 0
        while aux != None:
            if isinstance(aux, DocenteInvestigador):
                if aux.getDato().getCarrera() == area:
                    contDocInv += 1
            if isinstance(aux, Investigador):
                if aux.getDato().getCarrera() == area:
                    contInv += 1
            aux = aux.getSiguiente()
        print(f'Docentes Investigadores: {contDocInv}')
        print(f'Docentes Investigadores: {contInv}')

    def consultarTipoPersonal(self, pos):
        if pos > self.size() - 1:
            raise IndexError()
        aux = self.__comienzo
        pers = None
        i = 0
        while i < pos:
            pers = aux.getDato()
            aux = aux.getSiguiente()
            i += 1
        return pers

    def ordenarLista(self, lista):
        band = True
        while band:
            band = False
            for i in range(len(lista) - 1):
                if lista[i].getApellido() < lista[i + 1].getApellido():
                    lista[i], lista[i + 1] = lista[i + 1], lista[i]
                    band = True
        return lista

    def generarListaCarrera(self, carrera):
        aux = self.__comienzo
        pers = []
        while aux != None:
            if isinstance(aux, DocenteInvestigador):
                if aux.getDato().getCarrera() == carrera:
                    pers.append(aux.getDato())
            aux = aux.getSiguiente()
        return pers
    
    def generarListaCategoria(self, categoria):
        aux = self.__comienzo
        pers = []
        while aux != None:
            if isinstance(aux, DocenteInvestigador):
                if aux.getDato().getCategoria() == categoria:
                    pers.append(aux.getDato())
            aux = aux.getSiguiente()
        return pers
    
    def obtenerListado(self):
        aux= self.__comienzo
        lista = []
        while aux != None:
            lista.append(aux.getDato())
            aux = aux.getSiguiente()
        return lista


    def toJSON(self):
        lista = []
        aux= self.__comienzo
        while aux != None:
            lista.append(aux.getDato().toJSON())
            aux = aux.getSiguiente()
        d = dict(
            __class__ = self.__class__.__name__,
                agentes = lista
        )
        return d
    




    