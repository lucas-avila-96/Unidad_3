



class Personal:
    __cuil = ''
    __apellido = ''
    __nombre = ''
    __sueldoBasico = ''
    __antiguedad = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad):
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBaisco
        self.__antiguedad = antiguedad

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil = self.__cuil,
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldoBasico = self.__sueldoBasico,
                antiguiedad = self.__antiguedad,
            )
        )
        return d