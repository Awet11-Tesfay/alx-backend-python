#!/usr/bin/env python3
''' Description: function which takes alist of integers and floats and 
    return their sum as float
    Arguments: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Returns a Union of integers and float'''
    return sum(mxd_lst)