from challenge_03.src.shape import Shape


class Square(Shape):
    @staticmethod
    def calculate_area(input_numbers: list) -> float:
        '''
        Calculate the area of square.

        Args:
            input_numbers (list): A list contains required input for a square.

        Returns:
            float: Value of square area.
        '''
        if not Square.validate_input(input_numbers):
            raise ValueError

        side = input_numbers[0]
        return side * side

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        return "Quadrado.\nInsira o valor correspondente ao lado: "

    @staticmethod
    def validate_input(input_numbers: list) -> bool:
        '''
        Returns true if the inputs satisfy the geometric shape criteria, false otherwise.

        Returns:
            bool: The result of validation.
        '''
        return len(input_numbers) == 1 and float(input_numbers[0]) > 0
