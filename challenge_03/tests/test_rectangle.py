import pytest
from challenge_03.src.shape import Shape
from challenge_03.src.rectangle import Rectangle


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5, 10], 50.0),
        ([2, 6], 12.0),
        ([17.2, 8.7], 149.64)
    ]
)
def test_given_a_valid_params_when_call_rectangle_calculate_area_then_returns_a_correct_result(input, expected):

    result = Rectangle.calculate_area(input)

    assert issubclass(Rectangle, Shape) is True
    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5, 10], True),
        ([2, 6], True),
        ([17.2, 8.7], True)
    ]
)
def test_given_a_valid_params_when_call_rectangle_validate_input_then_return_true(input, expected):

    result = Rectangle.validate_input(input)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([-5, 12], False),
        ([42, 0], False),
        ([], False)
    ]
)
def test_given_an_invalid_params_when_call_rectangle_validate_input_then_return_false(input, expected):

    result = Rectangle.validate_input(input)

    assert result == expected
