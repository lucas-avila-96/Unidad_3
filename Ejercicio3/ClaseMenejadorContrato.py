import numpy as np
from ClaseContrato import Contrato
class ManejadorContrato:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloContratos = np.empty(dimension, dtype = Contrato)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarContrato(self, unContrato):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloContratos.resize(self.__dimension)
        self.__arregloContratos[self.__cantidad]=unContrato
        self.__cantidad += 1


    