import os
from challenge_08.src.sales import Sales
from rich import print


def clear():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def menu():
    print("\n\nRelatórios disponíveis:\n")
    choice = input(
        "[0] - Visualizar um exemplo dos dados do arquivo e como estão organizados\n"
        "[1] - Unidades vendidas por tipo de produto\n"
        "[2] - Total de receitas por tipo de produto\n"
        "[3] - Custo total por tipo de produto\n"
        "[4] - Lucro total por tipo de produto\n"
        "[5] - Vendas por tipo de produto e região\n"
        "[6] - Tipos de produto com maior receita de cada país\n"
        "[7] - Sair\n"
    )

    return choice


def main():
    sales = Sales("challenge_08/files/sales.csv")

    if sales is not None:
        options = {
            "0": ("[reverse]Exemplo dos dados do arquivo[/]\n", sales.sample),
            "1": ("[reverse]Unidades vendidas por tipo de produto[/]\n", sales.get_units_sold_by_item_type),
            "2": ("[reverse]Total de receitas por tipo de produto[/]\n", sales.get_total_revenue_by_item_type),
            "3": ("[reverse]Custo total por tipo de produto[/]\n", sales.get_total_cost_by_item_type),
            "4": ("[reverse]Lucro total por tipo de produto[/]\n", sales.get_total_profit_by_item_type),
            "5": ("[reverse]Vendas por tipo de produto e região[/]\n", sales.get_unit_solds_by_item_type_and_region),
            "6": (
                "[reverse]Tipos de produto com maior receita de cada país[/]\n",
                sales.get_item_type_with_highest_revenue_by_country
            )
        }

        clear()
        print("\n[b]Análise dos dados do arquivo sales.csv[/]\n")
        while True:
            try:
                choice = menu()
                if choice == "7":
                    print("[b]Encerrando...[/]")
                    break
                clear()
                report = options[choice]
                print(report[0], report[1]().to_string())
            except KeyError:
                print(":warning: [red b blink]Opção inválida![/]")


if __name__ == "__main__":
    main()
