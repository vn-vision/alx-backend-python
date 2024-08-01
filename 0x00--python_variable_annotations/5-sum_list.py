#!/usr/bin/python3
'''
sum_list - takes a list input_list
@input_list: list of floats
Returns: sum as float
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    # add the floats in the list and return their sum

    list_sum: float = 0
    for n in input_list:
        list_sum = list_sum + n

    return list_sum
