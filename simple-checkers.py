import pygame
import sys

# -- Initialization --
pygame.init()

# -- Constants      --
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 600
SQUARE_SIZE = 75

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

LIGHT_BROWN = (237, 201, 175)
DARK_BROWN = (159, 129, 112)


# -- Main loop      --
while True:
    square_pos_x = SQUARE_SIZE
    square_pos_y = 0
    above_square_occ = 0  # Checks if the square above is occupied

    # Checks for events like close & minimize
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(LIGHT_BROWN)

    # Draws the board
    for i in range(32):
        pygame.draw.rect(
            SCREEN, DARK_BROWN, (square_pos_x, square_pos_y, SQUARE_SIZE, SQUARE_SIZE)
        )

        square_pos_x += SQUARE_SIZE * 2

        if square_pos_x > SCREEN_WIDTH - SQUARE_SIZE:
            square_pos_y += SQUARE_SIZE

            if above_square_occ == 0:
                square_pos_x = 0
                above_square_occ = 1
            else:
                square_pos_x = SQUARE_SIZE
                above_square_occ = 0

    pygame.display.update()
