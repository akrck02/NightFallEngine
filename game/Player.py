from game.Node2D import Node2D
from game.Sprite import Sprite
from tkinter import Canvas


class Player(Node2D):
    sprite: Sprite

    def __init__(self, sprite: Sprite):
        self.sprite = sprite
        pass

    def draw(self, display: Canvas):
        pass

    def update(self, delta: float):
        pass
