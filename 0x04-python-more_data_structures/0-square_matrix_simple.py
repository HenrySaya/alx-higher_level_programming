#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_matrix = []
    for row in matrix:
        new_row = list(map(lambda col: col * col, row))
        new_matrix.append(new_row)
    return new_matrix
