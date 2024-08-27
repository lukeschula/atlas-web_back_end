#!/usr/bin/env python3
""" sum_mixed_list which takes a list mxd_lst of integers and floats """
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[float, int]]) -> float:
    """take list and returns sum"""
    return sum(mxd_lst)
