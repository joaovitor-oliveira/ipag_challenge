import pytest
from challenge_10.src.github_api import GithubAPI


@pytest.fixture
def github_api():
    return GithubAPI()


@pytest.fixture
def requests_mock():
    import requests_mock
    with requests_mock.Mocker() as mocker:
        yield mocker


def test_given_a_valid_username_when_call_get_user_repositories_then_success(github_api, requests_mock):
    username = "valid_username"
    expected_api_returns = {"param1": "value1", "param2": "value2", "param3": "value3"}
    expected_response = {
        "has_user": True,
        "data": {"param1": "value1", "param2": "value2", "param3": "value3"}
        }

    requests_mock.get(f"https://api.github.com/users/{username}/repos", status_code=200, json=expected_api_returns)

    response = github_api.get_user_repositories(username)

    assert response == expected_response


def test_given_an_invalid_username_when_call_get_user_repositories_then_failure(github_api, requests_mock):
    username = "invalid"
    expected_api_returns = {}
    expected_response = {
        "has_user": False,
        "data": []
        }

    requests_mock.get(f"https://api.github.com/users/{username}/repos", status_code=404, json=expected_api_returns)

    response = github_api.get_user_repositories(username)
    assert response == expected_response


def test_given_a_valid_username_when_call_get_repositories_info_then_success(github_api, requests_mock):
    username = "valid_username"
    expected_api_returns = [{"name": "value1", "description": "value2", "language": "value3", "stargazers_count": 1}]

    expected_response = {
        "has_user": True,
        "data": [["value1", "value2", "value3", 1]]
        }

    requests_mock.get(f"https://api.github.com/users/{username}/repos", status_code=200, json=expected_api_returns)

    response = github_api.get_repositories_info(username)

    assert response == expected_response


def test_given_an_invalid_username_when_call_get_repositories_info_then_failure(github_api, requests_mock):
    username = "invalid"
    expected_api_returns = []
    expected_response = {
        "has_user": False,
        "data": []
        }

    requests_mock.get(f"https://api.github.com/users/{username}/repos", status_code=404, json=expected_api_returns)

    response = github_api.get_repositories_info(username)
    assert response == expected_response
