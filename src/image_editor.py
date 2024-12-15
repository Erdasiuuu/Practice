import tkinter as tk
from frame import FrameManager
from get_photo import PhotoHandler
from crop import CropHandler
from brightness import BrightnessHandler
from draw_line import LineDrawer


class ImageEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.frame_manager = FrameManager(self.root)
        self.photo_handler = PhotoHandler(self)
        self.crop_handler = CropHandler(self)
        self.brightness_handler = BrightnessHandler(self)
        self.line_drawer = LineDrawer(self)

        self.image = None
        self.image_label = None

    def run(self):
        self.frame_manager.show_welcome_frame()
        self.root.mainloop()

    def set_image(self, photo):
        """Установить изображение для отображения."""
        self.image = photo
        self.update_image_label()

    def update_image_label(self):
        """Обновить отображение изображения на экране."""
        tk_image = self.photo_handler.get_tk_image(self.image)

        if self.image_label is None:
            self.image_label = tk.Label(self.frame_manager.main_frame, image=tk_image)
            self.image_label.image = tk_image
            self.image_label.pack(side=tk.RIGHT, anchor=tk.NE)
        else:
            self.image_label.image = tk_image
            self.image_label.config(image=tk_image)
