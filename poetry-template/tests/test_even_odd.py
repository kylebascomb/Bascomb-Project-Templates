from poetry_template.even_odd import EvenOddNumber
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [(10, True), (11, False), (0, True), (-1, False), (-2, True)],
)
def test_even_odd(test_input, expected):
    number = EvenOddNumber(test_input)
    assert number.num_is_even() == expected
