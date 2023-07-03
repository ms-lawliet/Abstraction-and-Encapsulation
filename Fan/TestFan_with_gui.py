# import needed modules
import customtkinter as ctk
from fan_class import Fan

ctk.set_appearance_mode("Dark")

root = ctk.CTk()
root.geometry("300x400")
root.title("TestFan")

# create objects
Fan1 = Fan(Fan.fast, "on", 10, "Yellow")
Fan2 = Fan(Fan.medium, "off", 5)

# call methods
Fan1.show()
Fan2.show()

# add design
lbl1 = ctk.CTkLabel(root, text=Fan1.show(), font=ctk.CTkFont(family="Courier New", size=24, weight="bold"))
lbl1.pack(padx=10, pady=(20, 20))
lbl1.configure(text_color="yellow")
lbl1.configure(fg_color="black")

lbl2 = ctk.CTkLabel(root, text=Fan2.show(), font=ctk.CTkFont(family="Courier New", size=24, weight="bold"))
lbl2.pack(padx=10, pady=(10, 20))
lbl2.configure(text_color="blue")
lbl2.configure(fg_color="black")

# make an exit button
button = ctk.CTkButton(root, text="Exit", command=root.destroy)
button.pack(padx=20, pady=10)

root.mainloop()
