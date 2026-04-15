#!/usr/bin/env python3
"""Module for getting element lengths from an iterable."""

from typing import Iterable, Tuple, List, Sized


def element_length(
    lst: Iterable[Sized]
) -> List[Tuple[Sized, int]]:
    """Return a list of tuples with each element and its length."""
    return [(i, len(i)) for i in lst]
