#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = ""
    for key, val in a_dictionary.items():
        if val == value:
            todel = key
    if todel != "":
        a_dictionary.pop(todel)
    return a_dictionary
