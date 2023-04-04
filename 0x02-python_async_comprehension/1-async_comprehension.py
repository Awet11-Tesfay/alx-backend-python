#!/usr/bin/env python3
''' Description: import async_generator from the previous task and the
                 write a coroutine called async_comprehensio that
                 takes no arguments The coroutine will collect 10
                 random numbers using an async comprehensing
                 over async_generator, then return the 10 random numbers
'''

import asyncio
from typing import List
import random

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    ''' Return lists '''
    return [x async for x in async_generator()]
