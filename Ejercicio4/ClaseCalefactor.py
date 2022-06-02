import abc
from abc import ABC

class Calefactor(ABC):
    __marca = ''
    __modelo = ''

    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    
    @abc.abstractmethod 
    def calcularConsumo(self, costo, cantidad):
        pass

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo