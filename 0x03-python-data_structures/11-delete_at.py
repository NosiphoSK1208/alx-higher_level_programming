#!/usr/bin/python3
# 11-delete_at.py

def delete_at(mylist=[], ids=0):
    if ids >= 0 and ids < len(mylist):
        del mylist[ids]
    return (mylist)
