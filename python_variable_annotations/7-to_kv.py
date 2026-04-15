#!/usr/bin/env python3
"""Module for converting key-value to tuple with squared value."""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple with key and squared value as float."""
    return (k, float(v * v))
