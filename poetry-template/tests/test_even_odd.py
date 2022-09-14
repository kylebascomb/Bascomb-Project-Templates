from poetry_template.even_odd import EvenOddNumber
import pytest


@pytest.mark.parametrize(
    "test_input, expected",
    [(10, True), (11, False), (0, True), (-1, False), (-2, True)],
)
def test_even_odd(test_input, expected):
    number = EvenOddNumber(test_input)
    assert number.num_is_even() == expected


@pytest.mark.parametrize(
    "test_input, expected", [(10, 10), (5, 5), (0, 0), (-2, -2), (-100000, -100000)]
)
def test_add(test_input, expected):
    number = EvenOddNumber(0)
    number.add_num(test_input)
    assert number.get_num() == expected


@pytest.mark.parametrize(
    "test_input, expected", [(10, -10), (5, -5), (0, 0), (-2, 2), (-100000, 100000)]
)
def test_subtract(test_input, expected):
    number = EvenOddNumber(0)
    number.subtract_num(test_input)
    assert number.get_num() == expected


@pytest.mark.parametrize(
    "test_input, expected", [(10, 10), (5, 5), (0, 0), (-2, -2), (-100000, -100000)]
)
def test_set(test_input, expected):
    number = EvenOddNumber(0)
    number.set_num(test_input)
    assert number.get_num() == expected


@pytest.mark.xfail
def test_fail():
    number = EvenOddNumber(0)
    assert number.get_num() == -1
