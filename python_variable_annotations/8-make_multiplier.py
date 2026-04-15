#!/usr/bin/env python3
"""Module for creating a multiplier function."""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Return a function that multiplies a float by multiplier."""

    def inner(x: float) -> float:
        """Multiply input by the captured multiplier."""
        return x * multiplier

    return inner
