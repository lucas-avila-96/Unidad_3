
from ClaseCalefactor import Calefactor

class Electrico(Calefactor):
    __potencia = 0

    def __init__(self, marca, modelo, potencia):
        super().__init__(marca, modelo)
        __potencia = potencia
    