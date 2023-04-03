#!/usr/bin/env python3
''' Description: asyncronous coroutine that takes in an interger
        and named wait_random that waits for random delay
    Arguments: max_delay: int = 10
    Returns: x
'''

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    x = random.uniform(0, max_delay)
    ''' Used to generate random float between 0 and max_delay '''
    await asyncio.sleep(x)
    ''' to delay for amount of that time '''
    return x
