
class Personal:
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldoBasico = ''
    __antiguedad = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera = '', cargo  = '', catedra = '', area = '', tipo = ''):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBaisco
        self.__antiguedad = antiguedad

    def getApellido(self):
        return self.__apellido
    
    def getCuil(self):
        return self.__cuil
    
    def getNombre(self):
        return self.__nombre
    
    def getSueldoBasico(self):
        return self.__sueldoBasico

    def getAntiguedad(self):
        return self.__antiguedad

    