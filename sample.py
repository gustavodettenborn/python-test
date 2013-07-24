# -.- coding: utf-8 -.-
import unittest


class Calculadora():

    def __init__(self):
        pass

    def soma(self, valor1, valor2):
        return valor1 + valor2


class CalculadoraTestCase(unittest.TestCase):

    def test_soma(self):
        valor1 = 1
        valor2 = 1
        assert not valor1 is None
        assert not valor2 is None
