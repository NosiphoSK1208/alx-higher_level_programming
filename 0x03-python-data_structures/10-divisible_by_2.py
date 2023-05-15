#!/usr/bin/python3
# 10-divisible_by_2.py

def divisible_by_2(a_list=[]):
    mult = []
    for i in range(len(a_list)):
        if a_list[i] % 2 == 0:
            mult.append(True)
        else:
            mult.append(False)

    return (mult)
