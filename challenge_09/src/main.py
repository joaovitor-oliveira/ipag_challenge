import os
from challenge_09.src.price_method import PriceMethod
from challenge_09.src.financing import Financing
from rich import print
from rich.table import Table


def clear() -> None:
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def is_numeric(input: str) -> bool:
    try:
        float(input)
        return True
    except ValueError:
        return False


def validate_input(value: str, down_payment: str, rate: str, monthly_payments: str) -> list:
    notifications = []

    inputs = {
        "Valor": (value, lambda x: is_numeric(x) and float(x) > 0),
        "Valor de entrada": (down_payment, lambda x: is_numeric(x) and float(x) >= 0),
        "Taxa de juros": (rate, lambda x: is_numeric(x) and float(x) >= 0),
        "Período": (monthly_payments, lambda x: x.isnumeric() and int(x) > 0)
    }

    for param, (input, validation) in inputs.items():
        if not validation(input):
            notifications.append(f"{param} inválido.")

    return notifications


def generate_simple_report(financing: Financing) -> None:
    monthly_payment = round(financing.calculate_monthly_payment(), 2)
    total_value = round(financing.calculate_total_value(), 2)
    emr = round(financing.calculate_effective_monthly_rate() * 1000, 2)
    tec = round(financing.calculate_total_effective_cost(), 2)

    table = Table(show_header=True, header_style='bold')
    table.add_column("Prestação")
    table.add_column("Custo efetivo total")
    table.add_column("Juros efetivos mensais")
    table.add_column("Valor total")

    table.add_row(f"{monthly_payment}", f"{tec}", f"{emr}", f"{total_value}")
    print(table)


def generate_complete_report(financing: Financing, value: float, n: int, rate: float) -> None:
    table = Table(show_header=True, header_style='bold')
    table.add_column("No")
    table.add_column("Prestação")
    table.add_column("Juros")
    table.add_column("Amortização")
    table.add_column("Saldo devedor")

    monthly_payment = round(financing.calculate_monthly_payment(), 2)
    outstanding_balance = value

    table.add_row(
            "0",
            "R$ 0.00",
            "R$ 0.00",
            "R$ 0.00",
            f"R$ {round(outstanding_balance, 2)}"
        )

    for month in range(n):
        monthly_interest = outstanding_balance * rate
        amortization = monthly_payment - monthly_interest
        outstanding_balance = max(0, outstanding_balance - amortization)
        table.add_row(
            f"{month + 1}",
            f"R$ {round(monthly_payment, 2)}",
            f"R$ {round(monthly_interest, 2)}",
            f"R$ {round(amortization, 2)}",
            f"R$ {round(outstanding_balance, 2)}"
        )

    table.add_row(
        "[b]Totais[/]",
        f"[b]R$ {round(financing.calculate_total_value(), 2)}[/]",
        f"[b]R$ {round(financing.calculate_total_effective_cost(), 2)}[/]",
        f"[b]R$ {round(value, 2)}[/]",
        ""
    )

    print(table)


def main():
    while True:
        clear()
        print(
            "[reverse b]Cálculo de financiamento PRICE[/]\n\n"
            "Essa simulação traz uma estimativa de valor baseado na tabela PRICE"
        )

        value = input("Valor: ")
        down_payment = input("Valor de entrada: ")
        rate = input("Taxa de juros % mensal: ")
        monthly_payments = input("Período em meses: ")

        notifications = validate_input(
            value,
            down_payment,
            rate,
            monthly_payments
        )

        if len(notifications) == 0:
            value = float(value)
            down_payment = float(down_payment)
            rate = float(rate)
            monthly_payments = int(monthly_payments)

            if value - down_payment > 0:
                financing = Financing(PriceMethod(value-down_payment, monthly_payments, rate / 100))
                generate_simple_report(financing)
                print("")
                generate_complete_report(financing, value-down_payment, monthly_payments, rate / 100)
            else:
                print(":warning: [red b blink]Valor de entrada maior ou igual ao do financiamento.[/]\n")
        else:
            for n in notifications:
                print(f"[red b blink] - {n}[/]")

        choice = input("Realizar outra simulação? [Y/n] ").upper()
        if choice != "Y":
            break


if __name__ == "__main__":
    main()
