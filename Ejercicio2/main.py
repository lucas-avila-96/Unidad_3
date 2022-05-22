from ClaseMenu import Menu
from ClaseManejadorRamos import ManejadorRamos
from ClaseManejadorFlores import ManejadorFlores


if __name__ == '__main__':
    manejadorFlores = ManejadorFlores()
    manejadorRamos = ManejadorRamos()
    manejadorFlores.leerArchivo()
    menu = Menu()

    print('ingrese una opcion')
    print('1. Registrar un ramo vendido')
    print('2. Mostrar el nombre de las 5 flores  más pedidas en un ramo')
    print('3. Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño')
    print('4. Finalizar')
    opcion = input('\nIngrese una opcion: ')
    while opcion != 4:
        menu.opcion(opcion, manejadorFlores, manejadorRamos)
        opcion = input('\nIngrese una opcion (4 para finalizar): ')
    print('\nSalió del Programa\n')