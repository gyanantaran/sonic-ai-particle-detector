
import pygame

from typing import Tuple

from src.constants import BALL_DEFAULT_COLOR, BALL_DEFAULT_RADIUS

class Ball:
    """Represents a ball inside the simulation
    """


    def __init__(self, x: Tuple[int, int], v: Tuple[int, int], radius: int = BALL_DEFAULT_RADIUS):
        """Initializes a ball

        Args:
            x (Tuple[int, int]): The position of the ball
            v (Tuple[int, int]): The velocity of the ball
            radius (int, optional): The radius of the ball
        """
        self.x, self.y = x
        self.vx, self.vy = v

        self.radius = radius

        # Appearance
        self.color = BALL_DEFAULT_COLOR


    def draw(self, screen: pygame.Surface) -> None:
        """Draws the ball on the screen

        Args:
            screen (pygame.Surface): The screen to draw on
        """
        pygame.draw.circle(
                surface=screen,
                color=self.color,
                center=self.center(),
                radius=self.radius,
                width=0 # Fill the ball
            )


    def update(self, dt: float) -> None:
        """Does nothing

        Args:
            dt (float): The delta time, from the last frame update
        """
        self.x += self.vx * dt
        self.y += self.vy * dt

    def center(self):
        """Returns the center (x, y) of the ball
        """
        return (self.x, self.y)
