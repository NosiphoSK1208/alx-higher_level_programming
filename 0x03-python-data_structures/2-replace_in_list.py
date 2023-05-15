#!/usr/bin/python3
# 2-replace_in_list.py
def replace_in_list(a_list, ids, elems):
    if ids >= 0 and ids < len(a_list):
        a_list[ids] = elems
    return (a_list)
