#!/usr/bin/env python3

'''
element_length - takes lst
@lst: Iterable with Sequence
Returns - list
'''
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
