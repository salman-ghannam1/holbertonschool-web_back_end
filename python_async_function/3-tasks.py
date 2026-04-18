#!/usr/bin/env python3
"""
This module creates asyncio tasks from coroutines.
"""

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Returns an asyncio.Task that executes wait_random.
    """
    return asyncio.create_task(wait_random(max_delay))
