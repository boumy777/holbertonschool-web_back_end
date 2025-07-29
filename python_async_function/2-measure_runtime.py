#!/usr/bin/env python3
import time
from typing import Union
from 1_concurrent_coroutines import wait_n
import asyncio

def measure_time(n: int, max_delay: int) -> float:
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = time.perf_counter()
    total_time = end - start
    return total_time / n

