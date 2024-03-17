from challenge_03.src.shape import Shape


class Triangle(Shape):
    @staticmethod
    def calculate_area(input_numbers):
        if not Triangle.validate_input(input_numbers):
            raise ValueError

        base, height = input_numbers
        return base * height / 2

    def __str__(self):
        return "Triangulo.\nInsira os valores correspondentes a base e a altura para calcular a área: "

    @staticmethod
    def validate_input(input_numbers):
        return (
            len(input_numbers) == 2 and
            float(input_numbers[0]) > 0 and
            float(input_numbers[1]) > 0
        )
