#!/usr/bin/python3
# 10-best_score.py
def best_score(a_dict):
    return max(a_dict, key=a_dict.get) if a_dict else None
