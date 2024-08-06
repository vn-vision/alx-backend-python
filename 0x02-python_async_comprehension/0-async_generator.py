#!/usr/bin/env python3
'''
coroutine async_generator with no arguments
loops 10 times, each asynchrously wait 1 second,
yields a random number between 0 and 10
'''

import asyncio
import random
from typing import AsyncGenerator

async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Takes no arguments, loops 10 times yielding
    a random number between 0 - 10
    returns float, takes no arguments
    '''

    for i in range(10):
        await asyncio.sleep(1) # simulate an asynchronous operation
        yield random.uniform(0, 10) # generate a random no 0-10
