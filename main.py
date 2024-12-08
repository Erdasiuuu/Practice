from PIL import Image, ImageTk
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk


class ImageEditor:
    def __init__(self):
        self.root = None
        self.window = None
        self.image_frame = None
        self.window = None
        self.image = None
        self.crop_frame = None
        self.crop_frame_fields = None
        self.show_welcome_window()


    def show_welcome_window(self):
        if self.root is None:
            self.root = tk.Tk()
            self.crop_frame = tk.Frame(self.root)
        else:
            self.clear_window()

        self.root.title("Загрузка изображения")
        self.root.minsize(300, 50)

        tk.Button(self.root, text="Загрузить изображение", command=self.load_image).pack()
        tk.Button(self.root, text="Сделать фото с камеры", command=self.capture_from_camera).pack()
        tk.Button(self.root, text="Выйти", command=self.root.destroy).pack()
        self.root.mainloop()


    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg")],
        )
        if file_path:
            photo = Image.open(file_path)
            self.show_image_window(photo)


    def capture_from_camera(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            photo = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.show_image_window(photo)
        else:
            print("Не удалось подключиться к камере")
        cv2.destroyAllWindows()


    def show_image_window(self, photo):
        self.clear_window()
        self.root.title("Просмотр изображения")
        
        self.image = ImageTk.PhotoImage(photo)
        
        label = tk.Label(self.root, image=self.image)
        label.pack()

        tk.Button(self.crop_frame, text="Обрезать изображение", command=self.toggle_crop_frame).pack()
        self.crop_frame.pack(fill=tk.BOTH)
        tk.Button(self.root, text="Новое изображение", command=self.show_welcome_window).pack()
        tk.Button(self.root, text="Выйти", command=self.root.destroy).pack()


    def toggle_crop_frame(self):
        """Показать или скрыть фрейм для ввода координат обрезки"""
        if self.crop_frame_fields is None:
            self.crop_frame_fields = tk.Frame(self.crop_frame)
            tk.Label(self.crop_frame_fields, text="Координаты обрезки").pack()
            tk.Label(self.crop_frame_fields, text="Левая:").pack()
            tk.Entry(self.crop_frame_fields).pack()
            tk.Label(self.crop_frame_fields, text="Верхняя:").pack()
            tk.Entry(self.crop_frame_fields).pack()
            tk.Label(self.crop_frame_fields, text="Правая:").pack()
            tk.Entry(self.crop_frame_fields).pack()
            tk.Label(self.crop_frame_fields, text="Нижняя:").pack()
            tk.Entry(self.crop_frame_fields).pack()
            self.crop_frame_fields.pack(fill=tk.BOTH)
        else:
            self.crop_frame_fields.destroy()
            self.crop_frame_fields = None
        
        

    def show_crop_window(self):
        tk.Label(self.window, text="Координаты обрезки").pack()
        tk.Label(self.window, text="Левая:").pack()
        entry_left = tk.Entry(self.window)
        entry_left.pack()
        tk.Label(self.window, text="Верхняя:").pack()
        entry_top = tk.Entry(self.window)
        entry_top.pack()
        tk.Label(self.window, text="Правая:").pack()
        entry_right = tk.Entry(self.window)
        entry_right.pack()
        tk.Label(self.window, text="Нижняя:").pack()
        entry_bottom = tk.Entry(self.window)
        entry_bottom.pack()


    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.crop_frame = tk.Frame(self.root)


if __name__ == '__main__':
    ImageEditor()
