from ClaseAparato import Aparato

class Lavarropa(Aparato):
    __capacidadLavado = 0
    __velocidadDeCentrifugado = 0
    __cantidadDeProgramas = ''
    __tipoDeCarga = ''


    def __init__(self, marca, modelo, color, pais, precio, capacidad, velocidad, cantProgramas, carga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLavado = capacidad
        self.__velocidadDeCentrifugado = velocidad
        self.__cantidadDeProgramas = cantProgramas
        self.__tipoDeCarga = carga

