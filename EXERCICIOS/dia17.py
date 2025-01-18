#ALGORITIMOS CRIADOS PARA RESOLVER PROBLEMAS COMPLEXOS.
#RECURSÃO - É QUANDO UMA FUNÇÃO CHAMA ELA MESMA PARA RESOLVER UM PROBLEMA

#RECURSÃO:
def contar_recrecivamente(n):
    if n <= 0:
        print("final!")
    else:
        print(n)
        contar_recrecivamente(n -1) #RECURSÃO é igual a um loop, só que feito com funçõe
    
contar_recrecivamente(10)

def fatorial(n):
    if n == 0:
        return 1
    else:
        return n * fatorial(n - 1)
    
print(fatorial(5))

# Fibonacci e estrutura de dados e algoritmos - Geralmente são assuntos em entravistas de emprego

# PESQUISA BINARIA RECURSIVA - Outro algoritmo muito usado em problemas complexos. Basicamente temos uma lista de números, e devemo encontrar um número especifico.
# A pesquisa binaria divide a lista em duas listas menores e pesquisa nas duas listas.

# O inicio é onde quero começar minha busca - inicio (indice)
# O final é até onde vou procura o meu alvo. E se eu não definir nada o começo é o fim da lista, e o fim é o começo.

def pesquisa_binaria(lista, alvo, inicio = 0, fim = None):
    if fim is None:
        fim = len(lista) -1 # Isso me dar o indice do elemento final

    if inicio > fim:
        return -1
    
    meio = (inicio + fim) // 2

    if list[meio] == alvo:
        return meio
    elif lista[meio] < alvo:
        return pesquisa_binaria(lista, alvo, meio + 1, fim) # Pesquisa o lado direito da lista dividida
    else:
        return pesquisa_binaria(lista, alvo, inicio, fim - 1) # Pesquisa o lado esqerdo da lista dividida
    
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

print(f"O indice do elemento 10 é: {pesquisa_binaria(lista, 10)}")
print(f"O indice do elemento 15 é: {pesquisa_binaria(lista, 15)}")