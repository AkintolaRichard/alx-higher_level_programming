#!/usr/bin/python3
def square_matrix_map(my_list=[]):
    return list(map(lambda x: list(map(lambda y: y * y, x)), my_list))
