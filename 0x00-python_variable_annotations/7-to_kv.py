#!/usr/bin/env pyhon3
''' Description: takes a string K and an int OR float v as arguments and
        returns a tuple. the first element of the tuple is the
        string K.
        The second element is the square of the int/float V and 
        should be annotated as a float.
    Arguments: K str, v: Union[int, float]
'''

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    ''' Return Tuple consisting of k and the square of v'''
    return (k, v**2)
