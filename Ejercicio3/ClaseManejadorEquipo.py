import numpy as np
from ClaseEquipo import Equipo

class ManejadorEquipo:
    __dimension = 0
    __cantidad = 0
    __incremento = 0

    def __init__(self, dimension = 1, incremento = 1):
        self.__arregloEquipos = np.empty(dimension, dtype = Equipo)
        self.__cantidad = 0
        self.__dimension = dimension
        self.__incremento = incremento

    def agregarEquipo(self, unEquipo):
        if self.__cantidad == self.__dimension:
            self.__dimension += self.__incremento
            self.__arregloEquipos.resize(self.__dimension)
        self.__arregloEquipos[self.__cantidad]=unEquipo
        self.__cantidad += 1

    def leerArchivo(self):
        unEquipo = Equipo('Boca', 'Buenos Aires')
        otroEquipo = Equipo('River', 'Buenos Aires')
        self.agregarEquipo(unEquipo)
        self.agregarEquipo(otroEquipo)



    def buscarEquipo(self):
        unEquipo = None
        print('Ingrese el identificador')
        for i in range(self.__arregloEquipos.size):
            print(f'{i + 1} - {self.__arregloEquipos[i]}')
        id = int(input('Id: '))
        unEquipo = self.__arregloEquipos[id - 1]
        return unEquipo
