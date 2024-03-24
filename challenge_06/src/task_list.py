from challenge_06.src.utils import Priority
from challenge_06.src.task import Task


class TaskList:

    def __init__(self):
        self.__tasks = []

    def __str__(self):
        result = ""
        for index, task in enumerate(self.__tasks):
            result = f"{index} - {task}\n"
        return result

    def __len__(self):
        return len(self.__tasks)

    def add_task(self, task: Task):
        self.__tasks.append(task)

    def update_task(self, index: int, description: str = None, priority: Priority = None):
        self.__tasks[index].update(description, priority)

    def complete_task(self, index: int):
        self.__tasks[index].complete()

    def delete_task(self, index: int):
        del self.__tasks[index]

    def get_tasks(self):
        return self.__tasks

    def exists_task(self, index):
        if index >= 0 and index < len(self.__tasks):
            return True
        else:
            return False

    def sort_by_status_and_priority(self):
        self.__tasks.sort(key=lambda task: (task.status.value, task.priority.value))
