import numpy as np
import csv
import Flores

class ManejadorFlores:
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension, incremento = 1) -> None:
        self.__arregloFlores = np.empty(dimension, dtype = Flores)
        self.__cantidad = 0
        self.__dimension = dimension

    def agregarFlores(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloFlores.resize(self.__dimension)
        self.__arregloFlores[self.__cantidad] = unaFlor
        self.__cantidad += 1
        
    def testFlores(self):
        archivo = open('flores.csv')
        reader = csv.reader(archivo, ';')

        for fila in reader:
            numero, nombre, color, descripcion = fila[0], fila[1], fila[2], fila[3]
            unaFlor = Flores(numero, nombre, color, descripcion)
            self.agregarFlores(unaFlor)