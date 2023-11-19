"""Holds the logic of the wave function collapse algorithm."""
import time
from queue import LifoQueue
from random import choice
from typing import Any

import numpy as np

from .grid import Dimensions, Grids, Point, neighbour
from .tiles import T

Array = Any


def choose_collapse(entropies: Array) -> Point | None:
    """Chooses square to collapse by random choice of minimum values in entropies grid.
    Returns its Point."""
    lowest_entropy = np.min(entropies)
    if lowest_entropy == T + 1:
        return None
    lowest_tiles = np.argwhere(entropies == lowest_entropy)
    return Point(*lowest_tiles[choice(range(len(lowest_tiles)))])


def collapse(point: Point, grids: Grids) -> None:
    """Collapes the given point, updating three grids."""

    # TODO: add weights etc

    # selecting random value from domain
    value = np.random.choice(np.where(grids.domains[point.x][point.y] == 1)[0])

    # updating grids
    grids.values[point.x][point.y] = value
    grids.entropies[point.x][point.y] = T + 1
    grids.domains[point.x][point.y] = np.zeros(T)
    grids.domains[point.x][point.y][value] = 1


def constrain(
    point: Point, npoint: Point, direction: int, grids: Grids, tileset: Array
) -> bool:
    """Checks and sometimes constrains the `npoint` given the state of the antecedent `point`.
    Returns True if the point was constrained, i.e. the domains subarray was reduced.

    This function is called when `point` has just been collapsed or constrained. As a result,
    `npoint` -- its neighbour in the `direction` int -- may need constraining.

    E.g., if `point` is now is 0R, `npoint` may only have 2R in its domain. Or, if point has
    no values but no 3G in its domain, `npoint` may have no 1G in its domain.

    This *ONLY FLIPS 0 OR MORE 1s* in the neighbours domain, and does so only considering a single
    direction, since the directions are independent and the provided direction is the only change
    since this tile's domain was last updated (instantiation, collapse or previous constrain).
    """

    ant = grids.domains[point.x][point.y]
    con = grids.domains[npoint.x][npoint.y]

    # calculating the side relative to b, not a
    ant_dir = direction
    con_dir = (ant_dir + 2) % 4

    # all terrain types {0, 1, 2} in the domain a, in the direction a_dir
    possible_terrains = tileset[ant == 1, ant_dir]

    # all items in the domain which are no longer possible; i.e., indices of items in
    # the domain which are 1 but which match tiles whose b_dir side is not in the possible
    # terrains
    impossible_tiles = ~np.isin(tileset[:, con_dir], possible_terrains)

    # flipping setting all impossible tiles to 0 in the domain
    con[impossible_tiles] = 0

    return impossible_tiles.any()


def wfc(grids: Grids, dims: Dimensions, tileset: Array) -> int:
    """This collapses one tile and propagates constraints. It is called continuously
    until all tiles are collapsed, when this function returns 1."""

    #
    # (1) COLLAPSING:
    #

    # choose tile to collapse
    to_collapse = choose_collapse(grids.entropies)
    # we stop if we find no more points to collapse
    if not to_collapse:
        return 1

    # collapsing chosen tile
    collapse(to_collapse, grids)
    print(f"collapsing {to_collapse}")

    #
    # (2) PROPAGATING CONSTRAINTS:
    #

    # we check neighbours of the collapsed point in stack-order, i.e. in something like
    # depth-first if the point connections were a graph
    stack = LifoQueue()
    stack.put(to_collapse)

    while not stack.empty():
        point = stack.get()
        print(f"updating point {point}")

        # checking all neighbours (by direction) of the given point
        for direction in range(4):
            npoint = neighbour(point, direction, dims)
            if npoint and grids.entropies[npoint.x][npoint.y] < T + 1:
                constrained = constrain(point, npoint, direction, grids, tileset)
                if constrained:
                    stack.put(npoint)
    return 0
