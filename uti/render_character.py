import pygame

from const.colors import one_stroke, two_stroke
from const.strokes import STROKES

cell_size = 16  # Size of each grid cell


def render_character(screen, stroke_history, character_lines, grid_x, grid_y):
    """Renders a character defined by lines within a grid cell.

    Args:
        screen: pygame display object thing IDK
        character_lines: A list of lines, where each line is a tuple of
                         two coordinate pairs: ((start_x, start_y), (end_x, end_y)).
                         Coordinates are within the 4-coordinate system (0, 1, -1).
        grid_x: The x-coordinate of the grid cell to render in.
        grid_y: The y-coordinate of the grid cell to render in.
        stroke_history:
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
