import pygame
import numpy as np


class GridVisualizer:
    def __init__(self, grid, cell_size=10):
        self.grid = grid
        self.cell_size = cell_size
        self.width = grid.shape[1] * cell_size
        self.height = grid.shape[0] * cell_size
        self.screen = pygame.display.set_mode((self.width, self.height))

    def draw_grid(self):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                color = (255, 255, 255) if cell else (0, 0, 0)
                rect = pygame.Rect(x * self.cell_size, y * self.cell_size,
                                   self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, color, rect)

    def update(self):
        pygame.display.flip()
