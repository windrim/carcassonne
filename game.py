import sys
import time
from random import randint

import pygame

# colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

WIDTH = 2000
HEIGHT = 2000


def tile_size(n: int, m: int, width: int, height: int) -> tuple[int, int]:
    """Given NxM dimensions of grid, and the display width and height,
    returns the WxL dimensions of one square in the grid."""

    return width // n, height // m


def disco_grid(
    screen, n: int, m: int, xsize: int, ysize: int, width: int, height: int
) -> None:
    """This function shows an example of drawing a grid with randomly coloured squares.
    It uses all the spatial parameters we use in the real setup."""
    for x in range(n, width, xsize):
        for y in range(m, height, ysize):
            rect = pygame.Rect(x, y, xsize, ysize)
            pygame.draw.rect(
                screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect
            )


def draw_grid(
    screen, n: int, m: int, xsize: int, ysize: int, width: int, height: int
) -> None:
    """This function shows an example of drawing a grid with randomly coloured squares.
    It uses all the spatial parameters we use in the real setup."""

    font = pygame.font.Font(None, 10)
    for x in range(n, width, xsize):
        for y in range(m, height, ysize):
            drawn = randint(0, 1)
            if drawn:
                rect = pygame.Rect(x, y, xsize, ysize)
                pygame.draw.rect(
                    screen, (randint(0, 255), randint(0, 255), randint(0, 255)), rect
                )
            else:
                text = font.render("X", True, WHITE, BLACK)
                text_rect = text.get_rect()
                text_rect.center = x + xsize, y + ysize
                screen.blit(text, text_rect)


def main(n: int, m: int):
    """Main loop of game, taking board dimensions as arguments."""
    pygame.init()

    pygame.display.set_caption("Caracassonne")
    screen = pygame.display.set_mode([WIDTH, HEIGHT])

    screen.fill((0, 0, 0))

    xsize, ysize = tile_size(n, m, WIDTH, HEIGHT)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                continue

        # disco_grid(screen, n, m, size[0], size[1], WIDTH, HEIGHT)
        draw_grid(screen, n, m, xsize, ysize, WIDTH, HEIGHT)

        pygame.display.flip()

    # exiting when loop stops on QUIT condition
    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    N = 100
    M = 100
    main(N, M)
