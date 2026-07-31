import pygame
from simulation import GameOfLife
from visualization import GridVisualizer
from config import WIDTH, HEIGHT, CELL_SIZE, FPS


def main():
    pygame.init()
    game = GameOfLife(WIDTH, HEIGHT)
    visualizer = GridVisualizer(game.grid, CELL_SIZE)
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        game.update()
        visualizer.draw_grid()
        visualizer.update()
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()