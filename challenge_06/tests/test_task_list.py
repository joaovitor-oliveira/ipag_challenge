import pytest
from challenge_06.src.task import Task
from challenge_06.src.task_list import TaskList
from challenge_06.src.utils import Priority, Status


@pytest.fixture
def task_list_factory():
    task_list = TaskList()
    task_list.add_task(Task("First Task", Priority.MEDIUM))
    task_list.add_task(Task("Second Task", Priority.LOW))
    task_list.add_task(Task("Third Task", Priority.HIGH))

    return task_list


def test_call_constructor_then_instantiate_a_task_list():
    task_list = TaskList()

    assert task_list is not None
    assert len(task_list) == 0


def test_given_a_populated_task_list_when_call_str_then_return_the_content(task_list_factory):
    task = Task()
    task_list = TaskList()
    task_list.add_task(task)

    expected_output = f"0 - {str(task)}\n"

    assert str(task_list) == expected_output


def test_given_a_new_task_when_call_add_task_then_insert_a_task():
    task_list = TaskList()
    task = Task()

    task_list.add_task(task)

    assert len(task_list) == 1


@pytest.mark.parametrize(
    "input",
    [
        (0, "Updated description", Priority.LOW),
        (0, "Another Description", Priority.HIGH)
    ]
)
def test_given_a_valid_params_when_call_update_task_then_task_updated(task_list_factory, input):
    task_list = task_list_factory
    index, description, priority = input

    task_list.update_task(index, description, priority)

    updated_task = task_list.get_tasks()[index]

    assert updated_task.description == description
    assert updated_task.priority == priority


@pytest.mark.parametrize(
    "input,expected",
    [
        (1, Status.DONE),
        (2, Status.DONE)
    ]
)
def test_given_an_index_when_call_complete_task_then_task_completed(task_list_factory, input, expected):
    task_list = task_list_factory
    index = input
    expected_result = expected

    task_list.complete_task(index)

    completed_task = task_list.get_tasks()[index]

    assert completed_task.status == expected_result


def test_given_an_index_when_call_delete_task_then_list_size_decreases(task_list_factory):
    task_list = task_list_factory

    task_list.delete_task(0)

    assert len(task_list) == 2


@pytest.mark.parametrize(
    "input,expected",
    [
        (1, True),
        (2, True),
        (3, False),
        (80, False)
    ]
)
def test_given_an_index_when_call_exists_tasks_then_returns_if_task_exists_or_not(task_list_factory, input, expected):
    task_list = task_list_factory
    index = input
    expected_result = expected

    result = task_list.exists_task(index)

    assert result is expected_result


def test_when_call_sort_by_status_and_priority_then_sorted_task_list(task_list_factory):
    task_list = task_list_factory
    descriptions = [task.description for task in task_list.get_tasks()]
    expected_order_descriptions = [
        descriptions[2],
        descriptions[0],
        descriptions[1]
    ]

    task_list.sort_by_status_and_priority()
    actual_order_descriptions = [task.description for task in task_list.get_tasks()]

    assert actual_order_descriptions == expected_order_descriptions
