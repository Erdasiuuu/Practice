from PIL import ImageEnhance
import tkinter as tk

class Brightness:
    def __init__(self, master, image, set_image):
        self.master = master
        self.image = image
        self.set_image = set_image
        self.frame = None

        self.entry = None

        self.create()

    def create(self):
        if self.frame is None:
            self.frame = tk.Frame(self.master)

            tk.Label(
                self.frame,
                text="Множитель яркости\n(Обязательно > 1)"
            ).pack()
            self.entry = tk.Entry(self.frame)
            self.entry.pack()

            tk.Button(
                self.frame,
                text="Повысить яркость",
                relief="ridge",
                command=self.brightness_image
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

    def brightness_image(self):
        try:
            value = float(self.entry.get())
            if value <= 1.:
                raise Exception("Недопустимое значение яркости")

            enhancer = ImageEnhance.Brightness(self.image[0])
            self.image[0] = enhancer.enhance(value)

            self.set_image()
        except Exception as e:
            print(e)
