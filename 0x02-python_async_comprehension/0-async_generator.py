#!/usr/bin/env python3
''' Description: write a coroutine called async_generator
                 takes no arguments and the coroutine will loop 10 times
                 each time asynchronously wait 1 second then yield a random
                 number betwen(0, 10)
'''

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    ''' Generator[float, None, None]'''
    for x in range(10):
        await asyncio.sleep(1)
        yield 10 * random.random()
