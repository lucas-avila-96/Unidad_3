
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
        self.__arregloCalefactor[self.__cantidad] = unCalefactor
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
        min = 9999999
        aux = None
        for i in range(self.__arregloCalefactor.size):
            if isinstance(self.__arregloCalefactor[i], Gas):
                x = self.__arregloCalefactor[i].calcularConsumo(costom3, cantidadm3)
                if x < min:
                    min = x
                    aux = self.__arregloCalefactor[i]
        return aux 
            

    def buscarMenorCostoElectrico(self, costokw, cantidadh):
        min = 9999999
        aux = None
        for i in range(self.__arregloCalefactor.size):
            if isinstance(self.__arregloCalefactor[i], Electrico):
                x = self.__arregloCalefactor[i].calcularConsumo(costokw, cantidadh)
                if x < min:
                    min = x
                    aux = self.__arregloCalefactor[i]
        return aux 

            
    def buscarMenorCosto(self):
        min = None
        aux = None
        for i in range(self.__arregloCalefactor.size):
            min = self.__arregloCalefactor[0].calcularConsumo()
            aux = self.__arregloCalefactor[i]

        
