#!/usr/bin/env python3
''' Description: Take the code from wait_n and alter into
                 new function task_wait_n. The code is nearly identical
    Arguments: n: int, max_delay: int = 10
    Returns: List: soted list
'''
import random
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    return sorted([await task_wait_random(max_delay) for i in range(n)])
