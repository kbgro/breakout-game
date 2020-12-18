from tkinter import Canvas

from .ball import Ball
from .game import GameObject


class Paddle(GameObject):
    """
    Represents the player's paddle and has two attributes to store the width
    and height of the paddle.
    """

    def __init__(self, canvas: Canvas, x, y):
        self.width: int = 80
        self.height: int = 10

        self.ball = None
        item = canvas.create_rectangle(
            x - self.width / 2,
            y - self.height / 2,
            x + self.width / 2,
            y + self.height / 2,
            fill="blue",
        )

        super().__init__(canvas, item)

    def set_ball(self, ball):
        """
        store a reference to the ball, which can be moved with the ball before
        the game starts.
        """
        self.ball: Ball = ball

    def move(self, offset):
        """
        horizontal movement of the paddle.
        """
        coords = self.get_position()
        width = self.canvas.winfo_width()
        if coords[0] + offset >= 0 and coords[2] + offset <= width:
            super().move(offset, 0)
            if self.ball is not None:
                self.ball.move(offset, 0)
