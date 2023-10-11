#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    matrix2 = []
    for i in matrix:
        x = []
        matrix2.append(x)
        for row in i:
            x.append(row ** 2)
    return matrix2
