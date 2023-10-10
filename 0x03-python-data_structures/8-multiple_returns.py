#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        firstch = None
    firstch = sentence[0]
    length = len(sentence)
    return length, firstch
