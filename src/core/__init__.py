from .grid import Dimensions, create_grids
from .tiles import load_tiles
from .wfc import wfc


def main(n: int, m: int) -> None:
    """Full runtime of the board generator."""
    # loading data from file
    files, tileset = load_tiles()

    # dimensions
    dims = Dimensions(n, m)

    # initializing grids
    grids = create_grids(dims)

    # collapsing tiles until seeing exit signal
    while True:
        res = wfc(grids, dims, tileset)
        if res == 1:
            break
