
class Jugador:
    __nombre = ''
    __dni = ''
    __ciudad = ''
    __pais = ''
    __fechaNac = ''

    def __init__(self, nombre, dni, ciudad, pais, fechaNac):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad = ciudad
        self.__pais = pais
        self.__fechaNac = fechaNac
