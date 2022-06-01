from Lista import Lista
from ClaseObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    puntos = Lista()

    diccionario = jsonF.leerJSONArchivo('personal.json')
    personal = jsonF.decodificarDiccionario(diccionario)