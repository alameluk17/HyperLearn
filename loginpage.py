import tkinter
import customtkinter
from PIL import ImageTk, Image
from homepage import *
def button_function():
    print("button pressed")
    homepage(main)
    

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#main widget    
main=customtkinter.CTk()
#main.geometry("400x240")
main.title("HYPER LEARN")

image1 = Image.open("Logo_matched.png")
image1=image1.resize((500, 500), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

panel = tkinter.Label(main, image = test)
panel.grid(row=0,column=0,rowspan=6)

label_1=tkinter.Label(main,text="LogIn",font=60)
label_1.grid(row=0,column=1)

#login credentials
label_2=tkinter.Label(main,text="Enter your Name              :",font=40)
label_3=tkinter.Label(main,text="Enter your Password        :",font=40)
entry_name=tkinter.Entry(main,width=30,bd=10,font=40)
entry_id=tkinter.Entry(main,width=30,bd=10,font=40)
label_2.grid(row=1,column=1)
label_3.grid(row=2,column=1)
entry_name.grid(row=1,column=3)
entry_id.grid(row=2,column=3) 


# Use CTkButton instead of tkinter Button
submit_button = customtkinter.CTkButton(master=main, text="Submit", command=button_function)
submit_button.grid(row=3,column=2)



#configurable label 
label_4=tkinter.Label(main,text="\n")
label_4.grid(row=4,column=2)

#new members
label_5=tkinter.Label(main,text="For new membership         :",font=40)
label_5.grid(row=5,column=1)
newuser_button = customtkinter.CTkButton(master=main, text="Sign Up", command=button_function)
newuser_button.grid(row=5,column=2)


main.mainloop()