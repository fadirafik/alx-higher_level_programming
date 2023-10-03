#!/usr/bin/python3
def remove_char_at(str, n):
    i = 0
    cpy = ""
    for s in str:
        if i != n:
            cpy += str[i]
        i += 1
        return cpy
