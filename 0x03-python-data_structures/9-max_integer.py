#!/usr/bin/python3
# 9-max_integer.py


def max_integer(mylist=[]):
    """Find the biggest integer of a list."""
    if len(mylist) == 0:
        return (None)

    v = mylist[0]
    for i in range(len(mylist)):
        if mylist[i] > v:
            v = mylist[i]

    return (v)

