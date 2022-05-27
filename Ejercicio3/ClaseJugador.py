
class Jugador:
    __nombre = ''
    __dni = ''
    __ciudad = ''
    __pais = ''
    __fechaNac = ''
    __listaContratos = []

    def __init__(self, nombre, dni, ciudad, pais, fechaNac):
        self.__nombre = nombre
        self.__dni = dni
        self.__ciudad = ciudad
        self.__pais = pais
        self.__fechaNac = fechaNac
        self.__listaContratos = []

    def __str__(self):
        return (f'{self.__nombre}')
    
    def getDni(self):
        return self.__dni

    def agregarContrato(self, contrato):
        self.__listaContratos.append(contrato)
    
    def consultarContratos(self):
        if len(self.__listaContratos) >= 1:
            for contrato in self.__listaContratos:
                print (str(contrato.getEquipo()))
                print(str(contrato.getFechaFin()))
        else: 
            print('No tiene contratos')
