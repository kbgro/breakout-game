from tkinter import Canvas


class GameObject(object):
    """
    Base class for game items.
    """

    def __init__(self, canvas, item):
        self.canvas: Canvas = canvas
        self.item = item

    def get_position(self):
        """
        Return item position in the canvas.
        """
        return self.canvas.coords(self.item)

    def move(self, x, y):
        """
        Moves item in the canvas to x,y coordinates.
        """
        self.canvas.move(self.item, x, y)

    def delete(self):
        """
        delete item in the canvas.
        """
        self.canvas.delete(self.item)
