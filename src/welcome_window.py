import tkinter as tk
from image_handler import ImageHandler

class WelcomeWindow:
    def __init__(self, master, image, switch_callback):
        self.master = master
        self.image = image
        self.switch_callback = switch_callback

        self.master.title("Просмотр изображения")
        self.frame = None
        self.create()

    def create(self):
        if self.frame is None:
            self.frame = tk.Frame(self.master)

            get_disk_image = lambda: ImageHandler.load_image(self.image)
            tk.Button(
                self.frame,
                text="Загрузить изображение",
                command=lambda: self.transform_to_main(get_disk_image)
            ).pack()

            get_camera_image = lambda: ImageHandler.capture_from_camera(self.image)
            tk.Button(
                self.frame,
                text="Сделать фото с камеры",
                command=lambda: self.transform_to_main(get_camera_image)
            ).pack()

            tk.Button(
                self.frame,
                text="Выйти",
                command=self.master.destroy
            ).pack()

    def transform_to_main(self, get_image):
        get_image()
        self.switch_callback("main")

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()
