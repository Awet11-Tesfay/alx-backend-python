#!/usr/bin/env python3
""" Description: async_comprehension is imported from the previous task and
                 and write a measure runtime coroutine that will execute
                 comprehension four times in parralel using asynio
                 total runtime is roughly 10 seconds
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ measure the total run time """
    begin = time.time()
    do = [async_comprehension() for x in range(4)]
    await asyncio.gather(*do)
    finish = time.time()
    return (finish - begin)
