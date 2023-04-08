import tkinter
import customtkinter
from PIL import ImageTk, Image

def button_function():
    print("button pressed")

def homepage(main):
    main.destroy()
    customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
    customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

    home = customtkinter.CTk()
    home.title("HomePage")
    image1 = Image.open("Logo_matched.png")
    image1=image1.resize((100, 100), Image.ANTIALIAS)
    test = ImageTk.PhotoImage(image1)

    logo_label = tkinter.Label(home , image =test )
    logo_label.grid(row=0, column=0)
    label_1 = tkinter.Label(home,text="HyperLearn HomePage",font=500);
    label_1.grid(row = 0 ,column =1, columnspan=4)

    label_2 = tkinter.Label(home,text = "Games",font=350)
    label_2.grid(row=1,column=0,columnspan=3)

    label_3 = tkinter.Label(home , text= "Your Profile",font =350)
    label_3.grid(row=1, column=3,columnspan=2)

    name_label = tkinter.Label(home,text ="Name  :",font = 200)
    name_label.grid(row=2,column=3)

    name_label2= tkinter.Label(home,text = "Heera" ,font=200)
    name_label2.grid(row=2,column=4)

    Age_label = tkinter.Label(home , text = "Age   :",font=200)
    Age_label.grid(row=3,column=3)

    Age_Label2 =tkinter.Label(home,text = "3",font=200)
    Age_Label2.grid(row = 3, column=4)

    Points_Label = tkinter.Label(home , text="Points" ,font=200)
    Points_Label.grid(row = 4,column =3)

    Points_Label1 = tkinter.Label(home , text = "50", font =200)
    Points_Label1.grid(row=4, column=4)
    

    gamelogo = Image.open("ImageRecoLogo.png")
    gamelogo=gamelogo.resize((200,200),Image.ANTIALIAS)
    gl = ImageTk.PhotoImage(gamelogo)

    logo_label = tkinter.Label(home, image = gl)
    logo_label.grid(row=2,column=0,rowspan =4)

    gamelogo2 = Image.open("safarilogo.png")
    gamelogo2=gamelogo2.resize((200,200),Image.ANTIALIAS)
    g2 = ImageTk.PhotoImage(gamelogo2)

    logo_label_2 = tkinter.Label(home, image = g2)
    logo_label_2.grid(row=2,column=1,rowspan =4)

    gamelogo3 = Image.open("spelbeelogo.png")
    gamelogo3 =gamelogo3.resize((200,200),Image.ANTIALIAS)
    g3 = ImageTk.PhotoImage(gamelogo3)

    logo_label_3 = tkinter.Label(home, image = g3)
    logo_label_3.grid(row=2,column=2,rowspan =4)

    PlayButton1 = customtkinter.CTkButton(master=home, text="Play", command=button_function)
    PlayButton1.grid(row=6,column=0)

    PlayButton2 = customtkinter.CTkButton(master=home, text="Play", command=button_function)
    PlayButton2.grid(row=6,column=1)

    PlayButton3 = customtkinter.CTkButton(master=home, text="Play", command=button_function)
    PlayButton3.grid(row=6,column=2)


    home.mainloop()