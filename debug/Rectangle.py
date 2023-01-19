from game.Node2D import Node2D
from tkinter import Canvas


class Rectangle(Node2D):

    def __init__(self):
        super().__init__()

    def draw(self, display: Canvas):
        display.canvas.create_rectangle(0, 0, 100, 100, fill="#af9afa")
        pass

    def update(self):
        pass
