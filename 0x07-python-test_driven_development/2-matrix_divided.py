#!/usr/bin/python3
"""


module for dividing matrices


"""


def matrix_divided(matrix, div):
    """

    matrix division bt divisor

    """
    j = 0
    c = 0
    sizerows = len(matrix[0])
    newmatrix = []
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    if len(matrix) == 1 and isinstance(matrix[0], int):
        newmatrix.append(matrix[0]/div)
        return newmatrix
    for row in matrix:
        newlist = []
        if len(row) != sizerows:
            raise TypeError("Each row of the matrix must have the same size")
        for i in row:
            if not isinstance(i, (int, float)):
                raise TypeError\
                    ("matrix must be a matrix (list of lists) of integers/floats")
            newlist.append(round(i/div, 2))
            c += 1
        newmatrix.append(newlist)
        j += 1
        c = 0
    return newmatrix
