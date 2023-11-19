"""This module holds the PyGame graphic frontend for the core architecture."""
import time
from typing import Any

import pygame

from core import Array
from core import main as core_main
from core.grid import Dimensions

WIDTH = 2000
HEIGHT = 2000


def tile_size(dims: Dimensions, width: int, height: int) -> tuple[int, int]:
    """Given NxM dimensions of grid, and the display width and height,
    returns the WxL dimensions of one square in the grid."""

    return width // dims.N, height // dims.M


def load_images(files: Array, xl: int, yl: int) -> dict[int, Any]:
    """Loads and scales all images from file at start of run."""
    images = {}
    for i, file in enumerate(files):
        img = pygame.image.load(file)
        img = pygame.transform.scale(img, (xl, yl))
        images[i] = img
    return images


def draw(
    screen, dims: Dimensions, xl: int, yl: int, grid: Array, images: dict[int, Any]
) -> None:
    """Draws the screen as one "frame"."""

    for i, x in enumerate(range(0, WIDTH, xl)):
        for j, y in enumerate(range(0, HEIGHT, yl)):
            if (val := grid[i][j]) != -1:
                screen.blit(images[val], (x, y))


def game(dims: Dimensions):
    """This holds the main event loop for the graphics."""

    pygame.init()

    # screen setup
    pygame.display.set_caption("Carcassonne")
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    # starting wfc algorithm
    boards = core_main(dims)

    # first result of boards is the filelist
    files = next(boards)

    # size of tiles given dims and screen
    xl, yl = tile_size(dims, WIDTH, HEIGHT)

    # loading images from file
    images = load_images(files, xl, yl)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

        # getting next board state
        grid = next(boards)
        draw(screen, dims, xl, yl, grid, images)

        pygame.display.flip()

    # exiting when loop stops on QUIT condition
    pygame.quit()
