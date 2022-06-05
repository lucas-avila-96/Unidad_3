import json
from ClasePersonal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    
    def __str__(self):
        cadena = 'Cuil: '+ str(self.getCuil()) +'\n'
        cadena += 'Apellido: '+ self.getApellido() +'\n'
        cadena += 'Nombre: '+ self.getNombre() +'\n'
        cadena += 'Sueldo basico: '+ str(self.getSueldoBasico()) +'\n'
        cadena += 'Antiguedad: '+ str(self.getAntiguedad()) +'\n'
        cadena += 'Carrera: '+ self.getCarrera() +'\n'
        cadena += 'Cargo: '+ self.getCargo() +'\n'
        return cadena

    def getCarrera(self):
        return self.__carrera
    
    def getCargo(self):
        return self.__cargo
    
    def getCatetra(self):
        return self.__catedra

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil = self.getCuil(), 
                apellido = self.getApellido(), 
                nombre = self.getNombre(), 
                sueldoBaisco = self.getSueldoBasico(), 
                antiguedad = self.getAntiguedad(),
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
            )
        )
        return d
