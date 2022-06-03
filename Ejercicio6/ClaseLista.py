
from zope.interface import implementer
from Interfaz import ILista
from Nodo import Nodo
from ClaseLavarropa import Lavarropa

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

    def insertarElemento(self, item, pos):
        if pos > self.size() - 1:
            raise IndexError
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

    def consultarTipoAparato(self, pos):
        aux = self.__comienzo
        ap = None
        i = 0
        while aux != None and i < pos:
            ap = aux.getDato()
            aux = aux.getSiguiente()
            i += 1
        print(f'El aparato en la posicion {pos} es {type(ap).__name__}')

    def calcularCantidadPorMarca(self, marca):
        aux = self.__comienzo
        c = 0
        i = 0
        while aux != None:
            ap = aux.getDato()
            if ap.getMarca() == marca:
                c += 1
            aux = aux.getSiguiente()
            i += 1
        return c
    
    def obtenerLavarropasCargaSuperior(self):
        aux = self.__comienzo
        lista = []
        i = 0
        while aux != None:
            ap = aux.getDato()
            if isinstance(ap, Lavarropa):
                lista.append(ap)
            aux = aux.getSiguiente()
            i += 1
        return lista

    def mostrarDatos(self):
        aux = self.__comienzo
        i = 0
        while aux != None:
            ap = aux.getDato()
            print(f'Marca: {ap.getMarca()}')
            print(f'Pais de fabricacion: {ap.getPaisDeFabricacion()}')
            print(f'Precio: {ap.getImporteVenta()}')
            aux = aux.getSiguiente()
            i += 1

    def toJSON(self):
        ap = []
        aux= self.__comienzo
        while aux != None:
            ap.append(aux.getDato().toJSON())
            aux= aux.getSiguiente()
        d = dict(
        __class__ = self.__class__.__name__,
            aparatos = ap
        )
        return d
    