#!/usr/bin/env python3
'''
import async_generator,
write a couroutine async_comprehension
'''

import asyncio
from typing import List


async def async_comprehension() -> List[float]:
    '''
    collect 10 random numbers from async_generator
    return the 10 random numbers
    '''

    async_generator = __import__('0-async_generator').async_generator
    results = [value async for value in async_generator()]
    return results
