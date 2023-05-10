#!/usr/bin/python3
# 12-fizzbuzz.py


def fizzbuzz():
    for the_nums in range(1, 101):
        if the_nums % 3 == 0 and the_nums % 5 == 0:
            print("FizzBuzz ", end="")
        elif the_nums % 3 == 0:
            print("Fizz ", end="")
        elif the_nums % 5 == 0:
            print("Buzz ", end="")
        else:
            print("{} ".format(the_nums), end="")
