from poetry_template.even_odd import EvenOddNumber

def test_even_odd():
    number = EvenOddNumber(10)
    assert number.get_num() == 10
    assert number.get_num() != 11
