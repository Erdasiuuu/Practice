import tkinter as tk

class Crop:
    def __init__(self, master, image, set_image):
        self.master = master
        self.image = image
        self.set_image = set_image
        self.frame = None

        self.entry_x1 = None
        self.entry_y1 = None
        self.entry_x2 = None
        self.entry_y2 = None

        self.create()

    def create(self):
        if self.frame is None:
            self.frame = tk.Frame(self.master)

            tk.Label(
                self.frame,
                text="Координаты обрезки"
            ).pack()

            tk.Label(
                self.frame,
                text="x1"
            ).pack()
            self.entry_x1 = tk.Entry(self.frame)
            self.entry_x1.pack()

            tk.Label(
                self.frame,
                text="y1"
            ).pack()
            self.entry_y1 = tk.Entry(self.frame)
            self.entry_y1.pack()

            tk.Label(
                self.frame,
                text="x2"
            ).pack()
            self.entry_x2 = tk.Entry(self.frame)
            self.entry_x2.pack()

            tk.Label(
                self.frame,
                text="y2"
            ).pack()
            self.entry_y2 = tk.Entry(self.frame)
            self.entry_y2.pack()

            tk.Button(
                self.frame,
                text="Обрезать",
                relief="ridge",
                command=self.crop_image
            ).pack()

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def toggle_frame(self):
        if self.frame.winfo_ismapped():
            self.hide()
        else:
            self.show()

    def crop_image(self):
        try:
            tmp_x1 = int(self.entry_x1.get())
            tmp_y1 = int(self.entry_y1.get())
            tmp_x2 = int(self.entry_x2.get())
            tmp_y2 = int(self.entry_y2.get())

            x1 = min(tmp_x1, tmp_x2)
            y1 = min(tmp_y1, tmp_y2)
            x2 = max(tmp_x1, tmp_x2)
            y2 = max(tmp_y1, tmp_y2)

            self.image[0] = self.image[0].crop((x1, y1, x2, y2))
            self.set_image()
        except Exception as e:
            print(e)

