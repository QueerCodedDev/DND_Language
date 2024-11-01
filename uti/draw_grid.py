import pygame


def draw_grid(screen, screen_width, screen_height, cell_size):
    """Draws a grid on the screen."""
    for x in range(0, screen_width, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (x, 0), (x, screen_height))
    for y in range(0, screen_height, cell_size):
        pygame.draw.line(screen, (200, 200, 200), (0, y), (screen_width, y))
