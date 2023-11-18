"""Holds structures for the Carcassonne tileset."""

import csv
from pathlib import Path
from typing import Any

import numpy as np

# The constant T is the size of the Carcassonne tileset
T = 113

Array = Any

def load_tiles() -> tuple[Array, Array]:
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
