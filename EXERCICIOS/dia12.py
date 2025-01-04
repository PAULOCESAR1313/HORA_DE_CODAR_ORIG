#TRATAMENTO DE ERROS E EXCEÇÕES - Precisamos criar programas aprova de falhas, mas não podemos garantir isso só com uma boa logica, e uma boa sintax.
# A maioria dos erros, vão ser calsados pelo usuario, por causa disto devemos prever possiveis erros, e tratalos, para isso vamos usar na maioria das vezes o blocos try, except, else, finally.
# Como um exeplo vamos tentar ler um arquivo que não existe.

#arquivo = open("dados.txt", "r")# Comando basico para leitura de arquivo em python
#conteudo = arquivo.read() # Comando basico, para chamar o arquivo que vai ser lido.
# Para tratarmos esse erro, famos usar o bloco try e o finally.

#try:
    #arquivo = open("dados.txt", "r")# Não é possivel usar somente o bloco try, precisamos usar o except e
    #conteudo = arquivo.read()# finally, para compor o comando. O except permite que escrevemos uma 
#except FileNotFoundError:#mensagem de erro; o finally permite que o progra rode apesar do erro.
    #print("Erro: O arquivo não existe")
#finally:
    #print("Operação finalizada")

#Agora vamos ver uma situação onde o arquivo existe e é lido.

try:
    arquivo = open("dados.txt", "r")
    conteudo = arquivo.read()
except FileNotFoundError:
    print("Erro: O arquivo não existe!")
else:
    print("Arquivo lido!")
    print(conteudo)
finally:
    print("Operação finalizada!")
bloco = "-" * 10, "BLOCO_2", "-" *10
print(bloco)

try:
    numero = int(input("Digite um número: "))
    resultado = 100 / numero
except ValueError:
    print("Entrada invalida! Tente novamente!")
except ZeroDivisionError:
    print("Entrada Invalida, divisão por 0!")
else:
    print(f"O resultado de 100 dividido por {numero} é: {resultado}")
finally:
    print("Operação concluida!")
