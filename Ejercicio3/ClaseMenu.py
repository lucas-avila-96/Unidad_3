
from ClaseEquipo import Equipo
from ClaseJugador import Jugador
from ClaseContrato import Contrato
from datetime import datetime
class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5
                            }

    def opcion(self,op ,mEquipo, mJugador, mContrato):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3' or op == '4' or op == '5' or op == '6':
            func(mEquipo, mJugador, mContrato)
        else:
            func()
    
    def opcion1(self, mEquipo, mJugador, mContrato):
        unEquipo = mEquipo.buscarEquipoPorId()
        unJugador = Jugador('Pol Fernandez', 123456789, 'bsas', 'arg', '01/05/1993')
        fechaIniciodt = datetime.strptime('23/05/2022', '%d/%m/%Y')
        fechaFindt = datetime.strptime('23/05/2024', '%d/%m/%Y')
        unContrato = Contrato(fechaIniciodt, fechaFindt, 150000, unJugador, unEquipo)

        mJugador.agregarJugador(unJugador)
        mContrato.agregarContrato(unContrato)
        
        unEquipo.agregarContrato(unContrato)
        unJugador.agregarContrato(unContrato)

    def opcion2(self, mEquipo, mJugador, mContrato):
        print('Ingrese el DNI')
        dni = int(input('Dni: '))
        unJugador = mJugador.buscarJugador(dni)
        if unJugador != None:
            unJugador.consultarContratos()
        else: 
            print('No se encontro')

    def opcion3(self, mEquipo, mJugador, mContrato):
        unEquipo = mEquipo.buscarEquipoPorId()
        unEquipo.consultarContratos()
    
    def opcion4(self, mEquipo, mJugador, mContrato):
        unEquipo = mEquipo.buscarEquipoPorNombre()
        unEquipo.obtenerImporteTotal()

    def opcion5(self, mEquipo, mJugador, mContrato):
        mContrato.guardarArchivo()

    