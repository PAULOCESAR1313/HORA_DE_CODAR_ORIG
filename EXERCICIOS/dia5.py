# ESTRUTURA DE REPETIÇÃO

# REPETIR N VEZES 
# ONDE N, A GENTE PODE DEFENIR
# OU N É UMA CONDIÇÃO 

frutas = ["maçã", "banana", "abacaxi", "melandia"]

# FOR INTEM_INDIVIDUAL IN LISTA:
# BLOCO REPETIÇÃO N VEZES

#for fruta in frutas:
 #   print("frutas:", fruta)

  #  for i in range(5):
   #     print("Num:", i)

#print(frutas[0])
#print(frutas[3])

#WHILE

# O WHILE PRECISA TER UM CONTADOR PARA STARTAR A CONTAGEM, E DE UMA CONDIÇÃO PARA NÃO ENTRA EM UM LOOP INFINITO.

#contador = 0
#while contador < 5:
#    print("Num while", contador)
#    contador += 1

# CALCULAR A MULTIPLICAÇAO DE 1 A N
#N = int(input("Digite um número:"))
#multiplic = 0

#for i in range(1, N + 1):
#    resultado = N * i
#    print(resultado)

# INDENTIFICAR NÚMEROS PARES E IMPARES ATÉ 21
pares = 0
impares = 0

for i in range(1, 21):
    if i % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Pares", pares)
print("Impares", impares)