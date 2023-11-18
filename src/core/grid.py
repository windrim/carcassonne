"""Structures for the grids used in this program.


values: array[N, array[M, {-1 ... T - 1}]]
entropies: array[N, array[M, {0 ... T - 1}]]
domains: array[N, array[M, array[T, {0, 1}]]]
    
The value grid holds the value at that point, which is -1 if that point has not 
yet been collapsed, and is otherwise a positive integer representing the index 
of the collapsed-to tile in the tileset.   

The domain grid holds a bitfield for every point indicating whether each tile in 
the tileset is possible. Thus it is NxMxT.

The entropy of a point on the grid is the size of its domain. These values
are stored separately from the domain grid for speed only: the WFC algorithm
finds the lowest entropy squares at every iteration, and after a point is collapsed
we set its entropy to T + 1, allowing us to use np.min, which would fail if we
zeroed the collapsed points' entropies.
"""

from dataclasses import dataclass
from typing import Any, Literal

import numpy as np

from .tiles import T

# Cardinal directions as integers. Couldn't really get Enum/IntEnum working
# here.
Direction = Literal[0, 1, 2, 3, 4]

# Couldn't get type hints for numpy arrays working either. This is for semantics.
Array = Any

@dataclass(slots=True, frozen=True)
class Dimensions:
    """Dimensions of the grid(s)."""
    N = int
    M = int

@dataclass(slots=True, frozen=True)
class Point:
    """One point on a grid."""
    x: int
    y: int

@dataclass(slots=True, frozen=True)
class Grids:
    """Container for the three grids in this algorithm."""
    values: Array
    entropies: Array
    domains: Array

def create_grids(dims: Dimensions) -> Grids:
    """Initializes the three grids used in this program."""

    return Grids(
        values=np.array([[-1 for _ in range(dims.M)] for _ in range(dims.N)]),
        entropies=np.array([[T for _ in range(dims.M)] for _ in range(dims.N)]),
        domains=np.array([[np.ones(T) for _ in range(dims.M)] for _ in range(dims.N)]),
    )


def neighbour(point: Point, direction: Direction, dims: Dimensions) -> Point | None:
    """Returns the point's neighbour in the given direction, returning None if no
    such point exists."""
    if direction == 0 and point.y != 0:
        return Point(point.x, point.y - 1)
    if direction == 1 and point.x != dims.N:
        return Point(point.x + 1, point.y)
    if direction == 2 and point.y != dims.M:
        return Point(point.x, point.y + 1)
    if direction == 3 and point.x != 0:
        return Point(point.x - 1, point.y)
    return None
