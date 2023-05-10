#!/usr/bin/python3
import random

a_number = random.randint(-10000, 10000)


if a_number >= 0:
    e_digit = a_number % 10
else:
    e_digit = a_number * -1 % 10 * -1

msg = "Last digit of %d is %d and is" % (a_number, e_digit)

if e_digit == 0:
    print(msg, "0")
elif e_digit > 5:
    print(msg, "greater than 5")
else:
    print(msg, "less than 6 and not 0")

