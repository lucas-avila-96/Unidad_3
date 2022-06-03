
from ClaseAparato import Aparato

class Heladera(Aparato):
    __capacidadLts = 0 
    __freezer = False
    __ciclica = False

    def __init__(self, marca, modelo, color, pais, precio, capacidad, freezer, ciclica):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLts = capacidad
        self.__freezer = freezer
        self.__ciclica = ciclica
    
    def getImporteVenta(self):
        importe = int(self.getPrecioBase())
        if self.__freezer is True:
            importe += importe * 5/100
        if self.__freezer == False:
            importe += importe * 1/100
        if self.__ciclica == True:
            importe += importe * 10/100

        return importe

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca = self.getMarca(),
                modelo = self.getModelo(), 
                color = self.getColor(),
                pais = self.getPaisDeFabricacion(),
                precio = self.getImporteVenta(),
                capacidad =self.__capacidadLts,
                freezer = self.__freezer,
                ciclica = self.__ciclica
            )
        )
        return d