
class Contrato:
    __fechaInicio = ''
    __fechaFin = ''
    __pagoMensual = 0.0
    __jugador = None
    __equipo = None

    def __init__(self, fechaInicio, fechaFin, pagoMensual, unJugador, unEquipo):
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual
        self.__jugador = unJugador
        self.__equipo = unEquipo

    def __str__(self) -> str:
        cadena = 'Fecha de inicio:'+ self.__fechaInicio+'\n'
        cadena += 'Fecha de fin: '+ self.__fechaFin +'\n' 
        cadena += 'Pago mensual: '+ str(self.__pagoMensual)+'\n'
        cadena += str(self.__jugador)+'\n'
        cadena += str(self.__equipo)
        return cadena

    def getFechaFin(self):
        return self.__fechaFin

    def getEquipo(self):
        return self.__equipo
