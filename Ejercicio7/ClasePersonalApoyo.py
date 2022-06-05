from ClasePersonal import Personal


class PersonalApoyo(Personal):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad)
        self.__categoria = categoria

    def getCategoria(self):
        return self.__categoria

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                categoria = self.__categoria
            )
        )
        return d

