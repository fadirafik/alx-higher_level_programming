#!/usr/bin/python3

def best_score(a_dictionary):
    max = 0
    winner = ""
    if a_dictionary:
        for key, val in a_dictionary.items():
            if max < val:
                max = val
                winner = key
        return winner
    else:
        return None
