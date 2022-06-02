from ClasePersonal import Personal

class Investigador(Personal):
    __area = ''
    __tipo = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, area, tipo):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad)
        self.__area = area
        self.__tipo = tipo

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                area = self.__area,
                tipo = self.__tipo
            )
        )
        return d