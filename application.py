import math
import time

import pygame
import csv

font = {}
# Load csv font data
with open('font.csv', newline='') as csvfile:
    buffer = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in buffer:
        font[row[0]] = row[1]

# Load special character font data
font_special = {
    ' ': '',
    '.': 'WA:AD:WS',
    ',': 'WA:AD:WD:WS',
    ':': 'WA:AD:DS:SW',
    ';': 'WA:AS:AD:WS',
    '+': 'AD:DW:WS',
    '-': 'WS:SD:DW:AD',
    '*': 'WS:SA:AD:DW',
    '/': 'WS:SA:AD:SD',
    '(': 'WS:AD',
    ')': 'WS:AD:AS',
    '=': 'WD:DS:SA:AW:WS:AD',
    '?': 'WA:AS:SD',
    '!': 'WA:WD:DS',
    '"': 'WD:WA:WS',
    '\'': 'WD:DS:SA'
}

# Add special characters to main list
font.update(font_special)

# Define positions
W = (0, 0)
A = (0, -1)
S = (1, -1)
D = (1, 0)

STROKES = {
    '': [],
    'WA': [W, A],
    'WS': [W, S],
    'WD': [W, D],
    'DA': [D, A],
    'DS': [D, S],
    'SA': [S, A]
}

# Initialize Pygame
pygame.init()

# Screen dimensions
cell_size = 64  # Size of each grid cell
screen_width = cell_size * 16
screen_height = cell_size * 16

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
one_stroke = white
two_stroke = (255, 0, 0)  # Red


# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Character Rendering")

# History of lines for rendering styling
stroke_history = []


def code_message(s):
    s = s.upper()
    coded_message = []
    for c in s:
        if c in font:
            coded_message.append(font[c])
        else:
            # print(f"This character [ {c} ] has no representation.")
            coded_message.append(font[' '])

    return coded_message


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
    # Parse strokes
    strokes = character_lines.split(':')
    for s in strokes:
        stroke = STROKES['']  # Empty stroke
        if s in STROKES:
            stroke = STROKES[s]
        try:
            if s[1] + s[0] in STROKES:  # Check for flipped pairs
                stroke = STROKES[s[1] + s[0]]
        except IndexError:
            print(s)

        # As long as the stroke isn't empty
        if stroke != STROKES['']:
            # Parse and assign coordinates if the stroke isn't empty
            start_x = grid_x * cell_size + stroke[0][0] * cell_size
            start_y = grid_y * cell_size - stroke[0][1] * cell_size
            end_x = grid_x * cell_size + stroke[1][0] * cell_size
            end_y = grid_y * cell_size - stroke[1][1] * cell_size

            # THIS WILL NEED TO BE SIMPLIFIED ONCE IT IS WORKING AS INTENDED
            # If the line is already in the log, add it as is
            if [{'x': start_x, 'y': start_y}, {'x': end_x, 'y': end_y}] in stroke_history:
                stroke_history.append([
                    {'x': start_x, 'y': start_y},
                    {'x': end_x, 'y': end_y}
                ])
            # If the line is in the log but with the coordinates flipped, enter it as it is in the log
            elif [{'x': end_x, 'y': end_y}, {'x': start_x, 'y': start_y}] in stroke_history:
                stroke_history.append([
                    {'x': start_x, 'y': start_y},
                    {'x': end_x, 'y': end_y}
                ])
            # If this is the first time the line is being entered into the list, enter it as is
            else:
                stroke_history.append([
                    {'x': start_x, 'y': start_y},
                    {'x': end_x, 'y': end_y}
                ])

            # Determine stroke color, default is one_stroke
            stroke_color = one_stroke
            stroke_count = (stroke_history.count([{'x': start_x, 'y': start_y}, {'x': end_x, 'y': end_y}]) +
                            stroke_history.count([{'x': end_x, 'y': end_y}, {'x': start_x, 'y': start_y}]))
            if stroke_count == 2:
                stroke_color = two_stroke
            # Render
            pygame.draw.line(screen, stroke_color, (start_x, start_y), (end_x, end_y), 1)


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(black)
    # draw_grid()

    # Positional variables
    i = 1
    j = 1
    increment = 1
    horizontal_limit = 1

    message = code_message("aa")
    stroke_history = []
    for m in message:
        if m == 'smile' or m == 'frown':
            continue
        else:
            if m != ' ':
                render_character(m, i, j)
            i += increment
            if i > horizontal_limit:
                j += increment
                i = 1

    print(stroke_history)

    pygame.display.flip()
    # running = False

pygame.quit()
