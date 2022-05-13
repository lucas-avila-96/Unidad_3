import csv
from ClaseFacultad import Facultad

class ManejaFacultades:
    __listaFacultades = []

    def __init__(self):
        self.__listaFacultades = []

    def testFacultades(self):
        archivo = open('Ejercicio1\Facultades.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera==True:
                facu = fila
                bandera = False
                listaCarrera = []
            elif fila[0] == facu[0]:
                listaCarrera.append(fila)
            else:
                nuevaFacultad = Facultad(facu[0],facu[1],facu[2],facu[3],facu[4],listaCarrera)
                self.__listaFacultades.append(nuevaFacultad)
                facu = fila
                listaCarrera=[]
        nuevaFacultad = Facultad(facu[0],facu[1],facu[2],facu[3],facu[4],listaCarrera)
        self.__listaFacultades.append(nuevaFacultad)
        archivo.close()
        
    def buscarFacultad(self):
        facu = None
        band = False
        i = 0
        print('Ingresar codigo de facultad')
        cod = int(input('Codigo'))
        while i <  len(self.__listaFacultades) and not band:
            if int(self.__listaFacultades[i].getCodigo()) == cod:
                band = True
            else: 
                i += 1

        if band == True:
            facu = self.__listaFacultades[i]
        
        return facu

    def listarCarrerasFacultad(self):
        facu = self.buscarFacultad()
        if facu != None:
            print(f'{facu.getNombre()}')
            print('\t---------------Carreras---------------')
            print('{:<50}{:<25}'.format('Nombre Carrera','Duracion'))
            for carrera in facu.getCarreras():
                print('{:<50}{:<20}'.format(carrera.getNombre(), carrera.getDuracion()))
        else: 
            print('no se encontro')

    def mostrarDatosCarrera(self):
        print('Ingresar nombre de la carerra')
        nombre = input('Nombre: ')
        i = 0
        bandera = False
        carreras = None
        while i < len(self.__listaFacultades) and not bandera:
            carreras = self.__listaFacultades[i].getCarreras()
            j = 0
            band=False
            while j < len(carreras) and not band:
                if carreras[j].getNombre() == nombre:
                    print(f'Codigo: {self.__listaFacultades[i].getCodigo()},{carreras[j].getCodigo()}; Facultad: {self.__listaFacultades[i].getNombre()}; Localidad: {self.__listaFacultades[i].getLocalidad()}')
                    bandera = True
                    band = True
                else: j += 1
            i+=1
        