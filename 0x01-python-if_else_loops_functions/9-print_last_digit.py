#!/usr/bin/python3
def print_last_digit(number):
    last = int(str(number)[-1])
    print(f"{last :d}", end="")
    return(last)
