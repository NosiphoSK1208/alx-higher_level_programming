#!/usr/bin/python3
# 102-complex_delete.py
def complex_delete(dictio, value):
    """Delete keys with a specific value in a dictionary."""
    while value in dictio.values():
        for k, v in dictio.items():
            if v == value:
                del dictio[k]
                break

    return (dictio)
