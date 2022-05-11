class Facultad:
    __codigo = 0
    __nombre = ''
    __direccion = ''
    __localidad = ''
    __telefono = ''
    __carreras = []

    def __init__(self, codigo, nombre, direccion, localidad, telefono, listaCarreras):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__direccion = direccion
        self.__localidad = localidad
        self.__telefono = telefono

        for fila in listaCarreras:
            codigo, nombre, duracion, tipo = fila[0], fila[1], fila[2], fila[3]
            self.__carreras.append(codigo, nombre, duracion, tipo)

    def getCodigo(self):
        return self.__codigo

    def getNombre(self):
        return self.__nombre
        
    def getCarreras(self):
        return self.__carreras