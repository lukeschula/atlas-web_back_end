#!/usr/bin/env python3
"""task 0"""
import random
from typing import Generator
import asyncio


async def async_generator() -> Generator[float, None, None]:
    """ loop 10 times, wait 1 second,yield a random #"""
    for _ in range(0, 10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
