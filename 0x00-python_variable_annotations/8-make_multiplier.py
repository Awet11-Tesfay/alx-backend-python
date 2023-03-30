#!/usr/bin/env python3
''' Description: function that takes float and
        returns a function that multiplies afloat by multiplier
    Argument: multiplier: float
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Returns function that multiplies float by multiplier'''
    return lambda x: x  * multiplier
