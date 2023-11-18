"""Holds the logic of the wave function collapse algorithm."""
from dataclasses import dataclass
from queue import LifoQueue
from random import choice
from typing import Any

import numpy as np

from .grid import Dimensions, Direction, Grids, Point, neighbour
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


# TODO
def collapse(point: Point, grids: Grids) -> None:
    """Collapes the given point, altering the provided arrays."""


# TODO
def constrain(point: Point, direction: Direction, grids: Grids, tileset: Array) -> int:
    return 0


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

    #
    # (2) PROPAGATING CONSTRAINTS:
    #

    # we check neighbours of the collapsed point in stack-order, i.e. in something like
    # depth-first if the point connections were a graph
    stack = LifoQueue()
    stack.put(to_collapse)

    while not stack.empty():
        point = stack.get()

        # checking all neighbours (by direction) of the given point
        for direction in range(4):
            npoint = neighbour(point, direction, dims)
            if npoint and entropies[npoint.x][npoint.y] < T + 1:
                constrained = constrain(point, direction, grids, tileset)
                breakpoint()
    return 0
