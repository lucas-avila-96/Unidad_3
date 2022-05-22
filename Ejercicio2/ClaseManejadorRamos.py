
class ManejadorRamos:
    __ventasRamos = []

    def __init__(self):
        self.__ventasRamos = []

    def agregarVenta(self, unRamo):
        self.__ventasRamos.append(unRamo)
            
    def floresMasVendidas(self):
        diccionario = {}

        for ramo in self.__ventasRamos:
            for flor in ramo.getFlores():
                if not flor.getNombre() in diccionario.keys():
                    diccionario.setdefault(flor.getNombre(), 1)
                else: 
                    diccionario[flor.getNombre()] += 1
        
        for key in diccionario:
            print (f'{key} : {diccionario[key]}')

    def floresVendidasTipo(self, tipo):
        floresVendidas = []
        for ramo in self.__ventasRamos:
            if ramo.getTamano() == tipo:
                for flor in ramo.getFlores():
                    if not flor.getNombre() in floresVendidas:
                        floresVendidas.append(flor)
        
        for flor in floresVendidas:
            print(flor.getNombre())