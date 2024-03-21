#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for itr in matrix:
        new.append(list(map(lambda x: x * x, itr)))
    return new
