import pygame
import sys
from settings import *
from simulation import Simulation


class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Pygame Momentum Simulator")
        self.clock = pygame.time.Clock()
        self.simulation = Simulation()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.simulation.run()
            pygame.display.update()
            self.clock.tick(FPS)


if __name__ == "__main__":
    main = Main()
    main.run()

