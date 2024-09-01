#!/usr/bin/env python3

from typing import List
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:

    delay = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    for i in range(len(delay)):
        for j in range(i + 1, len(delay)):
            if delay[i] >= delay[j]:
                delay[i], delay[j] = delay[j], delay[i]
    return delay
