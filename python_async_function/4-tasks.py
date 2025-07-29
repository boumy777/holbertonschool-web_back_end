#!/usr/bin/env python3
import asyncio
from 3_tasks import task_wait_random

async def task_wait_n(n: int, max_delay: int) -> list[float]:
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    results = []
    for task in asyncio.as_completed(tasks):
        res = await task
        results.append(res)
    return results

