#!/usr/bin/python3

import random
from enum import IntEnum


class DigitEnum(IntEnum):
    ZR = 0

anum = random.randint(-10, 10)
if anum > DigitEnum.ZR:
    print("{} is positive".format(anum))
elif anum == DigitEnum.ZR:
    print("{} is zero".format(anum))
else:
    print("{} is negative".format(anum))
