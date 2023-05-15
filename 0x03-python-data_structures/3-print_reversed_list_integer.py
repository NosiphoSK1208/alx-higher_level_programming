#!/usr/bin/python3
# 3-print_reversed_list_integer.py
def print_reversed_list_integer(all_list=[]):
    if isinstance(all_list, list):
        all_list.reverse()
        for x in all_list:
            print("{:d}".format(x))
