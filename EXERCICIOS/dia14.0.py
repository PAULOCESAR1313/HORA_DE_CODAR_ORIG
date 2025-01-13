# GERENCIADOR DE TAREFAS

import os
import json

# Função para carregar tarefas

def carregar_tarefas():
    if os.path.exists('tarefas.json'):
        with open('tarefas.json','r') as arquivo:
            return json.load(arquivo)
    return []

# Listar tarefas
def listar_tarefas(tarefas):
    print("Tarefas:")
    for tarefa in tarefas:
        status = "Concluida" if tarefa['concluida'] else "Pendente"
        print(f"ID: {tarefa['id']}, Titulo: {tarefa['titulo']}, Status: {status}")

# Escreve no arquivo e salvar tarefa

def salvar_tarefas(tarefas):
    with open('tarefas.json','w') as arquivo:
            json.dump(tarefas, arquivo, indent=4)

#Gerar ID

def gerar_id(tarefas):
    if tarefas:
        return tarefas[-1]['id'] + 1 # Vai pegar o ultima id e vai somar um no id para nova tarefa.

# Adicionar tarefas

def adicionar_tarefas(tarefas):
    print("Adicionar uma nova tarefa")
    titulo = input("Titulo: ")
    descricao = input("Descrição")

    tarefa = {
        'id': gerar_id(tarefas),
        'titulo': titulo,
        'descricao': descricao,
        'status': False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

# Concluir tarefa

def concluir_tarefa(tarefas):
    try:
        id_tarefa = int(input("Digite o ID da tarefa para concluir: "))
        for tarefa in tarefas:
            if tarefa['id'] == id_tarefa:
                if tarefa['status']:
                    print("A tarefa já está concluida!")
                else:
                    tarefa['status'] = True
                    salvar_tarefas(tarefas)
                    print("Tarefa concluida com sucesso!!")
                return           
        print("Tarefa não encontrada!!")
    except ValueError:
        print("ID Invalido! Tente novamente!")        

# Menu principal

def menu():
    print("==== GERENCIADOR DE TAREFAS ====")
    print("1. Adicionar tarefas")
    print("2. Listar tarefas")
    print("3. Concluir tarefas")
    print("4. Remover tarefas")
    print("5. Sair")
    return input("Escolha uma opção: ")

# Loop das ações do sistema
def main():
    tarefas = carregar_tarefas()
    while True:
        opcao = menu()

        if opcao == '1':
            adicionar_tarefas(tarefas)
        elif opcao == '2':
            listar_tarefas(tarefas)
        elif opcao == '3':
            concluir_tarefa(tarefas)
        #elif opcao == '4':
            #excluir_tarefas(tarefas)
        elif opcao == '5':
            print("Encerrando o programa!")
            break
        else:
            print("Opição Invalida!")

if __name__ == '__main__':
    main()