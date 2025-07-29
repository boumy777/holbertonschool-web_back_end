#!/usr/bin/env python3
import time
import asyncio
from 1_concurrent_coroutines import wait_n

def measure_time(n: int, max_delay: int) -> float:
    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    return (end - start) / n

