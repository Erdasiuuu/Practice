from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog

def crop_image():
    try:
        left = int(entry_left.get())
        top = int(entry_top.get())
        right = int(entry_right.get())
        bottom = int(entry_bottom.get())
        
        cropped_img = img.crop((left, top, right, bottom))
        cropped_img.show()
    except Exception as e:
        print(f"Ошибка: {e}")

def load_image():
    global img
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if file_path:
        img = Image.open(file_path)
        img.show()

app = tk.Tk()
app.title("Обрезка изображения")

tk.Button(app, text="Загрузить изображение", command=load_image).pack()

tk.Label(app, text="Координаты обрезки").pack()
tk.Label(app, text="Левая:").pack()
entry_left = tk.Entry(app)
entry_left.pack()
tk.Label(app, text="Верхняя:").pack()
entry_top = tk.Entry(app)
entry_top.pack()
tk.Label(app, text="Правая:").pack()
entry_right = tk.Entry(app)
entry_right.pack()
tk.Label(app, text="Нижняя:").pack()
entry_bottom = tk.Entry(app)
entry_bottom.pack()

tk.Button(app, text="Обрезать изображение", command=crop_image).pack()

app.mainloop()
