
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

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca = self.__marca,
                modelo = self.__modelo,
                color = self.__color,
                pais = self.__paisDeFabricacion,
                precio = self.__precio,
            )
        )
        return d





