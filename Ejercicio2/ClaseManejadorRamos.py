
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
        
        l = list(diccionario.values())
        l.sort(reverse=True)
        top5 = l[0 : 5]

        for clave, valor in diccionario.items(): 
            if valor in top5:
                print(f'{clave} : {valor}')

    def floresVendidasTipo(self, tipo):
        floresVendidas = []
        for ramo in self.__ventasRamos:
            if ramo.getTamano() == tipo:
                for flor in ramo.getFlores():
                    if not flor.getNombre() in floresVendidas:
                        floresVendidas.append(flor)
        
        for flor in floresVendidas:
            print(flor.getNombre())