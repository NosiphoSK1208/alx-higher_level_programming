#!/usr/bin/python3
# 0-square_matrix_simple.py
def square_matrix_simple(mtx=[]):
    return ([list(map(lambda x: x * x, row)) for row in mtx])

