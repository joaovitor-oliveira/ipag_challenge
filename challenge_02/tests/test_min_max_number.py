import pytest
from challenge_02.src.min_max_number import min_and_max


@pytest.mark.parametrize(
    "input,expected",
    [
        ([3, 5, 0], (5, 0)),
        ([2, 18, 2], (18, 2)),
        ([-1312, -210, -415], (-210, -1312))
    ]
)
def test_given_a_valid_input_when_call_min_and_max_functions_then_returns_a_correct_output(input, expected):
    arr = input

    _max, _min = min_and_max(arr)

    assert _max == expected[0]
    assert _min == expected[1]
