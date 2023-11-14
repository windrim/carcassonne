import random
from dataclasses import dataclass
from enum import IntEnum
from typing import Any, Literal

import numpy as np

# Enums didn't work out here lmao
NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3
Direction = Literal[0, 1, 2, 3, 4]

@dataclass(slots=True)
class Square:
    """Representation of one square on the grid.
    - tile index; -1 if empty
    - domain of possible values in this position, as bit array of length t

    Note that Squares have entropy, but these are stored in a separate array
    for faster searching/updating."""

    value: int
    domain: Any


def choose_value(square: Square) -> int:
    """Given Square, pick a random legal choice of value."""
    # TODO: add weights etc
    indices_of_possible = np.argwhere(square.domain == 1)
    return random.choice(indices_of_possible)


def neighbour_coords(i: int, j: int, n: int, m: int, direction: int) -> tuple[int, int]:
    """Returns co-ordinates of neighbour, given direction. Returns -1, -1 if
    square @ [i, j] has no neighbour in that direction."""
    k, l = -1, -1
    match direction:
        case 0:
            if j != 0:
                k, l = i, j - 1
        case 1:
            if i != n:
                k, l = i + 1, j
        case 2:
            if j != m:
                k, l = i, j + 1
        case 3:
            if j != 0:
                k, l = i - 1, j
    return k, l

def constrain(
    grid: Any,
    entropies: Any,
    tileset: Any,
    i: int,
    j: int,
    direction: int
) -> bool:
    """Checks and maybe constrains possible values for given Square at [i, j], which 
    is adjacent to some collapsed or constrained Square, in the provided direction. 

    # Propagating Constraints
    
    E.g., we collapse/constrain a square and check if its north neighbour should also
    be constrained. We then give the co-ordinates corresponding to that neighbour, and
    the north direction to this function.
    
    Returns True if square was constrained, signalling we must check all *this* square's
    neighbours for constraint too. This creates a "wave" (??) of constrain() calls that 
    propagates over the original, collapsed square's nearby neighbours. 

    # Constraining

    When this is called, we know either that the antecedent square has changed its domain.
    This can mean it was collapsed, i.e. domain_n = 1, or just constrained to a lower amount.

    In this case, we check if this square's domain must also be constrained. For example,
    if the antecedent tile now shares only road or city edges with this square, we can't
    have tiles with a grass edge on that side.

    """

    # TODO: refactor to a standard co-ord type
    # TODO: pass co-ord pairs for both antecedent and current to this
    # TODO: do some linalg to update the range of current, using range
    # of ante, with tileset somehow in between ...

    constrained = False

    # Square we will constrain, a neighbour (of 1 or more steps away) of the
    # one we just collapsed
    square = grid[i][j]

    # Direction of antecedent square
    ante_dir = (direction + 2) % 4
    ante_cords = neighbour_coords(i, j, len(grid), len(grid[0]), ante_dir)
    ante = grid[i][j]

    breakpoint()

    return constrained
    
