import pytest
from challenge_03.src.shape import Shape
from challenge_03.src.circle import Circle


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5], 78.54),
        ([2.5], 19.63),
        ([8.7], 237.79)
    ]
)
def test_given_a_valid_params_when_call_circle_calculate_area_then_returns_a_correct_result(input, expected):

    result = Circle.calculate_area(input)

    assert issubclass(Circle, Shape) is True
    assert round(result, 2) == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5], True),
        ([2], True),
        ([17.2], True)
    ]
)
def test_given_a_valid_params_when_call_circle_validate_input_then_return_true(input, expected):

    result = Circle.validate_input(input)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([-5], False),
        ([0], False),
        ([123, 321], False)
    ]
)
def test_given_an_invalid_params_when_call_circle_validate_input_then_return_false(input, expected):

    result = Circle.validate_input(input)

    assert result == expected
