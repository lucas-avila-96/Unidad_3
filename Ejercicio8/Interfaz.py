
from zope.interface import Interface

class ILista(Interface):
    def insertarElemento(elemento, posicion):
        pass

    def agregarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass
    