
class ManejadorJugador:
    __listaJugadores = []

    def __init__(self):
        self.__listaJugadores = []

    def agregarJugador(self, unJugador):
        self.__listaJugadores.append(unJugador)

    def buscarJugador(self, dni):
        unJugador = None
        band = False
        i = 0
        while i < len(self.__listaJugadores) and not band:
            if self.__listaJugadores[i].getDni() == dni:
                unJugador = self.__listaJugadores[i]
                band = True
        return unJugador

        