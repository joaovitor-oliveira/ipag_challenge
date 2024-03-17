from challenge_03.src.shape import Shape


class Square(Shape):
    @staticmethod
    def calculate_area(input_numbers):
        if not Square.validate_input(input_numbers):
            raise ValueError

        side = input_numbers[0]
        return side * side

    def __str__(self):
        return "Quadrado.\nInsira o valor correspondente ao lado para calcular a área: "

    @staticmethod
    def validate_input(input_numbers):
        return len(input_numbers) == 1 and float(input_numbers[0]) > 0
