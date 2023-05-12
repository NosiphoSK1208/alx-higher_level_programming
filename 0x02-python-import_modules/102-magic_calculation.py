#!/usr/bin/python3
# 102-magic_calculation.py

def magic_calculation(num, num2):
    """Match bytecode provided by Holberton School."""
    from magic_calculation_102 import add, sub

    if num < num2:
        c = add(num, num2)
        for i in range(4, 6):
            c = add(c, i)
        return (c)

    else:
        return(sub(num, num2))
