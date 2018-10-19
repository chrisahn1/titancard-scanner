import tkinter
class Window:
    def __init__(self, window, title):
        self.window = window
        self.window.title(title)
        self.window.mainloop()

Window(tkinter.Tk(), "Titan Card Scanner")
