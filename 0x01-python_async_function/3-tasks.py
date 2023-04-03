#!/usr/bin/env python3
''' Description: write a funcion do not create an async funcion use the
                 regular function syntax to do this
                 task_wait_random that takes an integer
    Arguments: max_delay: int
    Returns: asyncio.Task
'''

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> asyncio.Task:
    return create_task(wait_random(max_delay))
