
import pygame

from src.constants import CONTAINER_DEFAULT_RADIUS, CONTAINER_DEFAULT_THICKNESS, CONTAINER_DEFAULT_CENTER, CONTAINER_DEFAULT_COLOR, GAME_DEFAULT_SCREEN_COLOR, CONTAINER_DEFAULT_VELOCITY
from src.utils import distance

from src.ball import Ball

import numpy


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
        self.vx, self.vy = CONTAINER_DEFAULT_VELOCITY # Does not update anywhere

        self.radius = radius
        self.thickness = thickness

        half_thickness = thickness // 2
        self.innerRadius = radius - half_thickness
        self.outerRadius = radius + half_thickness

        # Appearance
        self.color = CONTAINER_DEFAULT_COLOR


    def center(self):
        return (self.x, self.y)


    def draw(self, screen: pygame.Surface) -> None:
        """Draws the barrier on the screen by drawing white on grey circle

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


    def update(self, dt: float) -> None:
        """Does not do anything whatsoever

        Args:
            dt (float): The delta time
        """
        # HARDCODE:
        if 800 < self.x or self.x < 200:
            self.vx *= -1

        self.x += self.vx * dt
        self.y += self.vy * dt


    def returnBallCollision(self, ball: Ball) -> bool:
        """For spatial locality. That is, the balls would be different.

        Args:
            ball (Ball): The ball to check collision against.

        Returns:
            bool: True if collision
        """
        collision = False

        d = distance(self.center(), ball.center())
        if ((d + ball.radius) >= self.innerRadius) and ((d - ball.radius) <= self.outerRadius):
            collision = True

        return collision


    def collisionPhysics(self, ball: Ball) -> bool:
        """Works on collision occurrences to save audio and change state of ball

        Args:
            ball (Ball): The ball to check collision against

        Returns:
            bool: True if collision
        """

        # first check collision
        if (self.returnBallCollision(ball) == False):
            return False
            pass

        else:
            dx = (ball.x - self.x)
            dy = (ball.y - self.y)
            d = (dx ** 2 + dy ** 2) ** (0.5)

            r_cap = (dx / d, dy / d)

            v_rel = (ball.vx - self.vx, ball.vy - self.vy)
            v_rel_dot_r_cap = (v_rel[0] * r_cap[0] + v_rel[1] * r_cap[1])

            v_rad = (v_rel_dot_r_cap * r_cap[0], v_rel_dot_r_cap * r_cap[1])
            v_new = (ball.vx - 2 * v_rad[0], ball.vy - 2 * v_rad[1])

            ball.vx, ball.vy = v_new

            return True
