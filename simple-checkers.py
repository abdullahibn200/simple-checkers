import pygame
import sys


pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

WHITE = (255, 255, 255)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(WHITE)
    pygame.display.flip()
