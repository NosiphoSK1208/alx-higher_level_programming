#!/usr/bin/python3
# 2-uniq_add.py
def uniq_add(own_list=[]):
    out_put = 0
    for x in set(own_list):
        out_put += x
    return (out_put)
