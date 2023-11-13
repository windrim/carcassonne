import random
from dataclasses import dataclass
from enum import Enum, auto
from typing import Any

import numpy as np


class Direction(Enum):
    """Model of directions in which some square may have a neighbour."""

    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()


@dataclass(slots=True)
class Square:
    """Representation of one square on the grid.
    - tile index; -1 if empty
    - range of possible values in this position, as bit array of length t

    Note that Squares have entropy, but these are stored in a separate array
    for faster searching/updating."""

    value: int
    rang: Any


def choose_value(square: Square) -> int:
    """Given Square, pick a random legal choice of value."""
    # TODO: add weights etc
    indices_of_possible = np.argwhere(square.rang == 1)
    return random.choice(indices_of_possible)


def neighbour_coords(i: int, j: int, n: int, m: int, direction: Direction) -> tuple[int, int] | None:
    """Returns co-ordinates of neighbour, given direction. Returns None if
    square @ [i, j] has no neighbour in that direction."""
    # TODO: this isn't done yet
    match direction:
        case Direction.NORTH:
            if j == 0:
                return None
            return i, j + 1
        case Direction.EAST:
            if i == n:
                return None
            return i + 1, j
        case Direction.SOUTH:
            if j == m:
                return None
            return i + 1, j
        case Direction.WEST:
            if j == 0:
                return None
            return i + 1, j
    
