#!/usr/bin/env python3
''' Description: function which takes alist of integers and floats and 
    return their sum as float
    Arguments: mxd_lst: floats and integers
'''

from typing import List


def sum_mixed_list(mxd_lst: List[int, float]) -> float:
    return sum(mxd_lst)