from challenge_03.src.shape import Shape
from math import pi


class Circle(Shape):
    @staticmethod
    def calculate_area(input_numbers):
        if not Circle.validate_input(input_numbers):
            raise ValueError

        radius = input_numbers[0]
        return radius * radius * pi

    def __str__(self):
        return "Circulo.\nInsira o valor correspondente ao raio para calcular a área: "

    @staticmethod
    def validate_input(input_numbers):
        return len(input_numbers) == 1 and float(input_numbers[0]) > 0
