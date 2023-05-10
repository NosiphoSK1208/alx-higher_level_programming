#!/usr/bin/python3
# 102-magic_calculation.py


def magic_calculation(f_num, s_num, t_num):
    if f_num < s_num:
        return (t_num)
    if t_num > s_num:
        return (f_num + s_num)
    return (f_num*s_num - t_num)
