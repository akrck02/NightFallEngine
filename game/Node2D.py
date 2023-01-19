from gmath.geometry.Vector2 import Vector2
from tkinter import Canvas


class Node2D:

    position: Vector2

    def __init__(self):
        self.position = Vector2.zero();

    def draw(self, display: Canvas):
        pass

    def update(self, delta: float):
        pass
