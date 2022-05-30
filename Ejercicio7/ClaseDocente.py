
import json
from ClasePersonal import Personal


class Docente(Personal):
    __carrera = ''
    __cargo = ''
    __catedra = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, carrera, cargo, catedra):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                carrera = self.__carrera,
                cargo = self.__cargo,
                catedra = self.__catedra,
            )
        )
        return d
