from ClaseCarrera import Carrera
class Facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []

    def __init__(self,codigo,nombre,direccion,localidad,telefono,lista):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono
        self.__carreras=[]
        for carrera in lista:
            self.__carreras.append(Carrera(int(carrera[1]),carrera[2],carrera[3],carrera[4],carrera[5]))
   
    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre
        
    def getCarreras(self):
        return self.__carreras