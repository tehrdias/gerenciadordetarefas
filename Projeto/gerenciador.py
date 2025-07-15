def adicionar_tarefa(nome_tarefa, tarefas):
    tarefas.append({'tarefa': nome_tarefa, 'completa': False})
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")
    return

def ver_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, start=1):
        status = "Completa" if tarefa['completa'] else "Pendente"
        print(f"{i}. {tarefa['tarefa']} - {status}")
def atualizar_tarefa(indice, nome_nova_tarefa, tarefas):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['tarefa'] = nome_nova_tarefa
        print(f"Tarefa {indice + 1} atualizada para '{nome_nova_tarefa}'")
    else:
        print("Índice inválido.")
def completar_tarefa(indice, tarefas):
    if 0 <= indice < len(tarefas):
        tarefas[indice]['completa'] = True
        print(f"Tarefa {indice + 1} marcada como completa.")
    else:
        print("Índice inválido.")
def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa['completa']]
    print("Tarefas completadas deletadas com sucesso!")




tarefas = []
while True:
    print("\nMenu Gerenciador de Lista de tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Atualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(nome_tarefa, tarefas)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        indice = int(input("Digite o índice da tarefa a ser atualizada: ")) - 1
        nome_nova_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(indice, nome_nova_tarefa, tarefas)
    elif escolha == "4":
        indice = int(input("Digite o índice da tarefa a ser completada: ")) - 1
        completar_tarefa(indice, tarefas)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
    elif escolha == "6":
        break

print("Saindo do gerenciador de tarefas. Até logo!")