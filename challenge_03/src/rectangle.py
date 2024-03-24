from challenge_03.src.shape import Shape


class Rectangle(Shape):
    @staticmethod
    def calculate_area(input_numbers: list) -> float:
        '''
        Calculate the area of rectangle.

        Args:
            input_numbers (list): A list contains required input for a rectangle.

        Returns:
            float: Value of rectangle area.
        '''
        if not Rectangle.validate_input(input_numbers):
            raise ValueError

        height, width = input_numbers
        return height * width

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        return "Retangulo.\nInsira os valores correspondentes a altura e a largura separados por espaço: "

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
