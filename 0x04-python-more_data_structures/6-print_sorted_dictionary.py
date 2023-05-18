#!/usr/bin/python3
# 6-print_sorted_dictionary.py
def print_sorted_dictionary(dict):
    [print("{}: {}".format(i, dict[i])) for i in sorted(dict)]

