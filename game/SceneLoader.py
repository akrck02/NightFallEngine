from game.Tree import Tree
from debug.Rectangle import Rectangle
from Constant import WINDOW_WIDTH, WINDOW_HEIGHT
from gmath import Number

class SceneLoader:

    @staticmethod
    def load():
        return Tree()

    @staticmethod
    def loadFirst():
        tree = Tree()
 
        cell = 10

        for x in range(0, WINDOW_WIDTH, cell):
            for y in range(0, WINDOW_HEIGHT, cell):
                rectangle = Rectangle()
                rectangle.x = x
                rectangle.y = y

                # Get random color hex value
                rectangle.color = Number.randomHex()

                print(rectangle)

                rectangle.width = cell*.98
                rectangle.height = cell*.98
                tree.addChild(rectangle)




        return tree
