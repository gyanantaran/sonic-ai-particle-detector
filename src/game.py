
import pygame

from src.ball import Ball
from src.container import Container

from src.constants import GAME_DEFAULT_BALLS, GAME_DEFAULT_SCREEN_COLOR, GAME_DEFAULT_SCREEN_SIZE, GAME_DEFAULT_FRAME_RATE
from src.utils import distance

import random

# HARDCODING
container = Container()
balls = [Ball((random.randint(400, 600), random.randint(400, 600)), (50, 0)) for _ in range(GAME_DEFAULT_BALLS)]
collision_data = []

class Game:
    """This class represents the game instances
    """

    def __init__(self):
        """Generates a new Game object
        """
        pygame.init()
        self.game_running = True
        self.clock = pygame.time.Clock()

        self.screen = pygame.display.set_mode(size=GAME_DEFAULT_SCREEN_SIZE)

        self.dt = 0.1

    def run(self):
        """Runs the game
        """
        while self.game_running:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_running = False
                    print(collision_data)
                    self.quit(reason="Manual quit")

            self.screen.fill(GAME_DEFAULT_SCREEN_COLOR)

            container.draw(self.screen)

            # On top of the container
            for ball in balls:
                ball.update(self.dt)
                ball.draw(self.screen)

                container.collisionPhysics(ball, collision_data)

            pygame.display.flip()

            self.dt = self.clock.tick(GAME_DEFAULT_FRAME_RATE) / 1000.0

    def quit(self, reason: str = None):
        """Quits the game
        """
        if reason is None:
            pass
        else:
            print(f"Quitting because {reason}")

        pygame.quit()
