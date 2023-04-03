#!/usr/bin/env python3
''' Description: write a funcion do not create an async funcion use the
                 regular function syntax to do this
                 task_wait_random that takes an integer
    Arguments: max_delay: int
'''

from asyncio import create_task, Task

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 10) -> Task:
    return create_task(wait_random(max_delay))
