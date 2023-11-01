#!/usr/bin/python3
"""


module of text indentation


"""


def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i in text:
        if i == "." or i == "?" or i == ":":
            print("{:s}".format(i))
            print("")
        else:
            print("{:s}".format(i), end="")
