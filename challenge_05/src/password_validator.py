class PasswordValidator:
    '''Class for validating password.'''

    def __init__(self) -> None:
        '''
        Initalize the password validation instance and the errors list as empty.
        '''
        self.__errors = []

    def add_notification(self, notification: str) -> None:
        '''
        Add a notification message to the list of errors.

        Args:
            notification (str): The error message to be added.
        '''
        self.__errors.append(notification)

    def validate(self, password: str) -> None:
        '''
        Validates the password according to various criteria.

        Args:
            password (str): The password to be validated.
        '''
        validations = {
            "length": (len(password) >= 8, "A senha deve ter no mínimo 8 caracteres."),
            "uppercase": (
                any(character.isupper() for character in password), "A senha deve ter pelo menos uma letra maiúscula."
            ),
            "lowercase": (
                any(character.islower() for character in password), "A senha deve ter pelo menos uma letra minúscula."
            ),
            "numeric": (any(character.isnumeric() for character in password), "A senha deve ter pelo menos um número.")
        }

        for _, (is_valid, error_message) in validations.items():
            if not is_valid:
                self.add_notification(error_message)

    def has_errors(self) -> bool:
        '''
        Check if there are validation errors.

        Returns:
            bool: True if there are errors, false otherwise.
        '''
        return len(self.__errors) > 0

    def get_errors(self) -> list:
        '''
        Gets the list of a validation errors.

        Returns:
            list: A list of error message.
        '''
        return self.__errors
