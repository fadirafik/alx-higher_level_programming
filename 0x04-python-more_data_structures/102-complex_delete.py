#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = []
    for key, val in a_dictionary.items():
        if val == value:
            todel.append(key)
    if len(todel) != 0:
        for i in todel:
            a_dictionary.pop(todel[todel.index(i)])
    return a_dictionary
