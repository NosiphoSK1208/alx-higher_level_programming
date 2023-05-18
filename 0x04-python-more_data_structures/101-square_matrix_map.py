#!/usr/bin/python3
def square_matrix_map(mtx=[]):
    return (list(map(lambda sk: list(map(lambda kh: kh ** 2, sk[:])), mtx)))

