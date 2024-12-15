from tkinter import filedialog
from PIL import Image
import cv2

class ImageHandler:
    def load_image(image):
        file_path = filedialog.askopenfilename(
            title="Выберите изображение",
            filetypes=[("Изображения", "*.png *.jpg")],
        )
        if file_path:
            image[0] = Image.open(file_path)

    def capture_from_camera(image):
        cap = cv2.VideoCapture(0)
        ret, frame = cap.read()
        cap.release()
        if ret:
            image[0] = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        else:
            print("Не удалось подключиться к камере")
        cv2.destroyAllWindows()
