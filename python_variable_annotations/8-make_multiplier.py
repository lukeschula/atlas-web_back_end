#!/usr/bin/env python3
"""takes a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float"""
    def multiplier_function(value: float) -> float:
        return value * multiplier
    return multiplier_function
