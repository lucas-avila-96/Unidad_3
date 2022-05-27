import numpy as np
import csv 
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

    def guardarArchivo(self):      
        myFile = open('Ejercicio3/Contratos.csv', 'w')
        writer = csv.writer(myFile, delimiter=';')
        for i in range(self.__arregloContratos.size):
            jugador = self.__arregloContratos[i].getJugador()
            equipo = self.__arregloContratos[i].getEquipo()
            dni = jugador.getDni()
            equipo = equipo.getNombre()
            fechaInicio = self.__arregloContratos[i].getFechaInicio()
            fechaFin = self.__arregloContratos[i].getFechaFin()
            pagoMensual = self.__arregloContratos[i].getPagoMensual()
            writer.writerow([dni, equipo, fechaInicio, fechaFin, pagoMensual])
        print("Escritura completa")

            

    