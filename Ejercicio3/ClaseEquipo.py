from ClaseContrato import Contrato
from datetime import date
class Equipo:
    __nombre = ''
    __ciudad = ''
    __listaContratos = []

    def __init__(self, nombre, ciudad):
        self.__nombre = nombre
        self.__ciudad = ciudad
        self.__listaContratos = []

    def agregarContrato(self, contrato):
        self.__listaContratos.append(contrato)

    def consultarContratos(self):
        if len(self.__listaContratos) >= 1:
            for contrato in self.__listaContratos:
                print(contrato)
        else:
            print('No existen contratos')

    def obtenerImporteTotal(self):
        total = 0
        for contrato in self.__listaContratos:
            total += contrato.getPagoMensual() * contrato.getDiferenciaMeses()
        print(f'Importe total de los contratos{total}')

    def getNombre(self):
        return self.__nombre
        
    def __str__(self):
        return (f'{self.__nombre}')

    def listarContratos(self):
        for contrato in self.__listaContratos:
            fechaActual = date.today()
            fechaFin = contrato.getFechaFin()
            dif = fechaFin - fechaActual
            if int(dif.days / 30) < 6:
                print(contrato)