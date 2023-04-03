#!/usr/bin/env python3
''' Description:async coroutine that takes in an integer argument
                max_delay, with a default value of 10 named  wait_random
                that waits for a random dealy between 0 and max_delay
    Arguments: max_delay: int = 10      
'''

import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    ''' Wait up to max_delay run again and then returns length of the delay '''
    x = random.uniform(0, max_delay)
    await asyncio.sleep(x)
    return x
