from ClaseAparato import Aparato

class Televisor(Aparato):
    __tipoDePantalla = '' 
    __pulgadas = '' 
    __tipoDedfinicion = ''
    __conexionInternet = False

    def __init__(self, marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipoDePantalla =  pantalla
        self.__pulgadas = pulgadas
        self.__tipoDedfinicion = definicion
        self.__conexionInternet = internet

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                pantalla = self.__tipoDePantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__tipoDedfinicion,
                internet = self.__conexionInternet,
            )
        )
        return d