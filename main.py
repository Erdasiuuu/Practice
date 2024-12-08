from PIL import Image, ImageTk
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class ImageEditor:
    def __init__(self):
        window = None
        image = None
        self.show_welcome_window()


    def show_welcome_window(self):
        self.window = tk.Tk()
        self.window.title("Загрузка изображения")
        self.window.minsize(300, 50)

        tk.Button(self.window, text="Загрузить изображение", command=self.load_image).pack()
        tk.Button(self.window, text="Сделать фото с камеры", command=self.capture_from_camera).pack()
        tk.Button(self.window, text="Выйти", command=self.window.destroy).pack()
        self.window.mainloop()


    def load_image(self):
        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg *.jpeg *.bmp *.gif")],
        )
        if file_path:
            self.image = Image.open(file_path)
            self.show_image_window()


    def capture_from_camera(self):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            self.image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            self.show_image_window()
        else:
            print("Не удалось подключиться к камере")
        cv2.destroyAllWindows()


    def show_image_window(self):
        self.window.destroy()
        self.window = tk.Tk()
        self.window.title("Просмотр изображения")
        
        photo = ImageTk.PhotoImage(self.image)
        
        label = tk.Label(self.window, image=photo)
        label.pack()    

        tk.Button(self.window, text="Обрезать изображение", command=self.show_crop_window).pack()
        tk.Button(self.window, text="Выйти", command=self.window.destroy).pack()
        window.mainloop()


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


    def crop_image(self):
        if img:
            try:
                left = int(entry_left.get())
                top = int(entry_top.get())
                right = int(entry_right.get())
                bottom = int(entry_bottom.get())
                cropped_img = img.crop((left, top, right, bottom))
                cropped_img.show()
            except Exception as e:
                print(f"Ошибка: {e}")


if __name__ == '__main__':
    ImageEditor()
