from game.Node2D import Node2D
from tkinter import Canvas


class Tree:
    children = []

    def __init__(self):
        pass

    def update(self, delta: float):
        pass

    def draw(self, display: Canvas):
        for child in self.children:
            child.draw(display)

    def addChild(self, node: Node2D):
        self.children.append(node)
        pass
