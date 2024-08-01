#!/usr/bin/python3

'''
sum_mixed_list - takes a list mxd_lst
@mxd_lst: list of ints and floats
Returns - sum as float
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    # return sum of numbers in list
    sum_list: float = 0

    for n in mxd_lst:
        sum_list = sum_list + n

    return float(sum_list)
