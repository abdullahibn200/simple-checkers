import pygame
import sys


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LIGHT_BROWN = (255, 241, 199)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(LIGHT_BROWN)
    pygame.display.flip()
