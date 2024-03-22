#!/usr/bin/python3

def weight_average(my_list=[]):
    length = len(my_list)
    if length == 0:
        return 0
    total = 0
    denom = 0
    for i in range(length):
        total += my_list[i][0] * my_list[i][1]
        denom += my_list[i][1]
    return total / denom
