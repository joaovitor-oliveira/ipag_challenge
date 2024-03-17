import pytest
from ipag_challenge.challenge_01.src.utils import operations


@pytest.mark.parametrize(
    "input,expected",
    [
        ((3, 5), 8.0),
        ((2, 2), 4.0),
        ((123456789, 987654321.0), 1111111110)
    ]
)
def test_given_a_valid_numbers_when_call_addition_operator_then_returns_a_correct_sum(input, expected):
    x, y = input
    operator = "+"

    answer = operations[operator](float(x), float(y))

    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((3, 5), -2.0),
        ((2, 2), 0.0),
        ((123456789, 987654321), -864197532.0)
    ]
)
def test_given_a_valid_numbers_when_call_subraction_operator_then_returns_a_correct_difference(input, expected):
    x, y = input
    operator = "-"

    answer = operations[operator](float(x), float(y))

    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((3, 5), 15.0),
        ((2, 2), 4.0),
        ((-212, 570), -120840.0)
    ]
)
def test_given_a_valid_numbers_when_call_multiplication_operator_then_returns_a_correct_multiplication(input, expected):
    x, y = input
    operator = "*"

    answer = operations[operator](float(x), float(y))

    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((30, 5), 6.0),
        ((2, 2), 1.0),
        ((0, 570), 0.0),
        ((-16, 4), -4.0)
    ]
)
def test_given_a_valid_numbers_when_call_division_operator_then_returns_a_correct_quocient(input, expected):
    x, y = input
    operator = "/"

    answer = operations[operator](float(x), float(y))

    assert answer == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ((0, 0), "undefined"),
        ((-16, 0), "undefined")
    ]
)
def test_given_a_zero_divisor_when_call_division_operator_then_return_undefined(input, expected):
    x, y = input
    operator = "/"

    answer = operations[operator](float(x), float(y))

    assert answer == expected
