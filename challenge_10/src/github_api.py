import requests


class GithubAPI:

    def __init__(self) -> None:
        self.BASE_URL = "https://api.github.com"

    def get_user_repositories(self, username: str) -> dict:
        '''
        Get user repositories

        Args:
            username (str): A github username.

        Returns:
            dict: User repositories.
        '''
        URL = f"{self.BASE_URL}/users/{username}/repos"

        response = requests.get(URL)

        if response.status_code == 200:
            return {"has_user": True, "data": response.json()}

        return {"has_user": False, "data": []}

    def get_repositories_info(self, username: str) -> dict:
        '''
        Get the users repositiries with the information of name, description, language and stars.

        Args:
            username (str): A github username.

        Returns:
            dict: User repositories info.
        '''
        repos = self.get_user_repositories(username)
        result = []

        if not repos["has_user"]:
            return repos

        for rep in repos["data"]:
            result.append({
                "name": rep["name"],
                "description": rep["description"],
                "language": rep["language"],
                "stargazers_count": rep["stargazers_count"]
            })

        return {"has_user": True, "data": result}
