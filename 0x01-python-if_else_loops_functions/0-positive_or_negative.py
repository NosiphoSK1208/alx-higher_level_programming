#!/usr/bin/python3

import random
from enum import IntEnum


class DigitEnum(IntEnum):
    ZR = 0


number = random.randint(-10, 10)
if number > DigitEnum.ZR:
    print("{} is positive".format(number))
elif number == DigitEnum.ZR:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
