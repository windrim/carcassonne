"""This is the basic CLI for the program."""

from argparse import ArgumentParser
from dataclasses import dataclass

from core import main


def cli():
    """CLI entrypoint which actually calls main function."""
    # getting args
    root = ArgumentParser("Carcassonne board generator.")
    root.add_argument("n", type=int, default=20, help="Size of X dimension of board.")
    root.add_argument("m", type=int, default=20, help="Size of Y dimension of board.")

    # passing to main
    main(**vars(root.parse_args()))


if __name__ == "__main__":
    cli()
