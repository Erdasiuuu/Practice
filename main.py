from PIL import Image, ImageTk, ImageEnhance, ImageDraw
import cv2
import tkinter as tk


class ImageEditor:
    def __init__(self):
        self.root = tk.Tk()
        self.frame = self.Frames(self.root)
        self.crop = self.Crop()
        self.brightness = self.Brightness()
        self.draw_line = self.DrawLine()
        self.toggle_frame(self.frame.welcome_frame_fields,
                          "Загрузка изображения")
        self.image = None
        self.image_label = None
        self.root.mainloop()


    class Crop:
        def __init__(self):
            self.crop_frame = None
            self.crop_frame_fields = None
            self.entry_x1 = None
            self.entry_y1 = None
            self.entry_x2 = None
            self.entry_y2 = None


    class Brightness:
        def __init__(self):
            self.brightness_frame = None
            self.brightness_frame_fields = None
            self.brightness_entry = None


    class DrawLine:
        def __init__(self):
            self.draw_line_frame = None
            self.draw_line_frame_fields = None
            self.entry_x1 = None
            self.entry_y1 = None
            self.entry_x2 = None
            self.entry_y2 = None
            self.thickness_entry = None


    class Frames:
        def __init__(self, root):
            self.welcome_window = tk.Frame(root)
            self.main_window = tk.Frame(root)
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

            self.crop.crop_frame = tk.Frame(self.frame.main_frame)
            crop_image = "Обрезать изображение"
            crop_function = lambda: self.toggle_frame(self.crop.crop_frame_fields,
                                                      crop_image)
            tk.Button(self.crop.crop_frame,
                      text=crop_image, command=crop_function).pack()
            self.crop.crop_frame.pack()

            self.brightness.brightness_frame = tk.Frame(self.frame.main_frame)
            brightness_image = "Повысить яркость изображения"
            brightness_function = lambda: self.toggle_frame(self.brightness.brightness_frame_fields,
                                                            brightness_image)
            tk.Button(self.brightness.brightness_frame,
                      text=brightness_image, command=brightness_function).pack()
            self.brightness.brightness_frame.pack()

            self.draw_line.draw_line_frame = tk.Frame(self.frame.main_frame)
            draw_line = "Нарисовать линию"
            draw_line_function = lambda: self.toggle_frame(self.draw_line.draw_line_frame_fields,
                                                           draw_line)
            tk.Button(self.draw_line.draw_line_frame,
                      text=draw_line, command=draw_line_function).pack()
            self.draw_line.draw_line_frame.pack()

            tk.Button(self.frame.main_frame,
                      text="Новое изображение",
                      command=self.create_welcome_frame).pack()

            tk.Button(self.frame.main_frame,
                      text="Выйти", command=self.root.destroy).pack()

        else:
            self.crop.crop_frame_fields.pack_forget()
            self.brightness.brightness_frame_fields.pack_forget()
            self.draw_line.draw_line_frame_fields.pack_forget()
            self.set_image(photo)

        self.frame.main_window.pack()
        self.frame.main_frame.pack()

        
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

            tk.Button(self.frame.welcome_frame,
                      text="Загрузить изображение",
                      command=self.load_image).pack()

            tk.Button(self.frame.welcome_frame,
                      text="Сделать фото с камеры",
                      command=self.capture_from_camera).pack()

            tk.Button(self.frame.welcome_frame,
                      text="Выйти",
                      command=self.root.destroy).pack()

        else:
            self.frame.main_window.pack_forget()

        self.frame.welcome_frame.pack()
        self.frame.welcome_window.pack()


    def create_crop_frame(self):
        self.crop.crop_frame_fields = tk.Frame(self.crop.crop_frame)
        tk.Label(self.crop.crop_frame_fields,
                 text="Координаты обрезки").pack()
        
        tk.Label(self.crop.crop_frame_fields,
                 text="Левая").pack()
        self.crop.entry_x1 = tk.Entry(self.crop.crop_frame_fields)
        self.crop.entry_x1.pack()

        tk.Label(self.crop.crop_frame_fields,
                 text="Верхняя").pack()
        self.crop.entry_y1 = tk.Entry(self.crop.crop_frame_fields)
        self.crop.entry_y1.pack()

        tk.Label(self.crop.crop_frame_fields,
                 text="Правая").pack()
        self.crop.entry_x2 = tk.Entry(self.crop.crop_frame_fields)
        self.crop.entry_x2.pack()

        tk.Label(self.crop.crop_frame_fields,
                 text="Нижняя").pack()
        self.crop.entry_y2 = tk.Entry(self.crop.crop_frame_fields)
        self.crop.entry_y2.pack()

        tk.Button(self.crop.crop_frame_fields,
                  text="Обрезать",
                  relief="ridge",  
                  command=self.crop_img).pack()

        self.crop.crop_frame_fields.pack()

        
    def create_brightness_frame(self):
        self.brightness.brightness_frame_fields = tk.Frame(self.brightness.brightness_frame)
        tk.Label(self.brightness.brightness_frame_fields,
                 text="Множитель яркости\n(Обязательно > 1)").pack()
        self.brightness.brightness_entry = tk.Entry(self.brightness.brightness_frame_fields)
        self.brightness.brightness_entry.pack()

        tk.Button(self.brightness.brightness_frame_fields,
                  text="Повысить яркость",
                  relief="ridge",  
                  command=self.brightness_img).pack()

        self.brightness.brightness_frame_fields.pack()

        
    def create_draw_line_frame(self):
        self.draw_line.draw_line_frame_fields = tk.Frame(self.draw_line.draw_line_frame)
        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Координаты обрезки").pack()
        
        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Левая").pack()
        self.draw_line.entry_x1 = tk.Entry(self.draw_line.draw_line_frame_fields)
        self.draw_line.entry_x1.pack()

        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Верхняя").pack()
        self.draw_line.entry_y1 = tk.Entry(self.draw_line.draw_line_frame_fields)
        self.draw_line.entry_y1.pack()

        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Правая").pack()
        self.draw_line.entry_x2 = tk.Entry(self.draw_line.draw_line_frame_fields)
        self.draw_line.entry_x2.pack()

        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Нижняя").pack()
        self.draw_line.entry_y2 = tk.Entry(self.draw_line.draw_line_frame_fields)
        self.draw_line.entry_y2.pack()

        tk.Label(self.draw_line.draw_line_frame_fields,
                 text="Толщина линии").pack()
        self.draw_line.entry_thickness = tk.Entry(self.draw_line.draw_line_frame_fields)
        self.draw_line.entry_thickness.pack()

        tk.Button(self.draw_line.draw_line_frame_fields,
                  text="Нарисовать",
                  relief="ridge",  
                  command=self.draw_line_img).pack()

        self.draw_line.draw_line_frame_fields.pack()
        

    def crop_img(self):
        try:
            tmp_x1 = int(self.crop.entry_x1.get())
            tmp_y1 = int(self.crop.entry_y1.get())
            tmp_x2 = int(self.crop.entry_x2.get())
            tmp_y2 = int(self.crop.entry_y2.get())

            x1 = min(tmp_x1, tmp_x2)
            y1 = min(tmp_y1, tmp_y2)
            x2 = max(tmp_x1, tmp_x2)
            y2 = max(tmp_y1, tmp_y2)

            self.image = self.image.crop((x1, y1, x2, y2))
            
            self.set_image()
        except Exception as e:
            print(e)

    def brightness_img(self):
        try:
            value = float(self.brightness.brightness_entry.get())
            if value <= 1.:
                raise Exception("Недопустимое значение яркости")

            enhancer = ImageEnhance.Brightness(self.image)
            self.image = enhancer.enhance(value)
            
            self.set_image()
        except Exception as e:
            print(e)


    def draw_line_img(self):
        try:
            tmp_x1 = int(self.draw_line.entry_x1.get())
            tmp_y1 = int(self.draw_line.entry_y1.get())
            tmp_x2 = int(self.draw_line.entry_x2.get())
            tmp_y2 = int(self.draw_line.entry_y2.get())
            thickness = int(self.draw_line.entry_thickness.get())

            x1 = min(tmp_x1, tmp_x2)
            y1 = min(tmp_y1, tmp_y2)
            x2 = max(tmp_x1, tmp_x2)
            y2 = max(tmp_y1, tmp_y2)
            
            draw = ImageDraw.Draw(self.image)
            draw.line((x1, y1, x2, y2), fill="green", width=thickness)
            
            self.set_image()
        except Exception as e:
            print(e)


    def set_image(self, photo=None):
        if photo is not None:
            self.image = photo
        tk_image = ImageTk.PhotoImage(self.image)

        if self.image_label is None:
            self.image_label = tk.Label(self.frame.main_frame,
                                        image=tk_image)

            self.image_label.image = tk_image
        else:
            self.image_label.image = tk_image
            self.image_label.config(image=tk_image)
        self.image_label.pack(side=tk.RIGHT, anchor=tk.NE)


if __name__ == '__main__':
    ImageEditor()
