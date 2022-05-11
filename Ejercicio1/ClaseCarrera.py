
class Carrera:
    __codigo = 0
    __nombre = ''
    __duracion = ''
    __titulo = ''
    __tipo = ''

    def __init__(self, codigo, nombre, duracion, titulo, tipo):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__duracion = duracion
        self.__titulo = titulo
        self.__tipo = tipo

    def getNombre(self):
        return self.__nombre

    def getDuracion(self):
        return self.__duracion
        