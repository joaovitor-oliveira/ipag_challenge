import requests
from rich import print
from rich.table import Table


class GithubAPI:

    def __init__(self) -> None:
        self.BASE_URL = "https://api.github.com"

    def get_user_repositories(self, username: str) -> dict:
        URL = f"{self.BASE_URL}/users/{username}/repos"

        response = requests.get(URL)

        if response.status_code == 200:
            return response.json()
        else:
            print("Erro ao buscar usuário. Usuário inexistente ou incorreto.")

    def generate_report(self, username: str) -> None:
        repos = self.get_user_repositories(username)

        table = Table(show_header=True, header_style="bold", show_lines=True)
        table.add_column("Nome")
        table.add_column("Descrição")
        table.add_column("Linguagem")
        table.add_column("Stars")

        if repos:
            for rep in repos:
                table.add_row(rep["name"], rep["description"], rep["language"], f"{rep["stargazers_count"]}")
        print(f"[reverse b]Repositórios do usuário: {username}[/]")
        print(table)
