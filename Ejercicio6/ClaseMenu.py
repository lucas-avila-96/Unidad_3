from ClaseObjectEncoder import ObjectEncoder
from ClaseHeladera import Heladera
from Ejercicio6.ClaseLavarropa import Lavarropa
from Ejercicio6.ClaseTelevisor import Televisor


class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { '1':self.opcion1,
                            '2':self.opcion2,
                            '3':self.opcion3,
                            '4':self.opcion4,
                            '5':self.opcion5,
                            '6':self.opcion6,
                            '7':self.opcion7,
                            }

    def opcion(self,op, listaAparatos):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        if op == '1' or op == '2' or op == '3':
            func(listaAparatos)
        else:
            func()
    
    def opcion1(self, listaAparatos):
        elemento = Heladera('philips', 'mod1', 'blanco', 'arg', '99999', '200L', True, True)
        pos = input('Posicion: ')
        try:
            listaAparatos.insertarElemento(elemento, pos)
        except IndexError:
            print('Error de indice')

    def opcion2(self, listaAparatos):
        elemento = None
        tipo = input('Tipo: ')
        tipo.lower()
        if tipo == type(Heladera).__name__.lower():
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            color = input('Color: ')
            pais = input('Pais: ')
            precio  = input('precio: ')
            capacidad = input('capacidad: ')
            freezer = input('Frezzer: ')
            ciclica = input('ciclica: ')
            elemento = Heladera(marca, modelo, color, pais, precio, capacidad, freezer, ciclica)
        elif tipo == type(Lavarropa).__name__.lower():
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            color = input('Color: ')
            pais = input('Pais: ')
            precio = input('precio: ')
            capacidad = input('Capacidad: ')
            velocidad = input('Velocidad: ')
            cantProgramas = input('Cantidad de programas: ')
            carga = input('Carga: ')
            elemento = Lavarropa(marca, modelo, color, pais, precio, capacidad, velocidad, cantProgramas, carga)
        elif tipo == type(Televisor).__name__.lower():
            marca = input('Marca: ')
            modelo = input('Modelo: ')
            color = input('Color: ')
            pais = input('Pais: ')
            precio = input('precio: ')
            pantalla = input('Pantalla: ')
            pulgadas = input('Pulgadas')
            definicion = input('Definicon: ')
            internet = input('Internet')
            elemento = Televisor(marca, modelo, color, pais, precio, pantalla, pulgadas, definicion, internet)
        listaAparatos.agregarElemento(elemento)
    
    def opcion3(self, listaAparatos):
       print('Ingrese posicion')
       pos = input('Posicion')
       listaAparatos.consultarTipoAparato(pos)

    def opcion4(self, listaAparatos):
        print('Ingrese marca')
        marca = input('Marca: ')
        cant = listaAparatos.calcularCantidadPorMarca(marca)
        print(f'Cantidad de aparatos marca {marca} es {cant}')

    def opcion5(self, listaAparatos):
        l = listaAparatos.obtenerLavarropasCargaSuperior()
        print('Aparatos con carga superior:')
        for ap in l:
            print(f'{ap.getMarca()}')

    def opcion6(self, listaAparatos):
        listaAparatos.mostrarDatos()

    def opcion7(self, listaAparatos):
        jsonF = ObjectEncoder()
        d = listaAparatos.toJSON()
        jsonF.guardarJSONArchivo(d,'aparatoselectronicos.json')
