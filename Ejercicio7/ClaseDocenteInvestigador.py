from ClaseDocente import Docente
from ClaseInvestigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoriaIncetivo = ''
    __importeExtra = 0

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo, categoriaIncetivo, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo)
        self.__categoriaIncetivo = categoriaIncetivo
        self.__importeExtra = importeExtra

    def __str__(self):
        cadena = 'Cuil: '+ self.getCuil() +'\n'
        cadena += 'Apellido: '+ self.getApellido() +'\n'
        cadena += 'Nombre: '+ self.getNombre() +'\n'
        cadena += 'Sueldo basico: '+ self.getSueldoBasico() +'\n'
        cadena += 'Antiguedad: '+ self.getAntiguedad() +'\n'
        cadena += 'Carrera: '+ self.getCarrera() +'\n'
        cadena += 'Cargo: '+ self.getCargo() +'\n'
        cadena += 'Area: '+ self.getArea() +'\n'
        cadena += 'Tipo: '+ self.getTipo() +'\n'
        cadena += 'Categoria Incentivo: '+ self.__categoriaIncetivo +'\n'
        cadena += 'Importe Extra: '+ self.__importeExtra +'\n'

        return cadena
        

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                categoriaIncetivo = self.__categoriaIncetivo,
                importExtra = self.__importeExtra,
            )
        )
        return d

    

        