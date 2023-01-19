from ui.Display import Display
from input.Control import Control
from game.SceneLoader import SceneLoader
from debug.Debug import Debug
from Constant import WINDOW_TITLE

import threading
import time
import math


class GameEngine:
    MAX_FPS = 60
    MAX_UPS = 120

    frameTime = 1.0 / MAX_FPS
    updateTime = 1.0 / MAX_UPS

    running = False
    scene = None
    debug = None

    def __init__(self):
        self.display = Display()
        self.running = True
        self.debug = Debug()
        self.input = Control()
        self.scene = SceneLoader.loadFirst()

    def start(self):

        update = threading.Thread(target=self.update)
        update.start()

        render = threading.Thread(target=self.draw)
        render.start()

        self.display.mainloop()

    def update(self):

        lastTime = time.time()

        updates: int = 0
        lastSecond: int = 0

        # While the game is running
        while self.running:
            currentTime = time.time()
            delta = currentTime - lastTime

            # Update
            self.scene.update(delta)
            updates += 1

            if math.trunc(lastSecond) == 1:
                self.debug.setUps(updates)
                updates = 0
                lastSecond = 0;

            # sleep thread
            time.sleep(self.updateTime)
            lastSecond += self.updateTime

    def draw(self):

        lastTime = time.time()
        frames: int = 0
        lastSecond: int = 0

        # While the game is running
        while self.running:
            currentTime = time.time()
            delta = currentTime - lastTime

            # Draw
            self.display.draw()
            self.display.title(WINDOW_TITLE + " " + str(self.debug.fps) + " FPS / " + str(self.debug.ups) + " UPS")
            self.scene.draw(self.display)
            frames += 1

            if math.trunc(lastSecond) == 1:
                self.debug.setFps(frames)
                frames = 0
                lastSecond = 0

            # sleep thread
            time.sleep(self.frameTime)
            lastSecond += self.frameTime


game = GameEngine()
game.start()
