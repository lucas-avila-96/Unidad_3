from ClaseMenu import Menu
from ClaseManejadorEquipo import ManejadorEquipo
from ClaseManejadorJugador import ManejadorJugador
from ClaseMenejadorContrato import ManejadorContrato

if __name__ == '__main__':
    menu = Menu()
    manejadorEquipo = ManejadorEquipo()
    manejadorJugador = ManejadorJugador()
    manejadorContrato = ManejadorContrato()

    manejadorEquipo.leerArchivo()
    print('ingrese una opcion')
    print('1. Crear un contrato para un jugador en un equipo')
    print('2. Consultar jugadores Contratados')
    print('3. Consultar Contratos')
    print('4. Obtener importe de contratos')
    print('5. Guardar Contratos')
    print('6. Salir')

    opcion = input('\nIngrese una opcion: ')
    while opcion != '6':
        menu.opcion(opcion, manejadorEquipo, manejadorJugador, manejadorContrato)
        opcion = input('\nIngrese una opcion (6 para finalizar): ')
    print('\nSalió del Programa\n')
