from PIL import Image, ImageTk
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk


class ImageEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = self.Frames(self.root)
        self.toggle_frame(self.frame.welcome_frame_fields, "Загрузка изображения")
        self.image = None
        self.image_label = None
        self.root.mainloop()

    class Frames:
        def __init__(self, root):
            self.welcome_window = tk.Frame(root)
            self.main_window = tk.Frame(root)
            self.crop_frame = None
            self.crop_frame_fields = None
            self.brightness_frame = None
            self.brightness_frame_fields = None
            self.draw_line_frame = None
            self.draw_line_frame_fields = None
            self.welcome_frame = None
            self.welcome_frame_fields = None
            self.main_frame = None



    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg")],
        )
        if file_path:
            photo = Image.open(file_path)
            self.create_main_window(photo)


    def capture_from_camera(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            photo = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.create_main_window(photo)
        else:
            print("Не удалось подключиться к камере")
        cv2.destroyAllWindows()


    def create_main_window(self, photo):
        self.root.title("Просмотр изображения")
        if self.frame.welcome_window.winfo_ismapped():
            self.frame.welcome_window.pack_forget()

        if self.frame.main_frame is None:
            self.frame.main_frame = tk.Frame(self.frame.main_window)
        
            self.set_image(photo)

            self.frame.crop_frame = tk.Frame(self.frame.main_frame)
            crop_image = "Обрезать изображение"
            crop_function = lambda: self.toggle_frame(self.frame.crop_frame_fields, crop_image)
            tk.Button(self.frame.crop_frame, text=crop_image, command=crop_function).pack()
            self.frame.crop_frame.pack()

            '''
            self.frame.brightness_frame = tk.Frame(self.root)
            brightness_image = "Повысить яркость изображения"
            brightness_function = lambda: self.toggle_frame(self.frame.brightness_frame_fields, brightness_image)
            tk.Button(self.frame.brightness_frame, text=brightness_image, command=brightness_function).pack()
            self.frame.brightness_frame.pack(fill=tk.BOTH)

            self.frame.draw_line_frame = tk.Frame(self.root)
            draw_line = "Нарисовать линию"
            draw_line_function = lambda: self.toggle_frame(self.frame.draw_line_frame_fields, draw_line)
            tk.Button(self.frame.draw_line_frame, text=draw_line, command=draw_line_function).pack()
            self.frame.draw_line_frame.pack(fill=tk.BOTH)
            '''
            tk.Button(self.frame.main_frame, text="Новое изображение", command=self.create_welcome_frame).pack()
            tk.Button(self.frame.main_frame, text="Выйти", command=self.root.destroy).pack()
        else:
            self.frame.crop_frame_fields.pack_forget()
            self.set_image(photo)

        self.frame.main_frame.pack()
        self.frame.main_window.pack()

        
    def toggle_frame(self, frame, text):
        if frame is None:
            if text == "Загрузка изображения":
                self.create_welcome_frame()
            elif text == "Обрезать изображение":
                self.create_crop_frame()
            elif text == "Повысить яркость изображения":
                self.create_brightness_frame()
            elif text == "Нарисовать линию":
                self.create_draw_line_frame()
        elif frame.winfo_ismapped():
            for widget in frame.winfo_children():
                widget.pack_forget()
            frame.pack_forget()
        else:
            for widget in frame.winfo_children():
                widget.pack()
            frame.pack()
        

    def create_welcome_frame(self):
        self.root.title("Загрузка изображения")
        self.root.resizable(False, False)

        if self.frame.welcome_frame is None:
            self.frame.welcome_frame = tk.Frame(self.frame.welcome_window)
            tk.Button(self.frame.welcome_frame, text="Загрузить изображение", command=self.load_image).pack()
            tk.Button(self.frame.welcome_frame, text="Сделать фото с камеры", command=self.capture_from_camera).pack()
            tk.Button(self.frame.welcome_frame, text="Выйти", command=self.root.destroy).pack()
        else:
            self.frame.main_window.pack_forget()


        self.frame.welcome_frame.pack()
        self.frame.welcome_window.pack()

    def create_crop_frame(self):
        self.frame.crop_frame_fields = tk.Frame(self.frame.crop_frame)
        tk.Label(self.frame.crop_frame_fields, text="Координаты обрезки").pack()
        tk.Button(self.frame.crop_frame_fields, text='hihi', command=self.crop).pack()
        self.frame.crop_frame_fields.pack()
        
    def create_brightness_frame(self):
        self.frame.brightness_frame_fields = tk.Frame(self.frame.brightness_frame)
        tk.Label(self.frame.brightness_frame_fields, text="Координаты обрезки").pack()
        self.frame.brightness_frame_fields.pack(fill=tk.BOTH)
        
    def create_draw_line_frame(self):
        self.frame.draw_line_frame_fields = tk.Frame(self.frame.draw_line_frame)
        tk.Label(self.frame.draw_line_frame_fields, text="Координаты обрезки").pack()
        self.frame.draw_line_frame_fields.pack(fill=tk.BOTH)
        

    def crop(self):
        self.image = self.image.crop((10, 20, 300, 400))
        self.set_image()


    def set_image(self, photo=None):
        if photo is not None:
            self.image = photo
        tk_image = ImageTk.PhotoImage(self.image)
        if self.image_label is None:
            self.image_label = tk.Label(self.frame.main_frame, image=tk_image)
            self.image_label.image = tk_image
        else:
            self.image_label.image = tk_image
            self.image_label.config(image=tk_image)
        self.image_label.pack(side=tk.RIGHT)


if __name__ == '__main__':
    ImageEditor()
