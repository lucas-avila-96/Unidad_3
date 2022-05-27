from ClaseAparato import Aparato

class Televisor(Aparato):
    __tipoDePantalla = '' 
    __pulgadas = '' 
    __tipoDedfinición = ''
    __conexionInternet = False


    def __init__(self, marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, internet):
        super().__init__(marca, modelo, color, pais, precio)
        self.__tipoDePantalla =  pantalla
        self.__pulgadas = pulgadas
        self.__tipoDedfinición = definicion
        self.__conexionInternet = internet

    