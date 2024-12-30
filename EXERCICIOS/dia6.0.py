# LISTAS (ARRAY) TUPLAS
# INTERLIGADO COM OS LOOPS - ESTRUTURAS DE REPETIÇÃO

carros = ["BMW", "FIAT", "FORD"]

# acessando os itens atraves dos indices - Os indices sempre começam em 0
print("Nossos carros:", carros)
print(carros[0])
print(carros[2])
print(len(carros))
# Para acrecentar um item na lista usamos o método append
carros.append("FERRARI")
print("Nossos carros:", carros)
print(carros)
print(carros[3])
print(len(carros))
# Removendo intem usanso o método remove
carros.remove("FIAT")
print("Nossos carros:", carros)
print(carros)
print(len(carros))