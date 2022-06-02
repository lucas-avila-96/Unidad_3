
class Aparato:
    __marca = ''
    __modelo = ''
    __color = ''
    __paisDeFabricacion = ''
    __precio = ''

    def __init__(self, marca, modelo, color, pais, precio):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__paisDeFabricacion = pais
        self.__precio = precio

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo
    
    def getColor(self):
        return self.__color
    
    def getPaisDeFabricacion(self):
        return self.__paisDeFabricacion

    def getPrecioBase(self):
        return self.__precio



