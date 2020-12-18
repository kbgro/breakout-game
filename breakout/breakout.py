import tkinter as tk

from .ball import Ball
from .brick import Brick
from .paddle import Paddle


class GameFrame(tk.Frame):
    """
    Game Canvas Frame
    """

    def __init__(self, master):
        super().__init__(master)

        self.lives = 3
        self.width = 610
        self.height = 400

        self.canvas = tk.Canvas(
            self, bg="#aaaaff", width=self.width, height=self.height
        )
        self.canvas.pack()
        self.pack()

        self.items = {}
        self.ball = None
        self.paddle = Paddle(self.canvas, self.width / 2, 326)
        self.items[self.paddle.item] = self.paddle

        for x in range(5, self.width - 5, 75):
            self.add_brick(x + 37.5, 50, 2)
            self.add_brick(x + 37.5, 70, 1)
            self.add_brick(x + 37.5, 90, 1)

        self.hud = None
        self.setup_game()
        self.canvas.focus_set()
        self.canvas.bind("<Left>", lambda _: self.paddle.move(-10))
        self.canvas.bind("<Right>", lambda _: self.paddle.move(10))

    def setup_game(self):
        """
        set's up game
        """
        self.add_ball()
        self.update_lives_text()
        self.text = self.draw_text(300, 200, "Press Space to start")
        self.canvas.bind("<space>", lambda _: self.start_game())

    def add_brick(self, x: int, y: int, hits: int):
        """
        add brick
        """
        brick = Brick(self.canvas, x, y, hits)
        self.items[brick.item] = brick

    def add_ball(self):
        """
        add ball
        """
        if self.ball is not None:
            self.ball.delete()
        paddle_coords = self.paddle.get_position()
        x = (paddle_coords[0] + paddle_coords[2]) * 0.5
        self.ball = Ball(self.canvas, x, 310)
        self.paddle.set_ball(self.ball)

    def draw_text(self, x: int, y: int, text: str, size="40"):
        """
        Displays text messages in the canvas.
        """
        font = ("Helvetica", size)
        return self.canvas.create_text(x, y, text=text, font=font)

    def update_lives_text(self):
        """
        Displays the number of lives left.
        """
        text = f"Lives: {self.lives}"
        if self.hud is None:
            self.hud = self.draw_text(50, 20, text=text, size=15)
        else:
            self.canvas.itemconfig(self.hud, text=text)

    def check_collisions(self):
        """
        links game loop with the ball collisions method
        """
        ball_coords = self.ball.get_position()
        items = self.canvas.find_overlapping(*ball_coords)
        objects = [self.items[x] for x in items if x in self.items]

        self.ball.collide(objects)

    def game_loop(self):
        """
        Game loop
        """
        self.check_collisions()
        num_bricks = len(self.canvas.find_withtag("brick"))

        if num_bricks == 0:
            self.ball.speed = None
            self.draw_text(300, 200, "You Win!")

        elif self.ball.get_position()[3] >= self.height:
            self.ball.speed = None
            self.lives -= 1

            if self.lives < 0:
                self.draw_text(300, 200, "Game Over")
            else:
                self.after(1000, self.setup_game)
        else:
            self.ball.update()
            self.after(50, self.game_loop)

    def start_game(self):
        """
        Starts the game loop.
        """
        self.canvas.unbind("<space>")
        self.canvas.delete(self.text)

        self.paddle.ball = None

        self.game_loop()
