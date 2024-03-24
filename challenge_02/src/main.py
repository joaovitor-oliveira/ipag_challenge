def min_and_max(arr):
    max_number = max(arr[0], max(arr[1], arr[2]))
    min_number = min(arr[0], min(arr[1], arr[2]))

    return max_number, min_number


if __name__ == "__main__":
    print("VERIFICADOR DE NUMEROS: MAIOR E MENOR\n")

    try:
        arr = [float(x) for x in input("Insira tres numeros separados por espaco: ").split()]

        max_number, min_number = min_and_max(arr)

        print(f"Maior: {max_number}\nMenor: {min_number}")

    except ValueError:
        print("Números inválidos.")
