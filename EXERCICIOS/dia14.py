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

# Adicionar tarefas

def adicionar_tarefas(tarefas):
    print("Adicionar uma nova tarefa")
    titulo = input("Titulo: ")
    descricao = input("Descrição")

    tarefa = {
        'id': 1,
        'titulo': titulo,
        'descricao': descricao,
        'status': False
    }

    tarefas.append(tarefa)
    salvar_tarefas(tarefas)
    print("Tarefa inserida com sucesso!")

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
            adicionar_tarefa(tarefas)
        if opcao == '2':
            listar_tarefas(tarefas)

if __name__ == '__main__':
    main()