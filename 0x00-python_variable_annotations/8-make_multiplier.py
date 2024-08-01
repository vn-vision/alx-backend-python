#!/usr/bin/env python3

'''
make_multiplier - takes a multiplier
@muliplier: float
Returns - function that multiplies a float by multiplier
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' return multiplier with float '''
    def mul_value(value: float) -> float:
        # multiply a float with the multiplier
        return (value * multiplier)

    return mul_value
