#!/usr/bin/python3
# 8-multiple_returns.py


def multiple_returns(asentence):
    if asentence == "":
        return (0, None)
    return (len(asentence), asentence[0])
