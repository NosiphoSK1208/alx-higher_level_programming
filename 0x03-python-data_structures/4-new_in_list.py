#!/usr/bin/python3
# 4-new_in_list.py


def new_in_list(alists, i, lmnts):
    if i < 0 or i > (len(alists) - 1):
        return (alists)

    copy = [x for x in alists]
    copy[i] = lmnts
    return (copy)
