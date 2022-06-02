from ClaseManejadorCalefactor import ManejadorCalefactor
from ClaseMenu import Menu
from ClaseCalefactor import Calefactor


if __name__ == '__main__':
    
    print('Ingrese cantidad de calefactores')
    dimension = int(input('Cantidad'))
    manejadorCalefactor = ManejadorCalefactor(dimension)
    manejadorCalefactor.leerArchivo()
    menu = Menu()

    print('ingrese una opcion')
    print('1. Mostrar marca y modelo del calefactor a gas natural de menor costo de consumo')
    print('2. Mostrar  marca  y modelo del calefactor eléctrico de menor consumo.')
    print('3. Mostrar tipo de calefactor y todos los datos del calefactor de menor consumo.')
    print('4. Finalizar')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '4':
        menu.opcion(opcion, manejadorCalefactor)
        opcion = input('\nIngrese una opcion (4 para finalizar): ')
    print('\nSalió del Programa\n')
