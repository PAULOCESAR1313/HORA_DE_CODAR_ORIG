# PROJETO DE GERENCIAMENTO DE NOTAS
# OBJTIVO - Permitir cadastra alunos, inserir notas, calcular média, mostrar se o aluno foi ou não aprovado. Exibir relatorio com os dados dos alunos.

def menu():
    print("======= SISTEMA DE GERENCIAMENTO DE NOTAS ======")
    print("1 - CADASTRAR ALUNOS")
    print("2 - CADASTRA NOTAS")
    print("3 - EXIBIR RELATORIO")
    print("4 - SAIR")
    return input("Escolha uma opção: ")

def cadastrar_alunos(alunos):
    nome = input("Cadastre o nome do aluno: ")

    if nome.strip == "":
        print("O campo não pode ficar vazio!!")
        return
    if nome in alunos:
        print("Aluno já cadastrado!")
        return
    alunos[nome] = []

    print(f"Aluno {nome} cadastrado.")

def inserir_notas(alunos):
    nome = input("Digite o nome do aluno: ")

    if nome not in alunos:
        print("nome não foi encontrado!")
        return
    print(f"Didite as notas do aluno {nome}. A nota de entre 0 e 10! digite fim para encerrar")

    while True:
        nota = input(f"Not {len(alunos[nome]) + 1}: ")

        if nota.lower() == 'fim':
            break

        try:
            nota = float(nota)

            if 0 <= nota <=10:
                alunos[nome].append(nota)
                print(f"A nota {nota} do aluno {nome}, foi inserida com sucesso!")
            else:
                print("Número invalido, a nota deve estar entre 0 e 10!")
        except ValueError:
            print("Entrada inválida! Tente novamente!")

def calcular_media_e_status(notas):
    if not notas:
        return 0, "Não possui notas!"
    
    media = sum(notas) / len(notas)

    if media >= 7:
        status = "APROVADO"
    elif media <= 3:
        status = "REPROVADO"
    else:
        status = "RECUPERAÇÃO"

    #status = "Aprovado" if  media >=7 else "Recuperação"

    return media, status 

def exibir_relatorio(alunos):
    if not alunos:
        print("Não há alunos cadastrados!")
        return
    print("====== RELATÓRIO DOS ALUNOS ======")

    for nome, nota in alunos.items():
        media, status = calcular_media_e_status(nota)
        print(f"Aluno: {nome}")
        print(f"Notas: {nota}")
        print(f"Média: {media}")
        print(f"Status: {status}")
        print(f"=" * 30)

def main():

    alunos = {}

    while True:
        opcao = menu()

        if opcao == '1':
            cadastrar_alunos(alunos)
        elif opcao == '2':
            inserir_notas(alunos)
        elif opcao == '3':
            exibir_relatorio(alunos)
        elif opcao == '4':
            print("SAINDO DO SISTEMA! TENHA UM BOM TRABALHO")
            break
        else:
            print("OPÇÃO INVÁLIDA!")

if __name__ == '__main__':
    main()