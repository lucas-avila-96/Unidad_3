from Ejercicio3.ClaseMenu import Menu
from ManejaFacultades import ManejaFacultades


if __name__ == '__main__':
    manejador = ManejaFacultades()
    manejador.testFacultades()
    print('mostrar datos de cada una de las carreras que se dictan en una facultad.')
    print('mostrar datos de una facultad')
    op = input('Ingrese una opcion')
    menu = Menu()
    menu.opcion(op, manejador)