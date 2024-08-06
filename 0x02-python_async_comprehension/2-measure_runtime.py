#!/usr/bin/env python3
'''
import async_comprehension -> a
write measure_runtime coroutine to execute a 4 times
'''

import asyncio
import time


async def measure_runtime() -> float:
    '''
    runs async_comprehension 4 times in parallel
    returns the total runtime
    '''

    async_com = __import__('1-async_comprehension').async_comprehension
    start_time = time.time()

    async def task1():
        await async_com()

    async def task2():
        await async_com()

    async def task3():
        await async_com()

    async def task4():
        await async_com()

    await asyncio.gather(task1(), task2(), task3(), task4())

    end_time = time.time()

    return end_time - start_time
