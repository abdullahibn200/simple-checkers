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


# -- Functions --

# As the name suggests this draws the board
def draw_board(screen, screen_width, square_size, square_color):
    square_pos_x = square_size
    square_pos_y = 0
    above_square_bw = 0  # Checks if the square above is b/w


    for _ in range(32):
        pygame.draw.rect(
            screen, square_color, (
                square_pos_x, square_pos_y, square_size, square_size
                )
        )

        square_pos_x += square_size * 2

        if square_pos_x > screen_width - square_size:
            square_pos_y += square_size

            if above_square_bw == 0:
                square_pos_x = 0
                above_square_bw = 1
            else:
                square_pos_x = square_size
                above_square_bw = 0



# -- Main loop      --
while True:
    # Checks for events like close & minimize
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    SCREEN.fill(LIGHT_BROWN)

    draw_board(SCREEN, SCREEN_WIDTH, SQUARE_SIZE, DARK_BROWN)

    pygame.display.flip()
