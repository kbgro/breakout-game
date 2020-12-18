from tkinter import Canvas
from typing import Sequence

from .brick import Brick
from .game import GameObject


class Ball(GameObject):
    """
    Store information about the speed, direction and radius of the ball
    """

    # [ 1,  1] - if the ball is moving towards the bottom-right corner
    # [-1, -1] - if the ball is moving towards the top-left corner
    # [ 1, -1] - if the ball is moving towards the top-right corner
    # [-1,  1] - if the ball is moving towards the bottom-left corner

    def __init__(self, canvas: Canvas, x: int, y: int):
        self.speed: int = 10
        self.direction: list = [-1, -1]
        self.radius: int = 10

        item = canvas.create_oval(
            x - self.radius,
            y - self.radius,
            x + self.radius,
            y + self.radius,
            fill="white",
        )

        super().__init__(canvas, item)

    def update(self):
        """
        update's ball direction.
        """
        coords = self.get_position()
        width = self.canvas.winfo_width()

        if coords[0] <= 0 or coords[2] >= width:
            self.direction[0] *= -1
        if coords[1] <= 0:
            self.direction[1] *= -1

        x = self.direction[0] * self.speed
        y = self.direction[1] * self.speed

        self.move(x, y)

    def collide(self, game_objects: Sequence):
        """
        handle brick and ball collision.
        """
        coords = self.get_position()
        x = (coords[0] + coords[2]) * 0.5

        if len(game_objects) > 1:
            self.direction[1] *= -1

        elif len(game_objects) == 1:
            game_object = game_objects[0]
            coords = game_object.get_position()

            if x > coords[2]:
                self.direction[0] = 1
            elif x < coords[0]:
                self.direction[0] = -1
            else:
                self.direction[1] *= -1

        for game_object in game_objects:
            if isinstance(game_object, Brick):
                game_object.hit()
