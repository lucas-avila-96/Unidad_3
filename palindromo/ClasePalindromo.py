class Palindromo:
    __palabra = None

    def __init__(self, palabra):
        self.__palabra = palabra

    def esPalindromo(self):
        esPalindromo = False
        l = list(self.__palabra)
        l.reverse()
        strInvertido = "".join(l)
        if self.__palabra == strInvertido:
            esPalindromo = True
        return esPalindromo

    def setPalabra(self, p):
        self.__palabra = p