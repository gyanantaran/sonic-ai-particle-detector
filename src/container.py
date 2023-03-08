
import pygame

from src.constants import CONTAINER_DEFAULT_RADIUS, CONTAINER_DEFAULT_THICKNESS, CONTAINER_DEFAULT_CENTER, CONTAINER_DEFAULT_COLOR, GAME_DEFAULT_SCREEN_COLOR
from src.utils import distance

from src.ball import Ball


class Container:
    """The circular barrier/wall in which the elements live. **Circular throughout this project**
    """

    def __init__(
            self,
            radius: int = CONTAINER_DEFAULT_RADIUS,
            thickness: int = CONTAINER_DEFAULT_THICKNESS
        ):
        """Initialize the barrier/container

        Args:
            radius (int, optional): The radius of the container.
                                    Defaults to CONTAINER_DEFAULT_RADIUS.

            thickness (int, optional): The thickness of the container. Arround the radius
                                        Defaults to CONTAINER_DEFAULT_THICKNESS.
        """
        self.x, self.y = CONTAINER_DEFAULT_CENTER  # Does not update anywhere

        self.radius = radius
        self.thickness = thickness

        half_thickness = thickness // 2
        self.innerRadius = radius - half_thickness
        self.outerRadius = radius + half_thickness

        # Appearance
        self.color = CONTAINER_DEFAULT_COLOR


    def draw(self, screen: pygame.Surface) -> None:
        """Draws the barrier on the screen

        Args:
            screen (pygame.Surface): The screen to draw on
        """
        # The outer edge
        pygame.draw.circle(
                surface=screen,
                color=self.color,
                center=self.center(),
                radius=self.outerRadius,
                width=0
            )

        # The inner edge
        pygame.draw.circle(
                surface=screen,
                color=GAME_DEFAULT_SCREEN_COLOR,
                center=self.center(),
                radius=self.innerRadius,
                width=0
            )

    def update(self) -> None:
        """Does not do anything whatsoever
        """
        pass

    def returnBallCollide(self, ball: Ball) -> bool:
        """For spatial locality. That is, the balls would be different.

        Args:
            ball (Ball): The ball to check collision against.

        Returns:
            bool: True if collision
        """
        collision = False
        if (distance(self.center(), ball.center()) + ball.radius) >= self.innerRadius:
            collision = True

        return collision


    def center(self):
        return CONTAINER_DEFAULT_CENTER
