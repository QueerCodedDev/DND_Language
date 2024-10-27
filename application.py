import pygame
import csv

# Load face font data
font = ['smile', ' frown']

# Load csv font data
with open('font.csv', newline='') as csvfile:
    buffer = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in buffer:
        font.append(row)

print(font[0])

# Load special character font data
font_special = [
    ['.', 'WA:AD:WS'],
    [',', 'WA:AD:WD:WS'],
    [':', 'WA:AD:DS:SW'],
    [';', 'WA:AS:AD:WS'],
    ['+', 'AD:DW:WS'],
    ['-', 'WS:SD:DW:AD'],
    ['*', 'WS:SA:AD:DW'],
    ['/', 'WS:SA:AD:SD'],
    ['(', 'WS:AD'],
    [')', 'WS:AD:AS'],
    ['=', 'WD:DS:SA:AW:WS:AD']
]

# Add special characters to main list
font.extend(font_special)

# Define positions
W = (0,  0)
A = (0, -1)
S = (1, -1)
D = (1,  0)

STROKES = {
    'WA': [W, A],
    'WS': [W, S],
    'WD': [W, D],
    'DA': [D, A],
    'DS': [D, S],
    'SA': [S, A]
}

print(STROKES['WA'])

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width = 400
screen_height = 400
cell_size = 25  # Size of each grid cell

# Colors
white = (255, 255, 255)
black = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Rendering")


def draw_grid():
    """Draws a grid on the screen."""
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (screen_width, y))


def render_character(character_lines, grid_x, grid_y):
    """Renders a character defined by lines within a grid cell.

    Args:
        character_lines: A list of lines, where each line is a tuple of
                         two coordinate pairs: ((start_x, start_y), (end_x, end_y)).
                         Coordinates are within the 4-coordinate system (0, 1, -1).
        grid_x: The x-coordinate of the grid cell to render in.
        grid_y: The y-coordinate of the grid cell to render in.
    """
    for line in character_lines:
        start_x = grid_x * cell_size + line[0][0] * cell_size
        start_y = grid_y * cell_size - line[0][1] * cell_size
        end_x = grid_x * cell_size + line[1][0] * cell_size
        end_y = grid_y * cell_size - line[1][1] * cell_size
        pygame.draw.line(screen, black, (start_x, start_y), (end_x, end_y), 3)


# Define the character 'L' with the corrected coordinates
character_L = [
    [(0, 0), (1, -1)],
    [(1, 0), (1, -1)],
    [(0, -1), (1, -1)]
]

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(white)
    draw_grid()
    render_character(character_L, 0, 0)  # Render 'L' at grid position (0, 0) - top left

    pygame.display.flip()

pygame.quit()
