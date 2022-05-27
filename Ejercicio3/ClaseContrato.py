from datetime import date

class Contrato:
    __fechaInicio = None
    __fechaFin = None
    __pagoMensual = 0
    __jugador = None
    __equipo = None

    def __init__(self, fechaInicio, fechaFin, pagoMensual, unJugador, unEquipo):
        self.__fechaInicio = fechaInicio
        self.__fechaFin = fechaFin
        self.__pagoMensual = pagoMensual
        self.__jugador = unJugador
        self.__equipo = unEquipo

    def __str__(self) -> str:
        cadena = 'Fecha de inicio:'+ str(self.__fechaInicio)+'\n'
        cadena += 'Fecha de fin: '+ str(self.__fechaFin) +'\n' 
        cadena += 'Pago mensual: '+ str(self.__pagoMensual)+'\n'
        cadena += str(self.__jugador)+'\n'
        cadena += str(self.__equipo)
        return cadena

    def getFechaFin(self):
        return self.__fechaFin

    def getFechaInicio(self):
        return self.__fechaInicio

    def getEquipo(self):
        return self.__equipo
        
    def getJugador(self):
        return self.__jugador
    
    def getDiferenciaMeses(self):
        difmeses = None
        difdias = self.__fechaFin - self.__fechaInicio
        difmeses = int(difdias.days / 30)
        return difmeses

    def getPagoMensual(self):
        return self.__pagoMensual
