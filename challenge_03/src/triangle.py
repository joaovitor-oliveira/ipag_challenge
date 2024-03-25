from challenge_03.src.shape import Shape


class Triangle(Shape):
    @staticmethod
    def calculate_area(input_numbers: list) -> float:
        '''
        Calculate the area of triangle.

        Args:
            input_numbers (list): A list contains required input for a triangle.

        Returns:
            float: Value of triangle area.
        '''
        if not Triangle.validate_input(input_numbers):
            raise ValueError

        base, height = input_numbers
        return base * height / 2

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        return "Triangulo.\nInsira os valores correspondentes a base e a altura separados por espaço: "

    @staticmethod
    def validate_input(input_numbers: list) -> bool:
        '''
        Returns true if the inputs satisfy the geometric shape criteria, false otherwise.

        Returns:
            bool: The result of validation.
        '''
        return (
            len(input_numbers) == 2 and
            float(input_numbers[0]) > 0 and
            float(input_numbers[1]) > 0
        )
