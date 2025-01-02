# MANIPULANDO STRINGS - As strings são as palavras, o testo, são declaradas entre aspas, duplas ou simples dependendo da linguagem.
# Podemos concatenar as strings o exemplo mais comum é a concatenação do primeiro nome com o segundo nome:

primeiro_nome = "Paulo César"
segundo_nome = "Pereira da Silva"

print(primeiro_nome + " " + segundo_nome)

# Encapsulando em uma variavel

nome_completo = primeiro_nome +" "+ segundo_nome
print(f"Olá, {nome_completo}")

# Podemos repetir strings usanso a multiplicação
decoracao = "-" * 50
print(decoracao)
# criando menu simples
print(decoracao + " Menu " + decoracao)

# Indexação - pegamos uma palavra qualquer, e associamos um indice para cada letra
texto = "Python"
print(texto[3])

# Fatiamento ou slicing - pega parte de uma frase, o fatiamento começa da letra indicada no indice e vai até a letra - 1 do indice final
frase = "Eu amo programar"
print(frase[7:]) 
print(frase[0:16])
# Podemos ainda, calcular o tamanho de uma string com o comando length
print(len(frase))
# Podemos altera o tamanho ou a case das strings, colocando tudo em caixa alta, ou caixa baixa ou alternando emtra as palavras.

texto2 = "Sou programador!"
print(texto2.upper()) # CAIXA ALTA
print(texto2.lower()) # caixa baixa
print(texto2.title()) # Caixa Alta No Inicio De Cada Palavra

# Podemos limpar espaços desnecessarios entre palavras

msg_com_espacos = "   Paulo César Pereira da Silva  "
print(msg_com_espacos)
print(msg_com_espacos.strip())

# Substituindo palavras

frase3 = "Eu gosto de Java"
nova_frase = frase3.replace("Java", "Javascript")

print(nova_frase)