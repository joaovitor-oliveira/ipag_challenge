from challenge_01.src.utils import operations
from rich import print


if __name__ == "__main__":
    print("BEM-VINDO A CALCULADORA iPag!\n\n")

    choice = "y"
    while choice.lower() == "y":
        try:
            _operation = input(
                "Escolha a operação desejada: "
                "adição[+] subtração[-] multiplicação[*] divisão[/]\n"
            )

            x, y = input(
                "Insira dois números separados por espaço: "
                ).split()

            answer = operations[_operation](float(x), float(y))
            print(
                f"Resultado: {round(answer, 2)}"
                if answer != "undefined"
                else ":warning-emoji: [bold red blink] Não é possível dividir por zero![/]"
            )
        except ValueError:
            print(":warning-emoji: [bold red blink] Números inválidos![/]\n")
        except KeyError:
            print(":warning-emoji: [bold red blink] Opção inválida![/]\n")

        choice = input("Deseja realizar outro cálculo? [Y/n] ")
