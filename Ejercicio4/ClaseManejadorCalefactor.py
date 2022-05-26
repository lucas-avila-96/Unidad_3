import numpy as np
import csv
from ClaseCalefactor import Calefactor
class ManejadorCalefactor:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension):
        self.__arregloCalefactor = np.empty(dimension, dtype = Calefactor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = 1

    def agregarCalefactor(self, unCalefactor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloCalefactor.resize(self.__dimension)
        self.__arregloCalefactor[self.__cantidad]=unCalefactor
        self.__cantidad += 1

    def leerArchivo(self):
        archivo = open('calefactor-electrico.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            marca, modelo, potencia = fila[0], fila[1], fila[2]
            unCalefactor = Calefactor(marca, modelo, potencia)
            self.agregarCalefactor(unCalefactor)
        archivo.close()

        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            marca, modelo, matricula, calorias = fila[0], fila[1], fila[2], fila[3]
            unCalefactor = Calefactor(marca, modelo, matricula, calorias)
            self.agregarCalefactor(unCalefactor)
        archivo.close()
