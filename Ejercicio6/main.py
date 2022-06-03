from ClaseLista import Lista
from ClaseObjectEncoder import ObjectEncoder
from ClaseMenu import Menu
from ClaseHeladera import Heladera


if __name__ == '__main__':
    menu = Menu()
    listaAparatos = Lista()

    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('Ejercicio6\Aparatoselectronicos.json')
    listaAparatos = jsonF.decodificarDiccionario(diccionario)

    print('Seleccione una opcion')
    print('1. Insertar un aparato en la colección en una posición determinada.')
    print('2. Agregar un aparato a la colección (solicitar el tipo de aparato, y luego los datos que correspondan).')
    print('3. Dada una posición de la Lista: Mostrar por pantalla qué tipo de objeto se encuentra almacenado en dicha posición.')
    print('4. Mostrar la cantidad de heladeras, lavarropas y televisores cuya marca sea phillips.')

    print('5. Mostrar la marca de todos los lavarropas que tienen carga superior .')
    print('6. Mostrar para todos los aparatos que la empresa tiene a la venta, marca, país de fabricación e importe de venta.')
    print('7. Almacenar los objetos de la colección Lista en el archivo “aparatoselectronicos.json”.')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '8':
        menu.opcion(opcion, listaAparatos)
        opcion = input('\nIngrese una opcion (8 para finalizar): ')
    print('\nSalió del Programa\n')
