#!/usr/bin/env python3
"""task 4"""
from typing import List
import asyncio
task_wait_random = __import__('0-basic_async_syntax').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_random is being called."""
    DL = await asyncio.gather(*(task_wait_random(max_delay) for _ in range(n)))
    for i in range(len(DL)):
        for j in range(i + 1, len(DL)):
            if DL[i] >= DL[j]:
                DL[i], DL[j] = DL[j], DL[i]
    return DL
