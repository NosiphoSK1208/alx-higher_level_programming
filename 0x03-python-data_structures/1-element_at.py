#!/usr/bin/python3
# 1-element_at.py
def element_at(element_list, int_ids):
    return(element_list[int_ids] if 0 <= int_ids < len(element_list) else "None")
