#DICIONARIOS - São como objtos em outras linguagens
# Em python - ARRAY [], TUPLA (), DICIONARIOS {}

aluno = {
    "Nome": "Paulo César",
    "Profissao": "Programador",
    "Idade": 47
}

# Estrutura de um dicionario, "chave":"valor" => "Nome": "Paulo César".
# O vaor pode ser número, array, string.

# Podemos acessar uma chave especifica

print(aluno)# Chamando o dicionario completo

print(aluno["Nome"])# Chamando um item especifico do dicionario

print(f"Nome do funcionario: {aluno['Nome']}, função: {aluno['Profissao']}")# Concatenando itens

# Atribuindo valor, e trocando valor

aluno["Nota"] = 15
aluno["Profissao"] = "Engenheiro"

print(aluno)

# Removendo a chave e o valor com o comendo del

del aluno["Profissao"]

print(aluno)

# CINJUNTO OU (SET) - São listas especiais

lista = [1, 2, 2, 2, 3,3, 4, 4,4, 5, 6, 6, 7, 7, 7, 7]
lista_unica = set(lista)

print(lista)
print(lista_unica)

# Adicionando valores no set

lista_unica.add(8) # adicionando um valor novo
lista_unica.add(6) # adicionando um valor existente na lista

print(lista_unica) #OBS: Quando adicionamos um valor que já existe na lista o valor é iguinorado!

# Removendo itens

lista_unica.remove(2)
print(lista_unica)

# Podemos unir os conjuntos

lista_2 = {1, 2,"a", "b",17}

uniao = lista_unica.union(lista_2)

print(uniao)

# Interseção

intersecao = lista_unica.intersection(lista_2)

print(intersecao)

# diferença

difereca = lista_unica.difference(lista_2)

print(difereca)