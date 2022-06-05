from ClaseLista import Lista
from ClaseMenu import Menu
from ClaseObjectEncoder import ObjectEncoder
from ClaseDocenteInvestigador import DocenteInvestigador

if __name__ == '__main__':
    '''
    print('MRO de la clase Ayudante: ', DocenteInvestigador.mro())
    di = DocenteInvestigador(41223444, 'Juarez', 'Roberto',150000, 5, 'LCC', 'Profesor','POO', 'area', 'tipo', 'incentivo', 20000)
    print(di)
    '''
    jsonF = ObjectEncoder()
    menu = Menu()
    diccionario = jsonF.leerJSONArchivo('personal.json')
    listaAgentes = jsonF.decodificarDiccionario(diccionario)
    op = input('Opcion')
    print('1-Insertar a agentes a la colección.')
    print(' 2-Agregar agentes a la colección.')
    print(' 3-Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.')
    print('4-Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.')
    print('5-Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.')
    print('6-Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.')
    print('7-Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada. ')   
    print('  8-Almacenar los datos de todos los agentes en el archivo “personal.json”')
    menu.opcion(op, listaAgentes)