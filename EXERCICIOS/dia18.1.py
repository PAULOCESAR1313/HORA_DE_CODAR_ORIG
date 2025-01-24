# BIBLIOTECA UNITTEST - Permite que você faça testes unitarios, para prevenção de bugging.

import unittest

def somar(a, b):
    return a + b

class TestSomar(unittest.TestCase):
    def test_somar_positivos(self):
        self.assertEqual(somar(2, 3), 5)
    def test_somar_negativos(self):
        self.assertEqual(somar(-1, -3), -4)
    def test_somar_zero(self):
        self.assertEqual(somar(2, 0), 2)
if __name__ == "__main__":
    print("Iniciando teste de soma....")
    unittest.main()