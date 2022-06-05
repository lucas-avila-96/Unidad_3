from ClasePersonal import Personal


class PersonalApoyo(Personal):
    __categoria = ''

    def __init__(self, cuil, apellido, nombre, sueldoBaisco, antiguedad, categoria):
        super().__init__(cuil, apellido, nombre, sueldoBaisco, antiguedad)
        self.__categoria = categoria
    
    def __str__(self):
        cadena = 'Cuil: '+ str(self.getCuil()) +'\n'
        cadena += 'Apellido: '+ self.getApellido() +'\n'
        cadena += 'Nombre: '+ self.getNombre() +'\n'
        cadena += 'Sueldo basico: '+ str(self.getSueldoBasico()) +'\n'
        cadena += 'Antiguedad: '+ str(self.getAntiguedad()) +'\n'
        cadena += 'Categoria: ' + self.__categoria +'\n'
        return cadena

    def getCategoria(self):
        return self.__categoria

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil = self.getCuil(), 
                apellido = self.getApellido(), 
                nombre = self.getNombre(), 
                sueldoBaisco = self.getSueldoBasico(), 
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria,
            )
        )
        return d

