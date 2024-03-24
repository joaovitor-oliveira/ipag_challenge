import pytest
from challenge_03.src.shape import Shape
from challenge_03.src.triangle import Triangle


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5, 10], 25.0),
        ([2, 6], 6.0),
        ([17.2, 8.7], 74.82)
    ]
)
def test_given_a_valid_params_when_call_triangle_calculate_area_then_returns_a_correct_result(input, expected):

    result = Triangle.calculate_area(input)

    assert issubclass(Triangle, Shape) is True
    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([5, 10], True),
        ([2, 6], True),
        ([17.2, 8.7], True)
    ]
)
def test_given_a_valid_params_when_call_triangle_validate_input_then_return_true(input, expected):

    result = Triangle.validate_input(input)

    assert result == expected


@pytest.mark.parametrize(
    "input,expected",
    [
        ([-5, 12], False),
        ([42, 0], False),
        ([], False)
    ]
)
def test_given_an_invalid_params_when_call_triangle_validate_input_then_return_false(input, expected):

    result = Triangle.validate_input(input)

    assert result == expected
