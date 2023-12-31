from typing import Any, Generator

from .grid import Dimensions, create_grids
from .tiles import load_tiles
from .wfc import wfc

Array = Any


def main(dims: Dimensions) -> Generator[Array, None, None]:
    """Full runtime of the board generator."""

    # loading data from file
    _, tileset = load_tiles()

    # initializing grids
    grids = create_grids(dims)

    # collapsing tiles until seeing exit signal
    while True:
        res = wfc(grids, dims, tileset)
        if res == 1:
            break
        # continually yielding values array for render
        yield grids.values

    # yielding none to signal end of run
    yield
