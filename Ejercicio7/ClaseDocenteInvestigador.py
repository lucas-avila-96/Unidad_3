from ClaseDocente import Docente
from ClaseInvestigador import Investigador


class DocenteInvestigador(Docente, Investigador):
    __categoriaIncetivo = ''
    __importeExtra = 0

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra, area, tipo, categoriaIncetivo, importeExtra):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra)
        self.__categoriaIncetivo = categoriaIncetivo
        self.__importeExtra = importeExtra

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                categoriaIncetivo = self.__categoriaIncetivo,
                importExtra = self.__importeExtra,
            )
        )
        return d

        