import os
import time
from challenge_07.src.brand_exception import BrandException
from challenge_07.src.lg_remote_control import LGRemoteControl
from challenge_07.src.samsung_remote_control import SamsungRemoteControl
from challenge_07.src.sony_remote_control import SonyRemoteControl
from challenge_07.src.lg_tv import LGTV
from challenge_07.src.samsung_tv import SamsungTV
from challenge_07.src.sony_tv import SonyTV
from rich import print

TVS = {
        "1": (LGTV(), "LG"),
        "2": (SamsungTV(), "SAMSUNG"),
        "3": (SonyTV(), "Sony"),
    }

CONTROLS = {
    "1": (LGRemoteControl, "LG"),
    "2": (SamsungRemoteControl, "Samsung"),
    "3": (SonyRemoteControl, "Sony")
}


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def select_tv():
    tv_choice = input(
                "TVs disponíveis: [1] LG - [2] Samsung - [3] Sony\n"
                "Insira o dígito correspondende a tv desejada: "
            )

    return TVS[tv_choice]


def select_control():
    control_choice = input(
                "Controles disponíveis: [1] LG - [2] Samsung - [3]Sony\n"
                "Insira o dígito correspondende ao controle desejado: "
            )
    return CONTROLS[control_choice]


def main():
    while True:
        try:
            print("\n[b reverse]Comunicação entre objetos[/]\n\n")
            choice = input("[1] - Simular\n[2] - Sair\n")
            if choice == "1":
                clear()

                selected_tv = select_tv()
                print(f"[b]TV {selected_tv[1]} selecionada.")

                selected_control = select_control()
                print(f"[b]Controle {selected_control[1]} selecionado.")

                print("\nSimulando...")
                time.sleep(0.5)

                tv = selected_tv[0]
                control = selected_control[0](tv)
                print(control.toggle_power())

                time.sleep(0.5)
            if choice == "2":
                break
        except KeyError:
            print(":warning: [red b blink] Opção inválida![/]")
        except BrandException as error:
            print(f":warning: [red b blink]{error}")


if __name__ == "__main__":
    main()
