# TRABALHANDO COM ARQUIVOS EM PYTHON

# Lendo um arquivo completo com python

with open('dados.txt', 'r') as arquivo:
    conteudo = arquivo.read()
    print(conteudo)

divisao = "-" * 50, "BLOCO_2", "-" * 50
print(divisao)

#Lendo o arquivo linha a linha
with open('dados.txt', 'r') as arquivo:
    for linha in arquivo:
        print(linha)
        break

# Escrevendo em um arquivo
with open('saida.txt', 'w') as arquivo:
    arquivo.write("linha \n")
    arquivo.write("linha 2 \n")
# Quando o arquivo não existe o python cria para você!
# Ultilizamos a contra bara, n, é para saltar uma linha.

divisao = "-" * 50, "BLOCO_3", "-" * 50
print(divisao)

with open('saida.txt', 'a') as arquivo:
    arquivo.write("linha 3 \n")
    arquivo.write("linha 4 \n")
print("Deu certo você adicionou mais duas linhas!")

# r = read - Ler os arquivos;
# w = write - Escrever o arquivo;
# a= append - Adicionar invormação.

divisao = "-" * 50, "BLOCO_4", "-" * 50
print(divisao)

# CSV - significa, comma separeted values

import csv

with open("contatos.csv", "w", newline= '') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)# cabeçalho
    escritor.writerow(['Nome', 'Profissão', 'Idade'])# colunas
    escritor.writerow(["Paulo", "Programador", 47])# dados
    escritor.writerow(["Thayanne", "Catadora", 23])# dados
    escritor.writerow(["Joaquim", "Estudante", 5])# dados

divisao = "-" * 50, "BLOCO_4", "-" * 50
print(divisao)
#JSON - Significado: Javascript object notation (API), Serve para comunicação entre sistemas

import json

dados = {
    "Nome": "Paulo",
    "Profissao": "Programador",
    "Idade": 47
}

# Adicionando o arquivo JSON

with open('dados.Json', 'w') as arquivo:
    json.dump(dados, arquivo, indent=4)