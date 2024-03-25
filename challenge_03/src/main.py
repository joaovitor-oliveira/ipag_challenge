from challenge_03.src.square import Square
from challenge_03.src.rectangle import Rectangle
from challenge_03.src.circle import Circle
from challenge_03.src.triangle import Triangle
from rich import print


if __name__ == "__main__":

    SHAPES = {
        "1": Square,
        "2": Rectangle,
        "3": Circle,
        "4": Triangle
    }

    try:
        choice = input(
            "Escolha a forma geométrica:\n"
            "[1] Quadrado\n"
            "[2] Retangulo\n"
            "[3] Circulo\n"
            "[4] Triangulo\n"
        )

        input_numbers = [float(x) for x in input(SHAPES[choice]()).split()]

        print(f"{round(SHAPES[choice].calculate_area(input_numbers), 2)} m2")
    except ValueError:
        print(":warning-emoji: [bold red blink] Entrada inválida![/]\n")
    except KeyError:
        print(":warning-emoji: [bold red blink] Opção inválida![/]\n")
