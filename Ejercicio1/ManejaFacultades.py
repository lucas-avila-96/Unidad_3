import csv
from ClaseFacultad import Facultad

class ManejaFacultades:
    __listaFacultades = []

    def __init__(self):
        self.__listaFacultades = []

    def agregarFacultad(self, unaFacultad):
        self.__listaFacultades.append(unaFacultad)

    def testFacultades(self):
        archivo = open('Facultades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        band = True
        for fila in reader:
            if band == True:
                facu = fila
                band = False
                listaCarrera = []
            else:
                if fila[0] == facu[0]:
                    listaCarrera.append(fila)
                else: 
                    nueva = self.__listaFacultades.append(fila[0], fila[1], fila[2], fila[3], fila[4], listaCarrera)
                    self.__listaFacultades(nueva)
                    facu = fila
                    listaCarrera = []