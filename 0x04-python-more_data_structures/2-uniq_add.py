#!/usr/bin/python3


def uniq_add(my_list=[]):
    summation = 0
    for i in set(my_list):
        summation += i
    return (summation)
