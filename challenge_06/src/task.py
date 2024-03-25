from challenge_06.src.utils import Priority, Status


class Task:
    '''Class representing a task with a description, priority and status.'''
    def __init__(
            self,
            description: str = "Task",
            priority: Priority = Priority.MEDIUM,
            status: Status = Status.PENDING) -> None:
        '''
        Initializes a task instance with the given description, priority and status.

        Args:
            description (str, optional): The description of a the task (default is "Task")
            priority (Priority, optional): The priority of the task (default is MEDIUM)
            status (Status, optional): The status of the task (default is PENDING)
        '''
        self.__description = description
        self.__priority = priority
        self.__status = status

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        return f"{self.__description} - {self.__priority.name} - {self.__status.name}"

    def update(self, description: str, priority: Priority) -> None:
        '''
        Update the description and priority of the task.

        Args:
            description (str): The new description of task.
            priority (Priority): The new priority of task.
        '''
        self.__description = description or self.__description
        self.__priority = priority or self.__priority

    def complete(self) -> None:
        '''Marks the task as completed.'''
        self.__status = Status.DONE

    @property
    def description(self) -> str:
        '''Returns a description of task.'''
        return self.__description

    @property
    def priority(self) -> Priority:
        '''Returns the priority of task.'''
        return self.__priority

    @property
    def status(self) -> Status:
        '''Returns the status of task.'''
        return self.__status
