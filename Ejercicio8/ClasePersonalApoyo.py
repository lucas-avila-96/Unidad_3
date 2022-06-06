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
        cadena += 'Sueldo: '+ str(self.getSueldo()) +'\n'
        cadena += 'Antiguedad: '+ str(self.getAntiguedad()) +'\n'
        cadena += 'Categoria: ' + self.__categoria +'\n'
        return cadena

    def getCategoria(self):
        return self.__categoria

    def getSueldo(self):
        sueldo = self.__sueldoBasico * (self.__antiguedad/100)
        if self.__categoria in range(10):
            sueldo * (10/100)
        else:
            if self.__categoria in range(10, 20):
                sueldo * (20/100)
            else:
                if self.__categoria in range(20, 22):
                    sueldo * (30/100)
        return sueldo

    def toJSON(self):
        d = dict(
            __class__= self.__class__.__name__,
            __atributos__= dict(
                cuil = self.getCuil(), 
                apellido = self.getApellido(), 
                nombre = self.getNombre(), 
                sueldo = self.getSueldo(), 
                antiguedad = self.getAntiguedad(),
                categoria = self.__categoria,
            )
        )
        return d

