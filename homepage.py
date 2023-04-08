import tkinter
import customtkinter
from PIL import ImageTk, Image

def homepage(main):
    main.destroy()
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    home = customtkinter.CTk()
    home.title("HomePage")


    label_1 = tkinter.Label(home,text="HyperLearn HomePage",font=500);
    label_1.grid(row = 0 ,column =4, columnspan=3)


    home.mainloop()