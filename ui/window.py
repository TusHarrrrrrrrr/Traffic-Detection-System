from tkinter import  *

class Window(Frame):
    title = "Traffic Violation System"
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.setup_window()
        self.createMenuOptions()

    def setup_window(self):
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.title(self.title)

    def createMenuOptions(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Open Video", command=self.open_file)
        file.add_command(label="Exit App", command=exit)
        menu.add_cascade(label="File", menu=file)

    def open_file(self):
        pass