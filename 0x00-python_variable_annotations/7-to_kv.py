#!/usr/bin/python3

'''
to_kv - takes a string k and int or float v
@k: string
@v: int or float
Return - tuple (str, int|float)
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int | float]) -> Tuple[str, float]:
    # return a tuple of string and float

    return ((k, v ** 2))
