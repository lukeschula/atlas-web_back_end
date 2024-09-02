#!/usr/bin/env python3
"""task 1"""

from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """collect 10 random #'s,  return the 10 random #'s"""
    return [num async for num in async_generator()]
