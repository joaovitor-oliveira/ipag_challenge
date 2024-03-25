import os
from challenge_10.src.github_api import GithubAPI
from rich import print
from rich.table import Table


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    return input(
            "[1] - Realizar uma busca\n"
            "[2] - Sair\n"
        )


def github_search():
    clear()
    username = input("Insira um username do github: ")
    api = GithubAPI()

    info = api.get_repositories_info(username)

    if not info["has_user"]:
        return print("Usuário não encontrado.")

    table = Table(show_header=True, header_style="bold", show_lines=True)
    table.add_column("Nome")
    table.add_column("Descrição")
    table.add_column("Linguagem")
    table.add_column("Stars")

    for rep in info["data"]:
        table.add_row(
            rep["name"],
            rep["description"],
            rep["language"],
            f"{rep["stargazers_count"]}"
        )

    print(f"[reverse b]Repositórios do usuário: {username}[/]")
    print(table)


def main() -> None:

    options = {
        "1": github_search,
        "2": exit
    }

    clear()
    print("[b]Repositórios de um usuário do github[/]\n\n")

    while True:
        choice = menu()

        if choice in options:
            options[choice]()
        else:
            print(":warning: [red b blink]Opção inválida![/]")


if __name__ == "__main__":
    main()
