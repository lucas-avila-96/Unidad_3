
from ClaseCalefactor import Calefactor

class Gas(Calefactor):
    __matricula = ''
    __calorias = ''

    def __init__(self, marca, modelo, matricula, calorias):
        super().__init__(marca, modelo)
        self.__matricula = matricula
        self.__calorias = calorias

    