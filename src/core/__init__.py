import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from queue import LifoQueue
from random import choice
from typing import Any, Literal

import numpy as np
from square import Direction, Square, choose_value

# number of possible tiles
T = 113


def load_tiles() -> tuple[Any, Any]:
    """Loads tiles and metadata from data/tiles/ data/tiles.csv. Returns two
    arrays: first is filenames of tiles; second is 2d array of the NESW joining
    types of each tile.

    Runs once at startup."""

    fns: list[Path] = []
    sides: list[list[int]] = []
    static_path = Path("data/tiles/")
    with open("data/tiles.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            fns.append(static_path / row[0])
            sides.append([int(x) for x in row[1:]])

    return np.array(fns), np.array(sides)


def create_grid(n: int, m: int, t: int) -> Any:
    """Initializes the grid as NxM, each element being an empty Square "struct"."""
    return np.array(
        [[Square(value=-1, rang=np.ones(t)) for _ in range(m)] for _ in range(n)]
    )


def create_entropy_grid(n: int, m: int) -> Any:
    """Initializes entropy grid as NxM, each element being the maximum starting entropy, T."""
    return np.array([[T for _ in range(m)] for _ in range(n)])


def choose_collapse(entropies: Any) -> tuple[int, int]:
    """Chooses square to collapse by random choice of minimum
    values in entropies grid. Returns its [i, j] co-ordinate."""
    lowest_entropy = np.min(entropies)
    if lowest_entropy == T + 1:
        return -1, -1
    lowest_tiles = np.argwhere(entropies == lowest_entropy)
    return lowest_tiles[choice(range(len(lowest_tiles)))]


def collapse(i: int, j: int, grid: Any, entropies: Any) -> None:
    """Collapses the Square at [i, j]."""
    # upading entropy to impossible value
    entropies[i][j] = T + 1

    # updating square to a random choice
    square = grid[i][j]
    square.value = choose_value(square)


def wave_function_collapse(grid: Any, entropies: Any) -> Literal[0, 1]:
    """Main algorithm. Eventually runs once per all tiles in grid. Returns 1 when grid completed,
    else 0.

    - find lowest entropy tile(s)
    - return code 1 if no tiles with positive entropy
    - collapse random tile from those with lowest entropy
    """
    # co-ordinates of tile to collapse
    i, j = choose_collapse(entropies)
    # quitting on -1 signal, i.e. no choices
    if i == -1:
        return 1

    # collapsing tile
    collapse(i, j, grid, entropies)

    # stack for squares affected by collapse which now must be updated
    stack = LifoQueue()

    # adding most recent, collapsed tile to stack
    stack.put(grid[i][j])

    # co-ordinates of last processed square
    k, l = i, j

    # updating each square and its neighbours
    while not stack.empty():
        square = stack.get()

        for direction in Direction:
            ni, nj = ...
            breakpoint()

    return 0


def main(n: int, m: int) -> None:
    """Full runtime of the board generator."""
    # loading data from file
    # files, meta = load_tiles()

    # initializing grids
    grid = create_grid(n, m, T)
    entropies = create_entropy_grid(n, m)

    # collapsing tiles until seeing exit signal
    while True:
        res = wave_function_collapse(grid, entropies)
        if res == 1:
            break


if __name__ == "__main__":
    # getting NxM dimensions of board
    N, M = sys.argv[1:]

    # main runtime
    main(int(N), int(M))
