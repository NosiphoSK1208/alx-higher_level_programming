#!/usr/bin/python3
# 12-roman_to_int.py
def roman_to_int(a_string: str):
    if a_string is None or type(a_string) != str:
        return 0
    arr_data = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    anums = [arr_data[x] for x in a_string] + [0]
    rep = 0

    for i in range(len(anums) - 1):
        if anums[i] >= anums[i+1]:
            rep += anums[i]
        else:
            rep -= anums[i]

    return rep

