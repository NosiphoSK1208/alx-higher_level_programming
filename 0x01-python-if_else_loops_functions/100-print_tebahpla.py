#!/usr/bin/python3
# 100-print_tebahpla.py
for rage_num in range(122, 96, -1):
    if rage_num % 2 != 0:
        rage_num = rage_num - 32
    print("{}".format(chr(rage_num)), end="")
