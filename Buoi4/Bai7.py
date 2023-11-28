import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class ImageFilterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image Filter App")

        # Khởi tạo biến
        self.original_image = None
        self.filtered_image = None

        # Tạo các thành phần giao diện
        self.create_widgets()

    def create_widgets(self):
        # Button để mở ảnh
        open_button = tk.Button(self.root, text="Open Image", command=self.open_image)
        open_button.pack(pady=10)

        # Button để áp dụng bộ lọc
        filter_button = tk.Button(self.root, text="Apply Filter", command=self.apply_filter)
        filter_button.pack(pady=10)

        # Hiển thị ảnh gốc
        self.original_label = tk.Label(self.root, text="Original Image")
        self.original_label.pack()

        # Hiển thị ảnh lọc
        self.filtered_label = tk.Label(self.root, text="Filtered Image")
        self.filtered_label.pack()

    def open_image(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.original_image = cv2.imread(file_path)
            self.display_image(self.original_image, self.original_label)

    def apply_filter(self):
        if self.original_image is not None:
            # Thực hiện xử lý ảnh ở đây (ví dụ: làm mịn ảnh)
            self.filtered_image = cv2.GaussianBlur(self.original_image, (5, 5), 0)
            self.display_image(self.filtered_image, self.filtered_label)

    def display_image(self, image, label):
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image = Image.fromarray(image)
        image = ImageTk.PhotoImage(image)

        label.configure(image=image)
        label.image = image

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageFilterApp(root)
    root.mainloop()
