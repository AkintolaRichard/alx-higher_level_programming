#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    dict_copy = a_dictionary.copy()
    for k, v in dict_copy.items():
        dict_copy[k] *= 2
    return dict_copy
