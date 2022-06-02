import unittest

from ClasePalindromo import Palindromo

class TestPalindromo(unittest.TestCase):
    __palindromo = None
    def setUp(self):
        self.__palindromo = Palindromo('ANA')

    def test_esPalindromoPar(self):
        self.assertTrue(self.__palindromo.esPalindromo())

    def test_unNoPalindromo(self):
        self.assertFalse(self.__palindromo.esPalindromo())

    def test_esPalindromoImpar(self):
        self.assertTrue(self.__palindromo.esPalindromo())

