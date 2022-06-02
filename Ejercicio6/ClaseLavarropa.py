from ClaseAparato import Aparato

class Lavarropa(Aparato):
    __capacidadLavado = 0
    __velocidadCentrifugado = 0
    __cantidadProgramas = ''
    __tipoCarga = ''


    def __init__(self, marca, modelo, color, pais, precio, capacidad, velocidad, cantProgramas, carga):
        super().__init__(marca, modelo, color, pais, precio)
        self.__capacidadLavado = capacidad
        self.__velocidadCentrifugado = velocidad
        self.__cantidadProgramas = cantProgramas
        self.__tipoCarga = carga


    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                marca = self.getMarca(),
                modelo = self.getModelo(), 
                color = self.getColor(),
                pais = self.getPaisDeFabricacion(),
                precio = self.getPrecio(),
                capacidadLavado = self.__capacidadLavado,
                velocidadCentrifugador = self.__velocidadCentrifugado,
                cantidadProgramas = self.__cantidadProgramas,
                tipoCarga = self.__tipoCarga,
            )
        )
        return d