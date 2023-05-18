#!/usr/bin/python3
# 8-simple_delete.py
def simple_delete(dict, key=""):
    if key in dict:
        del dict[key]
    return (dict)
