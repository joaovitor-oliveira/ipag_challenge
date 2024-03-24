from challenge_06.src.utils import Priority, Status


class Task:

    def __init__(
            self,
            description: str = "Task",
            priority: Priority = Priority.MEDIUM,
            status: Status = Status.PENDING):
        self.__description = description
        self.__priority = priority
        self.__status = status

    def __str__(self):
        return f"{self.__description} - {self.__priority.name} - {self.__status.name}"

    def update(self, description: str, priority: Priority):
        self.__description = description or self.__description
        self.__priority = priority or self.__priority

    def complete(self):
        self.__status = Status.DONE

    @property
    def description(self):
        return self.__description

    @property
    def priority(self):
        return self.__priority

    @property
    def status(self):
        return self.__status
