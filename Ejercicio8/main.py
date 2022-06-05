from ClaseLista import Lista
from ClaseMenu import Menu
from ClaseObjectEncoder import ObjectEncoder
from IDirector import IDirector
from ITesorero import ITesorero

def director(listaAgentes: IDirector):
    print('1-Modificar el sueldo básico de todos los agentes')
    print('2-Moficar el porcentaje que se paga por cargo a un docente')
    print('3-Modificar el porcentaje que se paga por categoría a un personal de apoyo')
    print('4-Modificar  el porcentaje extra que se paga a un docente investigador')
    print('5-Salir')
    opcion=int(input('Seleccione un número del 1 al 5: '))
    while opcion in [1,2,3,4]:
        dni = int(input('Dni: '))
        if opcion == 1:
            nuevoBasico = input('Nuevo basico: ')
            listaAgentes.modificarBasico(dni, nuevoBasico)
        if opcion == 2:
            nuevoPorcentaje = input('Nuevo porcentaje: ')
            listaAgentes.modificarPorcentajeporcargo(dni, nuevoPorcentaje)
        if opcion == 3:
            nuevoPorcentaje = input('Nuevo porcentaje: ')
            listaAgentes.modificarPorcentajeporcategoria(dni, nuevoPorcentaje)
        if opcion == 4:
            nuevoImporteExtra = input('Nuevo importe extra: ')
            listaAgentes.modificarImporteExtra(dni, nuevoImporteExtra)

def tesorero(listaAgentes: ITesorero):
    dni = int(input('Dni: '))
    listaAgentes.gastosSueldoPorEmpleado(dni)
        
def autenticarUsuario(listaAgentes):
    usuario=input('Usuario (Director/Tesorero): ')
    clave = input('Clave:')
    if usuario.lower() == 'uTesoreso'.lower() and clave =='ag@74ck':
        tesorero(ITesorero(listaAgentes))
    else:
        if usuario.lower() == 'uDirector'.lower() and clave == 'ufC77#!1':
            director(IDirector(listaAgentes))

if __name__ == '__main__':
    '''
    print('MRO de la clase Docente investigador: ', DocenteInvestigador.mro())
    di = DocenteInvestigador(41223444, 'Juarez', 'Roberto',150000, 5, 'LCC', 'Profesor','POO', 'area', 'tipo', 'incentivo', 20000)
    print(di)
    '''
    menu = Menu()
    jsonF = ObjectEncoder()
    diccionario = jsonF.leerJSONArchivo('Ejercicio8\Personal.json')
    listaAgentes = jsonF.decodificarDiccionario(diccionario)
    print('0-Inicia sesion')
    print('1-Insertar a agentes a la colección.')
    print('2-Agregar agentes a la colección.')
    print('3-Dada una posición de la lista: Mostrar por pantalla que tipo de agente se encuentra almacenado en dicha posición.')
    print('4-Ingresar por teclado el nombre de una carrera y generar un listado ordenado por nombre con todos los datos de los agentes que se desempeñan como docentes investigadores.')
    print('5-Dada un área de investigación, contar la cantidad de agentes que son docente    investigador, y la cantidad de investigadores que trabajen en ese área.')
    print('6-Recorrer la colección y generar un listado que muestre nombre y apellido, tipo de Agente y sueldo de todos los agentes, ordenado por apellido.')
    print('7-Dada una categoría de investigación (I, II, III, IV o V), leída desde teclado, listar apellido, nombre e importe extra por docencia e investigación, de todos los docentes investigadores que poseen esa categoría, al final del listado deberá mostrar el total de dinero que la Secretaría de Investigación debe solicitar al Ministerio en concepto de importe extra que cobran los docentes investigadores de la categoría solicitada. ')   
    print('8-Almacenar los datos de todos los agentes en el archivo “personal.json”')
    opcion = input('\nIngrese una opcion: ')
    while opcion != '9':
        if opcion == '0':
            autenticarUsuario(listaAgentes)
        else:
            if opcion in [1,2,3,4,5,6,7,8]:
                menu.opcion(opcion, listaAgentes)
        opcion = input('\nIngrese una opcion (9 para finalizar): ')
    print('\nSalió del Programa\n')