import tkinter as tk
from PIL import ImageTk
from crop import Crop
from brightness import Brightness
from draw_line import DrawLine


class MainWindow:
    def __init__(self, master, image, switch_callback):
        self.master = master
        self.image = image
        self.image_label = None
        self.switch_callback = switch_callback

        self.master.title("Просмотр изображения")
        self.frames = None
        self.structures = None
        self.create()

    def create(self):
        if self.frames is None:
            self.frames = {}
            self.interaction_classes = {}

            self.create_frames()

            self.create_interaction_classes()

            self.create_fields()

    def create_frames(self):
        main_frame = tk.Frame(self.master)
        self.frames["main"] = main_frame
        self.frames["info"] = tk.Frame(main_frame)
        self.frames["crop"] = tk.Frame(main_frame)
        self.frames["brightness"] = tk.Frame(main_frame)
        self.frames["draw_line"] = tk.Frame(main_frame)

    def create_interaction_classes(self):
        self.interaction_classes["crop"] = Crop(
                                            self.frames["crop"],
                                            self.image,
                                            self.set_image)

        self.interaction_classes["brightness"] = Brightness(
                                                        self.frames["brightness"],
                                                        self.image,
                                                        self.set_image)

        self.interaction_classes["draw_line"] = DrawLine(
                                                    self.frames["draw_line"],
                                                    self.image,
                                                    self.set_image)

    def create_fields(self):
        tk.Button(
                self.frames["crop"],
                text="Обрезать изображение",
                command=self.interaction_classes["crop"].toggle_frame
        ).pack()

        tk.Button(
                self.frames["brightness"],
                text="Повысить яркость изображения",
                command=self.interaction_classes["brightness"].toggle_frame
        ).pack()

        tk.Button(
                self.frames["draw_line"],
                text="Нарисовать линию",
                command=self.interaction_classes["draw_line"].toggle_frame
        ).pack()

        tk.Button(
                self.frames["info"],
                text="Новое изображение",
                command=lambda: self.switch_callback("welcome")
        ).pack()

        tk.Button(
                self.frames["info"],
                text="Выйти",
                command=self.master.destroy
        ).pack()

    def show(self):
        self.frames["main"].pack()
        self.set_image()
        self.frames["crop"].pack()
        self.frames["brightness"].pack()
        self.frames["draw_line"].pack()
        self.frames["info"].pack()

    def hide(self):
        self.frames["main"].pack_forget()
        for option in ["crop", "brightness", "draw_line"]:
            self.interaction_classes[option].hide()

        for frame in self.frames.values():
            frame.pack_forget()

    def set_image(self):
        tk_image = ImageTk.PhotoImage(self.image[0])

        if self.image_label is None:
            self.image_label = tk.Label(
                                    self.frames["main"],
                                    image=tk_image)
            self.image_label.image = tk_image
        else:
            self.image_label.image = tk_image
            self.image_label.config(image=tk_image)

        self.image_label.pack(side=tk.RIGHT, anchor=tk.NE)
