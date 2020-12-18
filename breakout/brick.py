from tkinter import Canvas

from .game import GameObject


class Brick(GameObject):
    """
    Represents brick object in game.
    """

    COLORS = {1: "#999999", 2: "#555555", 3: "#222222"}

    def __init__(self, canvas: Canvas, x: int, y: int, hits: int):
        self.width: int = 75
        self.height: int = 20
        self.hits: int = hits

        color = Brick.COLORS[hits]
        item = canvas.create_rectangle(
            x - self.width / 2,
            y - self.height / 2,
            x + self.width / 2,
            y + self.height / 2,
            fill=color,
            tags="brick",
        )

        super().__init__(canvas, item)

    def hit(self):
        """
        represents a hit on brick by a ball.
        """
        self.hits -= 1
        if self.hits == 0:
            self.delete()
        else:
            self.canvas.itemconfig(self.item, fill=Brick.COLORS[self.hits])
