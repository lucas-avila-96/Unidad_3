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

