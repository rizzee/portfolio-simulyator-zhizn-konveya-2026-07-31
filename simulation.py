import numpy as np


class GameOfLife:
    def __init__(self, width, height):
        """Initialize grid with random states."""
        self.width = width
        self.height = height
        # Use int8 to save memory since we only need 0/1 values
        self.grid = np.random.choice([0, 1], size=(height, width), dtype=np.int8)
    
    def count_neighbors(self, x, y):
        """Count live neighbors around cell (x,y)."""
        # Use numpy slicing for more efficient neighbor counting
        x_min = max(0, x-1)
        x_max = min(self.width, x+2)
        y_min = max(0, y-1)
        y_max = min(self.height, y+2)
        
        # Sum all neighbors (including self), then subtract self
        return np.sum(self.grid[y_min:y_max, x_min:x_max]) - self.grid[y, x]
    
    def update(self):
        """Update grid state based on Conway's rules."""
        # Create padded grid for simpler neighbor counting
        padded = np.pad(self.grid, 1, mode='constant')
        
        # Calculate neighbors for all cells at once
        neighbors = (
            padded[:-2, :-2] + padded[:-2, 1:-1] + padded[:-2, 2:] +
            padded[1:-1, :-2] +                   padded[1:-1, 2:] +
            padded[2:, :-2]   + padded[2:, 1:-1] + padded[2:, 2:]
        )
        
        # Apply Conway's rules using vectorized operations
        birth = (self.grid == 0) & (neighbors == 3)
        survive = (self.grid == 1) & ((neighbors == 2) | (neighbors == 3))
        
        # Combine birth and survive conditions
        self.grid = (birth | survive).astype(np.int8)