#!/usr/bin/env python3
''' Description: create a measure time function with integers n and max_delay
                 as agruments that measures the total execution
                 time for max_n(n, max_delay)
    Arguments: n: int, max_delay
'''
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Returns execution time for wait_n given n and mex_delay. '''
    start = time()
    run(wait_n(n, max_delay))
    return (time() - start) / n
