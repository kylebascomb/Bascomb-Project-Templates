


class EvenOddNumber:
    def __init__(self, num) -> None:
        self.num = num

    def add_num(self, num_to_add):
        self.num += num_to_add

    def subtract_num(self, num_to_subtract):
        self.num -= num_to_subtract

    def num_is_even(self):
        return self.num % 2 == 0

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num



