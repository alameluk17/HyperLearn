import tkinter
import customtkinter
from PIL import ImageTk, Image

def button_function():
    print("button pressed")
    return 0

from speechtotext import *

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#main widget    

list = ["Hill" , "Sun" , "Bird" , "River", "Sunset"]


ImageRec=customtkinter.CTk()
#main.geometry("400x240")
ImageRec.title("Image Recognition Game")
image1 = Image.open("ImageRec.jpeg")
image1=image1.resize((400, 400), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

panel = tkinter.Label(ImageRec, image = test)
panel.grid(row=0,column=0,rowspan=4)

label = tkinter.Label(ImageRec, text=list[2],font =40)
label.grid(row =0,column=1)

rec_button=customtkinter.CTkButton(master= ImageRec,text="Record",command=lambda:speechtotext(list[2]))
rec_button.grid(row=1,column=1)

next_button=customtkinter.CTkButton(master= ImageRec,text="Next",command=button_function)
next_button.grid(row=3,column=1)



ImageRec.mainloop()