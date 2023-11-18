"""Structures for the grid."""

from dataclasses import dataclass
from typing import Any, Literal

import numpy as np

# The constant T is the size of the Carcassonne tileset
T = 113

# Cardinal directions as integers. Couldn't really get Enum/IntEnum working
# here.
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
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


def create_grid(dims: Dimensions) -> Array:
    """Initializes the main grid: array[N, array[M, {-1 ... T - 1}]]

    The main grid holds the value of the tile, which is -1 if that point has not 
    yet been collapsed, and is otherwise a positive integer representing the index 
    of the collapsed-to tile in the tileset."""
    return np.array(
        [[-1 for _ in range(dims.M)] for _ in range(dims.N)]
    )

def create_domains(dims: Dimensions) -> Array:
    """Initializes the domain grid: array[N, array[M, array[T, {0, 1}]]]

    The domain grid holds a bitfield for every point indicating whether each tile in 
    the tileset is possible. Thus it is NxMxT."""
    return np.array(
        [[np.ones(T) for _ in range(dims.M)] for _ in range(dims.N)]
    )


def create_entropies(dims: Dimensions) -> Array:
    """Initializes the entropies grid: array[N, array[M, {0 ... T - 1}]]

    The entropy of a point on the grid is the size of its domain. These values
    are stored separately from the domain grid for speed only: the WFC algorithm
    finds the lowest entropy squares at every iteration."""
    return np.array(
        [[T for _ in range(dims.M)] for _ in range(dims.N)]
    )
