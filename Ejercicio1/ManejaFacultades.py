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
                    self.agregarFacultad(nueva)
                    facu = fila
                    listaCarrera = []
        
    def buscarFacultad(self):
        print('Ingresar codigo de facultad')
        cod = int(input('Codigo'))
        band = False
        i = 0
        facu = None
        while i <  len(self.__listaFacultades) and not band:
            if int(self.__listaFacultades[i].getCodigo()) == cod:
                band = True
            else: 
                i += 1

        if band == True:
            facu = self.__listaFacultades[i]
        return facu

    def listarDatosCarreras(self):
        facu = self.buscarFacultad()
        if facu != None:
            print(f'{facu.getNombre()}')
            for carrera in facu.getCarreras():
                print(f'{carrera.getNombre()}')
                print(f'{carrera.getDuracion()}')
        else: 
            print('no se encontro')
