#!/usr/bin/env python3
''' Description: Import wait_random from the previous python file
         you have written and write an async routine
    Arguments: n: int, max_delay: int = 10
    Returns: Lis: sorted list of delays as float
'''

import asyncio
import random
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    ''' waits for random delay until max_delay '''
    return sorted([await wait_random(max_delay) for i in range(n)])
