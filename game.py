import sys
from random import randint

import pygame

WIDTH = 2000
HEIGHT = 2000


def square_size(n: int, m: int, width: int, height: int) -> tuple[int, int]:
    """Given NxM dimensions of grid, and the display width and height,
    returns the WxL dimensions of one square in the grid."""

    return width // n, height // m


def draw_grid(
    screen, n: int, m: int, xsize: int, ysize: int, width: int, height: int
) -> None:
    for x in range(n, width, xsize):
        for y in range(m, height, ysize):
            rect = pygame.Rect(x, y, xsize, ysize)
            pygame.draw.rect(
                screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect
            )


def main(n: int, m: int):
    """Main loop of game, taking board dimensions as arguments."""
    pygame.init()

    screen = pygame.display.set_mode([WIDTH, HEIGHT])
    screen.fill((0, 0, 0))

    size = square_size(n, m, WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

        draw_grid(screen, n, m, size[0], size[1], WIDTH, HEIGHT)

        pygame.display.flip()

    # exiting when loop stops on QUIT condition
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    # TODO: cli
    N = 20
    M = 20
    main(N, M)
