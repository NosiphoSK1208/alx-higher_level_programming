#!/usr/bin/python3
# 5-no_c.py


def no_c(a_string):
    """Remove all characters c and C from a string."""
    new_str = [x for x in a_string if x != 'c' and x != 'C']
    return ("".join(new_str))
