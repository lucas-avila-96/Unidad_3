
from zope.interface import Interface
from zope.interface import implementer

class IClase(Interface):
    def insertarElemento(elemento, posicion):
        pass

    def insertarElemento(elemento):
        pass

    def mostrarElemento(posicion):
        pass
    