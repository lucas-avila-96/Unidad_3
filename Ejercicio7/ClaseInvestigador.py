from ClasePersonal import Personal

class Investigador(Personal):
    __area = ''
    __tipo = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__area = area
        self.__tipo = tipo


    def getArea(self):
        return self.__area
    
    def getTipo(self):
        return self.__tipo

    def getSueldo(self):
        sueldo = self.__sueldoBasico * (self.__antiguedad/100)
        return sueldo

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil = self.getCuil(), 
                apellido = self.getApellido(), 
                nombre = self.getNombre(), 
                sueldo = self.getSueldo(), 
                antiguedad = self.getAntiguedad(),
                area = self.__area,
                tipo = self.__tipo,
            )
        )
        return d

    def __str__(self):
        cadena = 'Cuil: '+ str(self.getCuil()) +'\n'
        cadena += 'Apellido: '+ self.getApellido() +'\n'
        cadena += 'Nombre: '+ self.getNombre() +'\n'
        cadena += 'Sueldo: '+ str(self.getSueldo()) +'\n'
        cadena += 'Antiguedad: '+ str(self.getAntiguedad()) +'\n'
        cadena += 'Area: '+ self.getArea() +'\n'
        cadena += 'Tipo: '+ self.getTipo() +'\n'
        return cadena