#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    sum = 0
    for i in my_list:
        if not (i in new_list):
            new_list.append(i)
    for j in new_list:
        sum += j
    return sum
