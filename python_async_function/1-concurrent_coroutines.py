#!/usr/bin/env python3
import asyncio
from 0_basic_async_syntax import wait_random

async def wait_n(n: int, max_delay: int) -> list[float]:
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results = []
    # as_completed permet de récupérer les résultats dès qu'ils sont prêts (ordre ascendant de temps)
    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)
    return results

