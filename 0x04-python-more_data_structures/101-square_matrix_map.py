#!/usr/bin/python3
# 100-weight_average.py
def weight_average(own_lists=[]):
    if not own_lists:
        return 0

    avg_num = 0
    size_den = 0

    for tup in own_lists:
        avg_num += tup[0] * tup[1]
        size_den += tup[1]

    return (avg_num / size_den)

