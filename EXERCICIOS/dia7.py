# PTOJETO ADIVINHE O NÚMERO - Para fazer esse projeto vamos importar uma biblioteca chamada de random

import random

print("Bem vindo ao jogo adivinhe o número!")

# precisamos repetir os números até o usuario acertar o número - vamos gerar número entre 1 e 20

while True:
    numero_secreto = random.randint(1, 20)

    print(numero_secreto)

    tentativas_restantes = 5

    print("Pensei em número entre 1 e 20")
    print("Você tem 5 tentativas para adivinha o número!")

    # loop de tentativas ao final das tentativas o loop acaba!
    while tentativas_restantes > 0:
        # vamos pegar o palpite do usuario com o input

        palpite = input("Digite um número entre 1 é 20: ")
        # devemos fazer uma validação da informação vinda do usuario, por que ele pode digitar algo diferente de um número!

        # validação
        if not palpite.isdigit():
            print("Entrada invalida, por vafor digite um número entre 1 e 20!")
            continue
        
        # converter palpite para inteiro
        palpite = int(palpite)

        # validação para ver se o número digitado esta no intervalo estipulado
        if palpite < 1 or palpite > 50:
            print("O número deve esta entre 1 e 20")
            continue
        # descontar as tentativas
        tentativas_restantes -= 1

        # verificar se o palpite esta correto
        if palpite == numero_secreto:
            print(f"Você acertou! Você ainda tinha {tentativas_restantes} tentativas")
            break
        elif palpite < numero_secreto:
            print("O número é maior que esse!")
        else:
            print("O número é menor que esse!")

        print(f"Tentativas restantes: {tentativas_restantes}")
    # while else para quando acabar as tentativas sem acerto!
    else:
        print(f"Você perdeu! O número secreto era {numero_secreto}")


    break