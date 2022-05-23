import csv

from ClaseJugador import Jugador

class ManejadorJugador:
    __listaJugadores = []

    def __init__(self):
        self.__listaJugadores = []

    def agregarJugador(self, unJugador):
        self.__listaJugadores.append(unJugador)

    def leerArchivo(self):
        archivo = open('Jugadores.csv')
        reader = csv.reader(archivo, delimiter = ';')
        bandera = True
        for fila in reader:
            if bandera:
                bandera = False
            else:
                nombre, dni, ciudad, pais, fechaNac = fila[0], fila[1], fila[2], fila[3], fila[4]
                unJugador = Jugador(nombre, dni, ciudad, pais, fechaNac)
                self.agregarJugador(unJugador)
        archivo.close()