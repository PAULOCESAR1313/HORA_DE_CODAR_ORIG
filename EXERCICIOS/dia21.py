# DESAFIO 01 - Calcular o fatorial de um número digitado pelo usuario do sisema, fazer validação.
# Enunciado:
    # Criar uma função que calcule o fatorial de um número não negativo fornecido pelo usuario
    # Valide o número para garantir que o mesmo não seja negativo.
    # Se o usuario fornecer um número invalido, peça para ele fornecer outro.
    # O fatorial deve ser calculado por um loop.

def calcular_fatorial():
    while True:
        try:
            numero = int(input("Digite um número inteiro não negativo para o calculo de fatorial: "))
            if numero < 0:
                print("Número negativo!")
                continue
            break
        except ValueError:
            print("Número inválido! Tente novamente!")
    fatorial = 1

    for i in range(1, numero + 1):
        fatorial *= i
    
    print(f"O fatorial de {numero} é {fatorial}")

calcular_fatorial()

# DESAFIO 02 - Contador de palavras em um texto.
# Enunciado:
    # Criar uma função que receba um texto de entrada e retorne o número de palavras contida nele
    # Consifere palavras o conjunto de caractere separado por espaço.
    # Equinore espaços extras no inicio e no final do texto.

def contador_de_palavras(texto):
    palavras = texto.strip().split()
    return len(palavras)

texto_usuario = input("Digite um texto; ")

quantidade = contador_de_palavras(texto_usuario)

print("========== TEXTO DO USUARIO ==========")
print(f"{texto_usuario}")
print("========== FIM DO TEXTO ==========")
print(f"O seu texto tem {quantidade} de palavras")