from tkinter import  *

class Window(Frame):
    title = "Traffic Violation System"
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.setup_window()

    def setup_window(self):
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.title(self.title)
