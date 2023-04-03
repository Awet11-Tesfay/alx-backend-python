#!/usr/bin/env pyhon3
''' Description: create a measure time function with integers n and max_delay
                 as agruments that measures the total execution 
                 time for max_n(n, max_delay)
    Arguments: n: int, max_delay: int
'''
from time import time
from asyncio import run
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Returns execution time for wait_n given n and mex_delay. '''
    time_1 = time()
    run(wait_n(n, max_delay))
    time_2 = time()
    elipsed = time_2 - time_1
    return elipsed / n