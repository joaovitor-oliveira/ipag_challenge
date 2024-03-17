from challenge_03.src.shape import Shape


class Rectangle(Shape):
    @staticmethod
    def calculate_area(input_numbers):
        if not Rectangle.validate_input(input_numbers):
            raise ValueError

        height, width = input_numbers
        return height * width

    def __str__(self):
        return "Retangulo.\nInsira os valores correspondentes ao lado maior e o lado menor para calcular a área: "

    @staticmethod
    def validate_input(input_numbers):
        return (
            len(input_numbers) == 2 and
            float(input_numbers[0]) > 0 and
            float(input_numbers[1]) > 0
        )
