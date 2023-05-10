#!/usr/bin/python3
# 9-print_last_digit.py


def print_last_digit(nums):
    print(abs(nums) % 10, end="")
    return (abs(nums) % 10)
