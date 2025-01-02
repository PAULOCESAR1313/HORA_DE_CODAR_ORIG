# FUNÇÃO - São formas de criar código que pode ser reutilizado! Quando temos um código que vai ser usados, varias vezes, em partes diferente do nosso sistema, transformamos ele em uma funão.
# sintaxe é def, em outras liguagem em geral usa-se function.

def saudacao():
    print("Seja bem vindo!")
# OBS - Toda função tem que ser chamada, ou invocado! Se não for chamada, ela não sera execultada!
saudacao()
# As funções tem os parametros que servem para execultar uma mesma função de forma diferente! O parametro dentro da função ele funciona como uma variavel.
def saudacao_personalisada(nome):
    print(f"Olá, {nome}, seja bem vindo!")

saudacao_personalisada("Mateus")
saudacao_personalisada("Paulo")
saudacao_personalisada("Thayanne")

#TRABALHANDO COM MULTIPLOS PARAMETROS - Podemos trabahar com infinitos parametros, e eles tem que ser separado por virgulas.

def apresentar_pessoas(nome, idade, profissão):
    print(f"Dados da pessoa, Nome: {nome}, idade: {idade} anos, profissão: {profissão}")

apresentar_pessoas("Paulo", 47, "Programador")

#comando return - Ele é uma instrução que retorna o valor para o programa! Ele é usado quando eu não quero imprimir o resultado, quero usar o resultado em outro local do meu programa!

def soma(a, b):
    resultado = a + b
    return resultado
soma(5, 5)
x = 10

soma_x = x + soma(5, 5)

print(soma_x)

resultado_soma = soma(1,99)

soma_y = 10 + resultado_soma
print(soma_y)

# O return volta o valor da função para o escopo global

# Criar uma funsão que converta Fahrenheit para Celsius
# Precisamos criar uma função que peque o valor em F e passe pela formula de conversão: (f - 32) * 5/9, reornando o valor para o escopo global, e imprimir o resultado!

def fahrenheit_p_celsius(f):
    return (f - 32) * 5/9
temp_f = 102
temp_c = fahrenheit_p_celsius(temp_f)

print(f"A temperatura {temp_f} F, foi convertido para {temp_c} C")
