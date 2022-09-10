

from ast import Num


class EvenOddNumber:
    def __init__(self, num) -> None:
        self.num = num
    
    def add_num(self, num_to_add):
        self.num += num_to_add
    
    def subtract_num(self, num_to_subtract):
        self.num -= num_to_subtract
    
    def multiply_num(self, num_to_multiply):
        self.num *= num_to_multiply
    
    def divide_num(self, num_to_divide):
        self.num /= num_to_divide

    def num_is_even(self):
        return self.num % 2 == 0

    def get_num(self):
        return self.num

    def set_num(self, num):
        self.num = num

if __name__ == "__main__":
    number = EvenOddNumber(5)
    print("Starting number at 5...")
    number.add_num(5)
    print("Adding 5 to number. Number is now {}".format(number.get_num()))
    
