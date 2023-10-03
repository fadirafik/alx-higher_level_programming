#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j < i or i == j:
            continue
        if j == 9 and i == 8:
            print(" {}{}".format(i, j))
            continue
        print(" {}{},".format(i, j), end="")
