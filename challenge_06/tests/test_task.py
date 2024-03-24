import pytest
from challenge_06.src.task import Task
from challenge_06.src.utils import Priority, Status


@pytest.fixture
def task_factory():
    return Task()


@pytest.mark.parametrize(
    "input",
    [
        ("aDescription", Priority.HIGH),
        ("aSecondDescription", Priority.MEDIUM),
        ("aThirdDescription", Priority.LOW),
    ]
)
def test_given_a_valid_params_when_call_constructor_then_instantiate_a_task(input):
    expected_description, expected_priority = input

    task = Task(expected_description, expected_priority)

    assert task.description == expected_description
    assert task.priority == expected_priority
    assert task.status == Status.PENDING


@pytest.mark.parametrize(
    "input",
    [
        ("aDescription", Priority.HIGH),
        ("aSecondDescription", Priority.MEDIUM),
        ("aThirdDescription", Priority.LOW),
    ]
)
def test_given_a_valid_params_when_call_str_task_then_return_the_content(input):
    expected_description, expected_priority = input

    task = Task(expected_description, expected_priority)

    assert str(task) == f"{expected_description} - {expected_priority.name} - {Status.PENDING.name}"


@pytest.mark.parametrize(
    "input",
    [
        ("aDescription", Priority.HIGH),
        ("aSecondDescription", Priority.MEDIUM)
    ]
)
def test_given_a_valid_params_when_call_update_task_then_updated_task_attributes(task_factory, input):
    expected_description, expected_priority = input

    task = task_factory
    task.update(expected_description, expected_priority)

    assert task is not None
    assert task.description == expected_description
    assert task.priority == expected_priority
    assert task.status == Status.PENDING


def test_given_a_task_when_call_complete_task_then_status_is_done(task_factory):

    task = task_factory
    task.complete()

    assert task is not None
    assert task.description == "Task"
    assert task.priority == Priority.MEDIUM
    assert task.status == Status.DONE
