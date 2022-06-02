
from ClaseCalefactor import Calefactor

class Electrico(Calefactor):
    __potencia = 0

    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        __potencia = potencia

    def calcularConsumo(self, costokw, cantidadh):
        return self.__potencia / 1000 * cantidadh * costokw

    def getPontencia(self):
        return self.__potencia

    def __str__(self):
        cadena = 'Marca: '+ self.getMarca() +'\n'
        cadena += 'modelo: '+ self.getModelo()+', Potencia: '+self.__potencia +'\n'
        return cadena
