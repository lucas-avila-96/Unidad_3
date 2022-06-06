from ClaseDocente import Docente
from ClaseInvestigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoriaIncetivo = ''
    __importeExtra = 0

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo, categoriaIncetivo, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoriaIncetivo = categoriaIncetivo
        self.__importeExtra = importeExtra

    def getSueldo(self):
        sueldo = self.__sueldoBasico * (self.__antiguedad/100)
        sueldo + self.getSueldo()
        sueldo + self.__importeExtra
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
                carrera = self.getCarrera(), 
                cargo = self.getCargo(), 
                catedra = self.getCatetra(), 
                area = self.getArea(), 
                tipo = self.getTipo(),
                categoriaIncetivo = self.__categoriaIncetivo,
                importeExtra = self.__importeExtra,
            )
        )
        return d

    def __str__(self):
        cadena = 'Cuil: '+ str(self.getCuil()) +'\n'
        cadena += 'Apellido: '+ self.getApellido() +'\n'
        cadena += 'Nombre: '+ self.getNombre() +'\n'
        cadena += 'Sueldo: '+ str(self.getSueldo()) +'\n'
        cadena += 'Antiguedad: '+ str(self.getAntiguedad()) +'\n'
        cadena += 'Carrera: '+ self.getCarrera() +'\n'
        cadena += 'Cargo: '+ self.getCargo() +'\n'
        cadena += 'Area: '+ self.getArea() +'\n'
        cadena += 'Tipo: '+ self.getTipo() +'\n'
        cadena += 'Categoria Incentivo: '+ self.__categoriaIncetivo +'\n'
        cadena += 'Importe Extra: '+ str(self.__importeExtra) +'\n'
        return cadena
        