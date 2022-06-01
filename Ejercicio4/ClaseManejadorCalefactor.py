import numpy as np
import csv
from ClaseCalefactor import Calefactor
from ClaseElectrico import Electrico
from ClaseGas import Gas
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
            unCalefactor = Electrico(marca, modelo, potencia)
            self.agregarCalefactor(unCalefactor)
        archivo.close()

        archivo = open('calefactor-a-gas.csv')
        reader = csv.reader(archivo, delimiter = ';')
        for fila in reader:
            marca, modelo, matricula, calorias = fila[0], fila[1], fila[2], fila[3]
            unCalefactor = Gas(marca, modelo, matricula, calorias)
            self.agregarCalefactor(unCalefactor)
        archivo.close()
    

    def buscarMenorCostoGas(self, costom3, cantidadm3):
        calefMenorCosto = None
        for i in range(self.__arregloCalefactor.size):
            if isinstance(self.__arregloCalefactor[i], Gas):
                self.__arregloCalefactor[i].calcularCosto(costom3, cantidadm3)

    def buscarMenorCostoElectrico(self, costokw, cantidadh):
        calefMenorCosto = None
        costo = 0
        for i in range(self.__arregloCalefactor.size):
            if isinstance(self.__arregloCalefactor[i], Electrico):
                self.__arregloCalefactor[i].calcularCosto(costokw, cantidadh)
            
    def buscarMenorCosto(self):
        calefMenorCosto = None
        for i in range(self.__arregloCalefactor.size):
            self.__arregloCalefactor[i].calcularCosto()
