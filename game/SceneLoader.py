from game.Tree import Tree
from debug.Rectangle import Rectangle


class SceneLoader:

    @staticmethod
    def load():
        return Tree()

    @staticmethod
    def loadFirst():
        tree = Tree()
        rectangle = Rectangle()
        tree.addChild(rectangle)

        return tree
