from tkinter import  *

import imageio as imageio
from PIL import Image, ImageTk
from tkinter import filedialog, messagebox
import cv2


class Window(Frame):
    title = "Traffic Violation System"
    home_banner_image = "assets/images/homepage.jpg"
    # first frame of the selected will be shown at this
    generated_image_path = "assets/images/generated/preview.png"
    program_instructions = """
    Step to run this program :
    1> Choose a recorded video from below button
    2> After Selecting, draw anchor points by clicking analyse video from button below video preview
    3> Program will detect vehicles in the video and automatically stores frames of vehicle going past the anchor points
    """

    # used to store a history of packed widgets
    widget_history = []
    def __init__(self, master=None):
        Frame.__init__(self, master)

        self.master = master
        self.setup_window()
        self.createMenuOptions()

        self.renderUI()

    def setup_window(self):
        w, h = self.master.winfo_screenwidth(), self.master.winfo_screenheight()
        self.master.geometry("%dx%d+0+0" % (w, h))
        self.master.title(self.title)

    def createMenuOptions(self):
        menu = Menu(self.master)
        self.master.config(menu=menu)

        file = Menu(menu)
        file.add_command(label="Exit App", command=exit)
        menu.add_cascade(label="File", menu=file)

    def open_file(self):
        self.selectedFileName = filedialog.askopenfilename()

        cap = cv2.VideoCapture(self.selectedFileName)

        try:
            reader = imageio.get_reader(self.selectedFileName)
            fps = reader.get_meta_data()['fps']

            ret, image = cap.read()
            cv2.imwrite(self.generated_image_path,
                        image)

            self.show_image(self.generated_image_path)
        except:
            messagebox.showerror("Error Occurred", "Import a Valid video File")


    def renderUI(self):
        self.imgSize = Image.open(self.home_banner_image)
        self.tkimage = ImageTk.PhotoImage(self.imgSize)
        self.w, self.h = (800, 300)

        self.canvas = Canvas(master=self.master, width=self.w, height=self.h)
        self.canvas.create_image(20, 20, image=self.tkimage, anchor='center')
        self.canvas.pack()

        label = Label(self.master,text=self.program_instructions)
        label.pack()
        self.widget_history.append(label)

        btn = Button(text = "Open video file",command = self.open_file)
        btn.pack()
        self.widget_history.append(btn)

    def addEmptyLine(self):
        br = Label(text = "")
        br.pack()
        self.widget_history.append(br)

    def show_image(self, frame):
        self.imgSize = Image.open(frame)
        self.tkimage = ImageTk.PhotoImage(self.imgSize)
        self.w, self.h = (800, 300)

        self.canvas.destroy()
        for w in self.widget_history:
            w.pack_forget()

        self.canvas = Canvas(master=self.master, width=self.w, height=self.h)
        self.canvas.create_image(0, 0, image=self.tkimage, anchor='nw')
        self.canvas.pack()

        analyze_btn = Button(text = "Analyze video",command = self.analyze_video)
        analyze_btn.pack()

    def analyze_video(self):
        messagebox.showinfo("TODO","Video analyzing not implemented")