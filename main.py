from PIL import Image, ImageTk
import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog, ttk


class ImageEditor:
    def __init__(self):
        self.root = None
        self.image_label = None
        self.frame = self.Frames()
        self.show_welcome_window()
        self.x = False

    class Frames:
        def __init__(self):
            self.crop_frame = None
            self.crop_frame_fields = None
            self.brightness_frame = None
            self.brightness_frame_fields = None
            self.draw_line_frame = None
            self.draw_line_frame_fields = None


    def show_welcome_window(self):
        if self.root is None:
            self.root = tk.Tk()
            self.frame.crop_frame = tk.Frame(self.root)
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
        
        image = ImageTk.PhotoImage(photo)
        self.image_label = tk.Label(self.root, image=image)
        self.image_label.pack()

        self.frame.crop_frame = tk.Frame(self.root)
        crop_image = "Обрезать изображение"
        crop_function = lambda: self.toggle_frame(self.frame.crop_frame_fields, crop_image)
        tk.Button(self.frame.crop_frame, text=crop_image, command=crop_function).pack()
        self.frame.crop_frame.pack(fill=tk.BOTH)


        tk.Button(self.root, text="Новое изображение", command=self.show_welcome_window).pack()
        tk.Button(self.root, text="Выйти", command=self.root.destroy).pack()

        
    def toggle_frame(self, frame, text):
        if frame is None:
            self.frame.crop_frame_fields = tk.Frame(self.frame.crop_frame)
            tk.Label(self.frame.crop_frame_fields, text="Координаты обрезки").pack()
            self.frame.crop_frame_fields.pack(fill=tk.BOTH)
        elif frame.winfo_ismapped():
            frame.pack_forget()
        else:
            frame.pack()
        
        

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


if __name__ == '__main__':
    ImageEditor()
