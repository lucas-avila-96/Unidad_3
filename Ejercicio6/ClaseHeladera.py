from ClaseAparato import Aparato

class Lavarropa(Aparato):
    __capacidadLts = 0 
    __freezer = False
    __ciclica = False

    def __init__(self, marca, modelo, color, pais, precio, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLts = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                capacidad =self.__capacidadLts,
                freezer = self.__freezer,
                ciclica = self.__ciclica
            )
        )
        return d