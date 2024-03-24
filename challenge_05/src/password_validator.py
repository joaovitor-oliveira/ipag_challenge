class PasswordValidator:

    def __init__(self):
        self.__errors = []

    def add_notification(self, notification):
        self.__errors.append(notification)

    def validate(self, password):
        if len(password) < 8:
            self.add_notification("A senha deve ter no mínimo 8 caracteres.")

        if not any(character.isupper() for character in password):
            self.add_notification("A senha deve ter pelo menos uma letra maiúscula.")

        if not any(character.islower() for character in password):
            self.add_notification("A senha deve ter pelo menos uma letra minúscula.")

        if not any(character.isnumeric() for character in password):
            self.add_notification("A senha deve ter pelo menos um número.")

    def has_errors(self):
        return len(self.__errors) > 0

    def get_errors(self):
        return self.__errors
