class Ramo:
    __tamano = ''
    __flores = []
    def __init__(self, tamano):
        self.__tamano = tamano
        self.__flores = []

    def agregarFlor(self, unaFlor):
        self.__flores.append(unaFlor)

    def getFlores(self):
        return self.__flores

    def getTamano(self):
        return self.__tamano