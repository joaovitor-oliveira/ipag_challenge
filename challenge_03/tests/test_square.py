import pytest
from challenge_03.src.shape import Shape
from challenge_03.src.square import Square


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5], 25.0),
        ([2], 4.0),
        ([17.2], 295.84)
    ]
)
def test_given_a_valid_params_when_call_square_calculate_area_then_returns_a_correct_result(input, expected):

    result = Square.calculate_area(input)

    assert issubclass(Square, Shape) is True
    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5], True),
        ([2], True),
        ([17.2], True)
    ]
)
def test_given_a_valid_params_when_call_square_validate_input_then_return_true(input, expected):

    result = Square.validate_input(input)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([-5], False),
        ([0], False),
        ([123, 321], False)
    ]
)
def test_given_an_invalid_params_when_call_square_validate_input_then_return_false(input, expected):

    result = Square.validate_input(input)

    assert result == expected
