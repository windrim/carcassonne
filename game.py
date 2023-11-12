import sys

import pygame

WIDTH = 2000
HEIGHT = 2000

pygame.init()

screen = pygame.display.set_mode([WIDTH, HEIGHT])

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Load example image from file
    img = pygame.image.load("tiles/Road0.png")
    img = pygame.transform.scale(img, (1000, 1000))

    # Fill the background with white
    screen.fill((0, 0, 0))

    # Draw image
    screen.blit(img, (0, 0))

    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
sys.exit()
