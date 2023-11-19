"""This is the basic CLI for the program."""

from argparse import ArgumentParser
from dataclasses import dataclass

from core.grid import Dimensions
from game import game


def cli():
    """CLI entrypoint which actually calls main function."""
    # getting args
    root = ArgumentParser("Carcassonne board generator.")
    root.add_argument("n", type=int, default=20, help="Size of X dimension of board.")
    root.add_argument("m", type=int, default=20, help="Size of Y dimension of board.")

    args = vars(root.parse_args())
    dims = Dimensions(N=args["n"], M=args["m"])

    # starting pygame
    game(dims)


if __name__ == "__main__":
    cli()
