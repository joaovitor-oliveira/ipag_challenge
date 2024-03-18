import time
import random
from rich import print


def game():
    print(":question: [reverse bold] Boas vindas ao jogo da adivinhação![/] :question:")
    print(
        "[bold]Instruções[/]:"
        "Tente [u]adivinhar[/] qual é o número [u]oculto.[/] Tal número é um inteiro entre 1 e 100\n"
    )

    random.seed(time.time())
    target = random.randint(1, 101)
    count = 0
    while True:
        try:
            choice = int(input("Insira o seu palpite: "))
            count += 1

            if choice == target:
                print(f":tada: [reverse bold] Parabéns! Você acertou em {count} tentativas.[/] :white_check_mark:")
                break
            else:
                status = "menor" if choice > target else "maior"
                print(f":x: Errou! O número oculto é [bold u]{status}[/] do que seu palpite!")
        except ValueError:
            print(":warning-emoji: [bold red blink] Número inválido, tente novamente.[/]\n")


if __name__ == "__main__":
    game()
