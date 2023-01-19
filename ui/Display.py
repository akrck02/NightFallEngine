import tkinter
import Constant


class Display(tkinter.Tk):

    def __init__(self):
        super().__init__()
        self.title(Constant.WINDOW_TITLE)
        self.geometry(str(Constant.WINDOW_WIDTH) + "x" + str(Constant.WINDOW_HEIGHT))

        self.canvas = tkinter.Canvas(self, width=0, height=0, bg='#222', bd=0, highlightthickness=0, relief='ridge')
        self.canvas.pack(expand=tkinter.YES, fill=tkinter.BOTH)

    # Update the window
    def update(self):
        pass

    # Draw the window
    def draw(self):
        pass
