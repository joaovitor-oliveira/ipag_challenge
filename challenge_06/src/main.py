import os
from challenge_06.src.utils import Priority, Status
from challenge_06.src.task import Task
from challenge_06.src.task_list import TaskList
from rich import print
from rich.table import Table


OPTIONS = [
        ["1", "ADICIONAR TAREFA"],
        ["2", "VISUALIZAR TAREFAS"],
        ["3", "EDITAR TAREFA"],
        ["4", "CONCLUIR TAREFA"],
        ["5", "REMOVER TAREFA"],
        ["6", "ORDENAR TAREFAS POR PRIORIDADE"],
        ["7", "SAIR"],
    ]


def menu_table():
    table = Table(show_header=True, header_style='bold')
    table.add_column("Opção")
    table.add_column("Ação")

    for opt in OPTIONS:
        table.add_row(opt[0], opt[1])

    print(table)


def show_menu():
    print("[reverse b]ESCOLHA UMA OPCAO: [/]")
    menu_table()


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def get_priority(value):
    priorities = {f"{p.value}": p for p in Priority}

    if value not in priorities:
        return priorities["2"]

    return priorities[value]


def create_task(task_list: TaskList):
    clear()
    description = input("Insira a descrição da tarefa: ")
    priority_choice = input("Escolha a prioridade da tarefa [1] - Alta | [2] - Média (default) | [3] - Baixa\n")
    priority = get_priority(priority_choice)

    task = Task(description, priority)
    task_list.add_task(task)
    task_list.sort_by_status_and_priority()


def format_task_table(task: Task):
    priorities = {}
    priorities[Priority.HIGH] = "ALTA :arrow_up:"
    priorities[Priority.MEDIUM] = "MÉDIA :left_right_arrow:"
    priorities[Priority.LOW] = "BAIXA :arrow_down:"

    _status = {}
    _status[Status.PENDING] = "PENDENTE :hourglass_flowing_sand:"
    _status[Status.DONE] = "CONCLUÍDA :white_check_mark:"

    description = f"[b]{task.description}[/]"
    priority = priorities[task.priority]
    status = _status[task.status]

    return (description, priority, status)


def show_tasks(task_list: TaskList):
    table = Table(show_header=True, header_style='bold')
    table.add_column("No.")
    table.add_column("Descrição")
    table.add_column("Prioridade")
    table.add_column("Status")

    clear()
    print("[b]TAREFAS[/]\n")

    for index, task in enumerate(task_list.get_tasks()):
        description, priority, status = format_task_table(task)
        table.add_row(f"{index + 1}", description, priority, status)

    print(table)


def update_tasks(task_list: TaskList):
    show_tasks(task_list)

    if len(task_list):
        index = int(input("Insira o número da tarefa: ")) - 1

        if task_list.exists_task(index):
            description = input("Insira uma nova descrição (enter para manter a anteiror): ")
            priority_choice = input(
                "Insira uma nova prioridade (enter para manter a anteiror) [1] - Alta | [2] - Média | [3] - Baixa\n"
            )
            priority = get_priority(priority_choice)
            task_list.update_task(index, description, priority)
            task_list.sort_by_status_and_priority()
            print("[b]Tarefa atualiza com sucesso!\n")
        else:
            print("[b]Essa tarefa não existe.[/]\n")
    else:
        print("[b]Não há tarefas.\n")


def complete_tasks(task_list: TaskList):
    show_tasks(task_list)

    if len(task_list):
        index = int(input("Insira o número da tarefa: ")) - 1

        if task_list.exists_task(index):
            task_list.complete_task(index)
            task_list.sort_by_status_and_priority()
            print("[b]Tarefa marcada como concluída!.\n")
        else:
            print("[b]Essa tarefa não existe.[/]\n")
    else:
        print("[b]Não há tarefas.\n")


def delete_tasks(task_list: TaskList):
    show_tasks(task_list)

    if len(task_list):
        index = int(input("Insira o número da tarefa: ")) - 1

        if task_list.exists_task(index):
            task_list.delete_task(index)
            print("[b]Tarefa removida.\n")
        else:
            print("[b]Essa tarefa não existe.[/]\n")
    else:
        print("[b]Não há tarefas.\n")


def sort_by_priority(task_list: TaskList):
    clear()
    task_list.sort_by_status_and_priority()
    print("[b]Tarefas ordenadas[/]")


def main():

    ACTIONS = {
        "1": create_task,
        "2": show_tasks,
        "3": update_tasks,
        "4": complete_tasks,
        "5": delete_tasks,
        "6": sort_by_priority,
        "7": "exit"
    }

    task_list = TaskList()
    clear()
    print(":memo: Boas vindas a TODO List da [green]iPag![/] :pen:")
    show_menu()

    while True:
        choice = input()

        if choice in ACTIONS:
            if ACTIONS[choice] == "exit":
                break
            ACTIONS[choice](task_list)
            show_menu()
        else:
            print(":warning-emoji: [bold red blink]Opção inválida, tente novamente.[/]\n")


if __name__ == "__main__":
    main()
