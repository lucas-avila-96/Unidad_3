
from ClaseCalefactor import Calefactor

class Gas(Calefactor):
    __matricula = ''
    __calorias = ''

    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    def calcularConsumo(self, costom3, cantidadm3):
        return self.__calorias / 1000 * cantidadm3 * costom3

    def getCalorias(self):
        return self.__calorias

    def getMatricula(self):
        return self.__matricula
    
    def __str__(self) -> str:
        cadena = 'Marca: '+ self.getMarca() +'\n'
        cadena += 'modelo: '+ self.getModelo()+', Matricula: '+self.__matricula +'\n'
        cadena += 'Calorias: ' + self.__calorias
        return cadena
