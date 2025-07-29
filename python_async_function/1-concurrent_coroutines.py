#!/usr/bin/env python3
import asyncio
from typing import List
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> List[float]:
    delays = []
    coros = [wait_random(max_delay) for _ in range(n)]
    for coro in asyncio.as_completed(coros):
        delay = await coro
        delays.append(delay)
    return delays

