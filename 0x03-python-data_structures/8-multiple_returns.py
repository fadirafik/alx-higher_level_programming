#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        firstch = None
    else:
        firstch = sentence[0]
    length = len(sentence)
    return length, firstch
