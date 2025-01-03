# EXERCICIOS
# Crie uma função que atribua uma nota para prova A de um aluno

def adicionar_nota(aluno):
    aluno["prova_A"] = int(input("Digite a nota da prova A: "))

aluno_teste = {
    "Nome": "Joaquim"
}

adicionar_nota(aluno_teste)

print(aluno_teste)

# Verificar palavras unicas de uma frase usando o set

frase = input("Digite uma frase!")

palavras = frase.split()

print(palavras)

palavras_unicas = set(palavras)

print(palavras_unicas)