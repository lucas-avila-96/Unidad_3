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

    def getImporteVenta(self):
        '''
        el 1% si el tipo de definición es SD, 2% si el tipo de definición es HD, 3% si el tipo de definición es FULL HD, mas 10% si tiene conexión a internet.
        '''
        importe = self.getPrecioBase()
        if self.__tipoDedfinicion == 'SD':
            importe += importe * 1/100
        if self.__tipoDedfinicion == 'HD':
            importe += importe * 2/100
        if self.__tipoDedfinicion == 'FULL HD':
            importe += importe * 3/100
        return importe

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca = self.getMarca(),
                modelo = self.getModelo(), 
                color = self.getColor(),
                pais = self.getPaisDeFabricacion(),
                precio = self.getPrecio(),
                pantalla = self.__tipoDePantalla,
                pulgadas = self.__pulgadas,
                definicion = self.__tipoDedfinicion,
                internet = self.__conexionInternet,
            )
        )
        return d