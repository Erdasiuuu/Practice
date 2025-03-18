import numpy as np
from PIL import Image

class ColorChannels:
    def __init__(self, master, image, set_image):
        self.master = master
        self.image = image
        self.set_image = set_image

    def show(self):
        self.frame.pack()

    def hide(self):
        self.frame.pack_forget()

    def get_channel(self, color):
        colors = ("red", "green", "blue")
        try:
            idx = colors.index(color)
            image_arr = np.array(self.image[0])
            image_arr[:,:,(idx!=0, idx!=1, idx!=2)] *= 0
            self.image[0] = Image.fromarray(image_arr)
            self.set_image()
        except Exception as e:
            print(e)
