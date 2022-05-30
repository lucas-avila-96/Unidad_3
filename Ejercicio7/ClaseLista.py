from zope.interface import implementer
import Interfaz
import Nodo

@implementer(Interfaz)
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

    def agregarItem(self, item):
        nodo = Nodo(item)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo = nodo
        self.__actual = nodo
        self.__tope += 1

    def size(self):
        cont = 0
        actual = self.__comienzo
        while actual != None:
            cont += 1
            actual = actual.getSiguiente()
        return cont

    def insertarElemento(self, pos, item):
        if pos > self.size() - 1:
            print('Error')
        actual = self.__comienzo
        anterior = None
        nuevo = Nodo(item)
        i = 0
        if pos == 0:
            nuevo.setSiguiente(self.__comienzo)
            self.__comienzo = nuevo
        else:
            actual = self.__comienzo
            anterior = None
            i = 0
            while i < pos:
                i += 1
                anterior = actual
                actual = actual.getSiguiente()
            anterior.setSiguiente(nuevo)
            nuevo.setSiguiente(actual)
        
    def insertarAlFinal(self, elemento):
        nuevo = Nodo(elemento)
        aux = self.__comienzo
        while aux.getSiguiente() != None:
            aux = aux.getSiguiente()
        aux.setSiguiente(nuevo)

    def listarDatos(self):
        aux = self.__comienzo
        while aux != None:
            print(aux.getDato())
            aux=aux.getSiguiente()