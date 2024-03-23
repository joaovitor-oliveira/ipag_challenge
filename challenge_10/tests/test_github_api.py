import pytest
from challenge_10.src.github_api import GithubAPI


@pytest.fixture
def github_api():
    return GithubAPI()


def test_given_a_valid_username_when_call_get_user_repositories_then_success(mocker, github_api):
    username = "valid_username"
    expected = [
        {"name": "repository_1", "description": "description_1", "language": "language_1", "stargazers_count": "1"}
    ]

    mocker.patch.object(github_api, "get_user_repositories", return_value=expected)

    response = github_api.get_user_repositories(username)

    assert response == expected


def test_given_an_invalid_username_when_call_get_user_repositories_then_failure(mocker, github_api, capsys):
    username = "invalid"

    mocker.patch.object(github_api, "get_user_repositories", return_value=None)

    github_api.get_user_repositories(username)

    out, _ = capsys.readouterr()
    assert out in "Erro ao buscar usuário. Usuário inexistente ou incorreto."
