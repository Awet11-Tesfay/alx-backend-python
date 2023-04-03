#!/usr/bin/env python3
""" Description: asyncronous coroutine that takes in an interge
    Arguments: max_delay, int default value, x as random generated float
"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:

    x =random.uniform(0, max_delay)
    """ Used to generate random float between 0 and max_delay """
    
    await asyncio.sleep(x)
    """ to delay for amount of that time """
    return x