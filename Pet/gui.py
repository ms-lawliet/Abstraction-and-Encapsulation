import tkinter as tk

root = tk.Tk()


def show_image():
    img_label = tk.Label(root)
    img_label.image = tk.PhotoImage(file="bg.jpg")
    img_label['image'] = img_label.image

    img_label.pack()


show_image()
root.mainloop()
