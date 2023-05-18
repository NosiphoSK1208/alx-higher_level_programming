#!/usr/bin/python3
# 1-search_replace.py
def search_replace(my_list, search, replace):
    create_list = my_list[:]
    for i in range(len(create_list)):
        if create_list[i] == search:
            create_list[i] = replace
    return (create_list)

