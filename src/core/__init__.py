import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from random import choice

import numpy as np
from numpy._typing import ArrayLike

# number of possible tiles
T = 113


def load_tiles() -> tuple[ArrayLike, ArrayLike]:
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


@dataclass(slots=True)
class Square:
    """Representation of one square on the grid.
    - empty or not
    - tile index if not empty
    - range of possible values in this position, as bit array of length t

    Note that Squares have entropy, but these are stored in a separate array
    for faster searching/updating."""

    empty: bool
    value: int
    rang: ArrayLike


def create_grid(n: int, m: int, t: int) -> ArrayLike:
    """Initializes the grid as NxM, each element being an empty Square "struct"."""
    return np.array(
        [
            [Square(empty=True, value=-1, rang=np.ones(t)) for _ in range(m)]
            for _ in range(n)
        ]
    )


def create_entropy_grid(n: int, m: int) -> ArrayLike:
    """Initializes entropy grid as NxM, each element being the maximum starting entropy, T."""
    return np.array([[T for _ in range(m)] for _ in range(n)])


def select_from_lowest(grid: ArrayLike) -> tuple[int, int]:
    """Returns an [i, j] co-ordinate on the grid to collapse, which was
    among the lowest entropy squares. Creates entropy array first."""
    lowest = lowest_entropy(grid)
    return lowest[choice(range(len(lowest)))]


def lowest_entropy(grid: ArrayLike) -> ArrayLike:
    """Returns an array of [i, j] co-ordinates (s) in the entropy grid. These
    co-ordinates correspond to Squares in the main grid."""
    lowest = np.min(grid)
    return np.argwhere(grid == lowest)


def main(n: int, m: int) -> None:
    """Full runtime of the board generator."""
    # loading data from file
    files, meta = load_tiles()

    # initializing grids
    grid = create_grid(n, m, T)
    entropies = create_entropy_grid(n, m)

    # getting lowest entropy in grid
    to_collapse = select_from_lowest(entropies)

    breakpoint()


if __name__ == "__main__":
    # getting NxM dimensions of board
    N, M = sys.argv[1:]

    # main runtime
    main(int(N), int(M))
