"""
ISPPJ1 2023
Study Case: Super Martian (Platformer)

Author: Alejandro Mujica
alejandro.j.mujic4@gmail.com

This file contains the class Camera.
"""
import pygame
import logging

logger = logging.getLogger("Camera")


class Camera:
    def __init__(self, x: int, y: int, width: int, height: int) -> None:
        """
        Camera init

        Args:
            x (int): xpos
            y (int): ypos
            width (int):
            height (int):
        """
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        logger.info("Created Camera on:%s,%s,%s,%s", x, y, width, height)

    def get_rect(self) -> pygame.Rect:
        return pygame.Rect(self.x, self.y, self.width, self.height)
