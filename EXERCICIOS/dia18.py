#DEBUGGING - Debuggingar é encontrar erros no código, ou entender como o seu código esta funcionando
# Print - É uma forma de debungging. Não é considerado a melhor forma, mas é rapida, ao colocar o comando print, no caso de algum erro no código uma mensage vai aparecer e apontar o erro.

#def dividir(a, b):
    #print(f"Quanto é {a} dividido por {b}?")
    #if b == 0:
        #print("ERRO: Dividir por zero")
        #return None
    
    #resultado = a / b
    #print(f"O resultado de {a} / {b} é: {resultado}")
    #return resultado
#dividir(0 ,5)
#dividir(10, 0)

# BIBLIOTECA - PDB, PYTHON DEBUGGING é uma forma mais profissional de se trabalhar com bugging.
# Nessa biblioteca a teclas especificas para operação de debuggingar, uma delas é a letra n que vai permitrir percorrer o seu código linha a linha ater encontrar o erro.

print("Usando a biblioteca PYTHON DEBUGGING - PDB")

import pdb

def dividr(a, b):
    #pdb.set_trace()

    if b == 0:
        return None
    
    resultado = a / b

    return resultado

dividr(0 ,5)
dividr(10, 0)

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
        self.assertEqual(somar(2, 3), 5)
if __name__ == "_main_":
    print("Iniciando teste de soma....")
    unittest.main()