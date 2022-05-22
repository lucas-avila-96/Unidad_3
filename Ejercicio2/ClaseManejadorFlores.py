import numpy as np
import csv
from ClaseFlor import Flor

class ManejadorFlores:
    __cantidad = 0
    __dimension = 0
    __incremento = 0

    def __init__(self, dimension = 0, incremento = 1):
        self.__arregloFlores = np.empty(dimension, dtype = Flor)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarFlores(self, unaFlor):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloFlores.resize(self.__dimension)
        self.__arregloFlores[self.__cantidad] = unaFlor
        self.__cantidad += 1
        
    def leerArchivo(self):
        archivo = open('Ejercicio2\Libro1.csv')
        reader = csv.reader(archivo, delimiter = ';')
        #self.__dimension = len(archivo.readlines())
        for fila in reader:
            numero, nombre, color, descripcion = fila[0], fila[1], fila[2], fila[3]
            unaFlor = Flor(numero, nombre, color, descripcion)
            self.agregarFlores(unaFlor)
    
    def buscarFlor(self, nombre):
        unaFlor = None
        i = 0
        band = False
        while i < self.__arregloFlores.size and not band:
            if self.__arregloFlores[i].getNombre() == nombre:
                unaFlor = self.__arregloFlores[i]
                band = True
            else:
                i += 1
        return unaFlor