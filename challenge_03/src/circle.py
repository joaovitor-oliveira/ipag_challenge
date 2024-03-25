from challenge_03.src.shape import Shape
from math import pi


class Circle(Shape):
    @staticmethod
    def calculate_area(input_numbers: list) -> float:
        '''
        Calculate the area of circle.

        Args:
            input_numbers (list): A list contains required input for a circle.

        Returns:
            float: Value of circle area.
        '''
        if not Circle.validate_input(input_numbers):
            raise ValueError

        radius = input_numbers[0]
        return radius * radius * pi

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        return "Circulo.\nInsira o valor correspondente ao raio: "

    @staticmethod
    def validate_input(input_numbers: list) -> bool:
        '''
        Returns true if the inputs satisfy the geometric shape criteria, false otherwise.

        Returns:
            bool: The result of validation.
        '''
        return len(input_numbers) == 1 and float(input_numbers[0]) > 0
