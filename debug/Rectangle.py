from game.Node2D import Node2D
from tkinter import Canvas


class Rectangle(Node2D):

    width = 10
    height = 10
    color = "#000"

    def __init__(self):
        super().__init__()

    def draw(self, display: Canvas):
        display.canvas.create_rectangle(self.x, self.y, self.x + self.width, self.y + self.height, fill=self.color)

    def update(self):
        pass

    def __str__(self):
        return "Rectangle[x: " + str(self.x) + " y: " + str(self.y) + " width: " + str(self.width) + " height: " + str(self.height) + " color: " + self.color
