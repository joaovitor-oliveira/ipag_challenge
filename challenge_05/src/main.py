from challenge_05.src.password_validator import PasswordValidator
from rich import print


if __name__ == "__main__":

    while True:
        print(":closed_lock_with_key: Boas vindas ao Validador de Senhas [green]iPag![/]\n")
        print(
            "Para garantir que voce possua uma senha forte, sua senha deve conter:\n"
            "[reverse b] Pelo menos [green]08[/] caracterres[/]\n"
            "[reverse b] Pelo menos uma letra maiúscula[/]\n"
            "[reverse b] Pelo menos uma letra minúscula[/]\n"
            "[reverse b] Pelo menos um número[/]\n"
        )

        password = input("Insira a senha a ser validada: ")

        validator = PasswordValidator()
        validator.validate(password)

        if validator.has_errors():
            print("[bold red blink] Senha inválida![/]\n")
            for error in validator.get_errors():
                print(f"[red blink]- {error}")
        else:
            print("[bold green blink]Senha válida![/]")

        choice = input("\nDeseja fazer outra validação? [Y/n] ").upper()

        if choice != "Y":
            print("Obrigado por utilizar nosso validador!")
            break
