#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dick = {}
    for key, val in a_dictionary.items():
        new_dick[key] = val * 2
    return new_dick
