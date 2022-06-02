from Lista import Lista
from ClaseObjectEncoder import ObjectEncoder


if __name__ == '__main__':
    jsonF = ObjectEncoder()
    puntos = Lista()

    diccionario = jsonF.leerJSONArchivo('personal.json')
    personal = jsonF.decodificarDiccionario(diccionario)

    '''
    1-Insertar a agentes a la colección.
    2-Agregar agentes a la colección.
    3-Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.
    4-Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.
    5-Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.
    6-Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.
    7-Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada.    
    8-Almacenar los datos de todos los agentes en el archivo “personal.json”  
    '''