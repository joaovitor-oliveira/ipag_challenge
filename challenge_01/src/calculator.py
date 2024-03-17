from ipag_challenge.challenge_01.src.utils import operations


if __name__ == "__main__":
    print("BEM-VINDO A CALCULADORA iPag!\n\n")

    choice = "y"
    while choice.lower() == "y":
        try:
            x, y = input(
                "Insira dois números separados por espaço: "
                ).split()

            _operation = input(
                "Escolha a operação desejada: "
                "adição[+] subtração[-] multiplicação[*] divisão[/]\n"
            )

            answer = operations[_operation](float(x), float(y))
            print(
                f"Resultado: {round(answer, 2)}"
                if answer != "undefined"
                else "Não é possível dividir por zero!"
            )
        except ValueError:
            print("Números inválidos!\n")

        choice = input("Deseja realizar outro cálculo? [Y/n] ")
