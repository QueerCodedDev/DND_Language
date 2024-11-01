import pygame

from const.colors import BLACK
from uti.code_message import code_message
from uti.render_character import render_character

# Initialize Pygame
pygame.init()

# Screen dimensions
cell_size: int = 16  # Size of each grid cell
screen_width: int = cell_size * 16
screen_height: int = cell_size * 16

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Rendering")

# Retrieve input
file_name: str = 'res/test_file.txt'
with open(file_name, 'r+') as file:
    message: str = file.read()

print(message)
# History of lines for rendering styling
stroke_history: list[dict[str, int]] = []

# Main loop
running: bool = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BLACK)
    # draw_grid(screen, screen_width, screen_height, cell_size)

    # Positional variables
    i: int = 1
    j: int = 1
    increment: int = 1
    horizontal_limit: int = 10

    message_code: list[str] = code_message(message)
    stroke_history = []
    for m in message_code:
        if m == 'smile' or m == 'frown':
            continue
        else:
            if m != ' ':
                render_character(screen, stroke_history, m, i, j)
            i += increment
            if i > horizontal_limit:
                j += increment
                i = 1

    # print(stroke_history)

    pygame.display.flip()
    # running = False

pygame.quit()
