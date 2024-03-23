from challenge_10.src.github_api import GithubAPI


def main():
    api = GithubAPI()

    api.generate_report("cacajr")


if __name__ == "__main__":
    main()
