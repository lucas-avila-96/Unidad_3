from unicodedata import numeric


class Flores:
    __numero = 0
    __nombre = ''
    __color = ''
    __descripcion = ''

    def __init__(self, numero, nombre, color, descripcion):
        self.__numero = numero
        self.__nombre = nombre
        self.__color = color
        self.__descripcion = descripcion