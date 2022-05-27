from zope.interface import implementer
import Interfaz
import Nodo

@implementer(Interfaz)
class Manejador:
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


    def agregarAparato(self, aparato):
        nodo = Nodo(aparato)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1


    def insertarElemento(self, elemento, pos):
        if pos == 0:
            self.__com = elemento
        else:
            pass
            
