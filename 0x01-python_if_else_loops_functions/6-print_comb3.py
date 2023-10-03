#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if j < i or i == j:
            continue
        print(f"{i}{j} ,", end="")
