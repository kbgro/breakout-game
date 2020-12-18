import tkinter as tk

from .breakout import GameFrame


def main():
    """
    call gameloop
    """
    root = tk.Tk()
    root.title("Hello, Pong!")

    game = GameFrame(root)
    game.mainloop()


if __name__ == "__main__":
    main()
