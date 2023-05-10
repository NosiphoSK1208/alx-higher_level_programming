#!/usr/bin/python3
# 101-remove_char_at.py


def remove_char_at(word_string, n):
    if n < 0:
        return (word_string)
    return (word_string[:n] + word_string[n+1:])
