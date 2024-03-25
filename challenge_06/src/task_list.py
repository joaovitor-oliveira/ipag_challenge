from challenge_06.src.utils import Priority
from challenge_06.src.task import Task


class TaskList:

    def __init__(self) -> None:
        '''Initializes a list of tasks.'''
        self.__tasks = []

    def __str__(self) -> str:
        '''Returns the representation of object as a string.'''
        result = ""
        for index, task in enumerate(self.__tasks):
            result = f"{index} - {task}\n"
        return result

    def __len__(self) -> int:
        '''Returns the number of tasks in the list.'''
        return len(self.__tasks)

    def add_task(self, task: Task) -> None:
        '''Adds a task in the list.'''
        self.__tasks.append(task)

    def update_task(self, index: int, description: str = None, priority: Priority = None) -> None:
        '''Updates the task in a given index given a new description and priority.'''
        self.__tasks[index].update(description, priority)

    def complete_task(self, index: int) -> None:
        '''Marks the task as completed on given index.'''
        self.__tasks[index].complete()

    def delete_task(self, index: int) -> Task:
        '''Deletes a task in a given index.'''
        del self.__tasks[index]

    def get_tasks(self) -> list:
        '''Return the list of tasks.'''
        return self.__tasks

    def exists_task(self, index: int) -> bool:
        '''
        Check if a tasks exists in a given index.

        Args:
            index (int): The index to be checked.

        Returns:
            bool: True if task exists, False otherwise.
        '''
        if index >= 0 and index < len(self.__tasks):
            return True
        else:
            return False

    def sort_by_status_and_priority(self) -> None:
        '''Sorts the tasks by status and priority.'''
        self.__tasks.sort(key=lambda task: (task.status.value, task.priority.value))
