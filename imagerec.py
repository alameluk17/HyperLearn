import tkinter as tk
import customtkinter
from PIL import ImageTk, Image
import speech_recognition as sr
from PIL import ImageTk, Image
import pygame

def play_mp3_file(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.time.delay(3000) # wait for the sound to finish playing
    pygame.mixer.music.stop()

def window2(txt):
    ImageRec.destroy()
    window2_main = tk.Tk()
    window2_main.configure(bg='beige')
    tk.Label(window2_main, text=txt).pack()
    return window2_main


def button_function():
    print("button pressed")
    return 0


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

#main widget    

list = ["lion"]#" , "Sun" , "Bird" , "River", "Sunset"]


ImageRec=customtkinter.CTk()
#main.geometry("400x240")
ImageRec.title("Image Recognition Game")
image1 = Image.open("lion.jpeg")
image1=image1.resize((400, 400), Image.ANTIALIAS)
test = ImageTk.PhotoImage(image1)

panel = tk.Label(ImageRec, image = test)
panel.grid(row=0,column=0,rowspan=4)

label = tk.Label(ImageRec, text=list[0].capitalize(),font =40)
label.grid(row =0,column=1)

# initialize the recognizer
def speechtotext(str):
    r = sr.Recognizer()

    with sr.Microphone() as source:
        # read the audio data from the default microphone
        print("Recognizing...")
        audio_data = r.record(source, duration=5)
        print("Recognizing...")
        # convert speech to text
        text = r.recognize_google(audio_data)
        print(text)
        if text != str:
            print("try again")
            play_mp3_file('medieval-fanfare-6826.mp3')
            window2_main=window2("You've guessed incorrectly, but that's okay! Try again!")
            gif = Image.open("gif2.gif")

            # Create a list of GIF frames
            frames = []
            for frame in range(0, gif.n_frames):
                gif.seek(frame)
                frames.append(ImageTk.PhotoImage(gif))

            # Create a tkinter label to display the GIF
            label = tk.Label(window2_main, image=frames[0])
            label.pack()

            # Define a function to animate the GIF
            def animate(frame):
                label.configure(image=frames[frame])
                window2_main.after(50, animate, (frame + 1) % len(frames))

            # Start the animation
            window2_main.after(0, animate, 0)

            button1=tk.Button(window2_main,text="Exit", command=window2_main.destroy)
            button1.pack()

            window2_main.mainloop()
        else:
            print("Correct answer")
            play_mp3_file('crowd-cheering-143103.mp3')
            window2_main=window2("Congratulations! You've guessed correctly")
            gif = Image.open("gif1.gif")

            # Create a list of GIF frames
            frames = []
            for frame in range(0, gif.n_frames):
                gif.seek(frame)
                frames.append(ImageTk.PhotoImage(gif))

            # Create a tkinter label to display the GIF
            label = tk.Label(window2_main, image=frames[0])
            label.pack()

            # Define a function to animate the GIF
            def animate(frame):
                label.configure(image=frames[frame])
                window2_main.after(50, animate, (frame + 1) % len(frames))

            # Start the animation
            window2_main.after(0, animate, 0)

            button1=tk.Button(window2_main,text="Exit", command=window2_main.destroy)
            button1.pack()

            window2_main.mainloop()


rec_button=customtkinter.CTkButton(master= ImageRec,text="Record",command=lambda:speechtotext(list[0]))
rec_button.grid(row=1,column=1)

next_button=customtkinter.CTkButton(master= ImageRec,text="Next",command=button_function)
next_button.grid(row=3,column=1)



ImageRec.mainloop()