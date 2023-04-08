import tkinter as tk
from PIL import ImageTk, Image
import random
from random import shuffle
import pyttsx3
import pygame


def play_mp3_file(filename):
    pygame.mixer.init()
    pygame.mixer.music.load(filename)
    pygame.mixer.music.play()
    pygame.time.delay(3000) # wait for the sound to finish playing
    #pygame.mixer.music.stop()
# Define a function to play an MP3 file
def play_audio():
    pygame.mixer.init()
    pygame.mixer.music.load("audio.mp3")
    pygame.mixer.music.play()


def window2(txt):
    root.destroy()
    window2_main = tk.Tk()
    window2_main.configure(bg='beige')
    tk.Label(window2_main, text=txt).pack()
    return window2_main

WORDS = {'cat': 'cat.gif', 'dog': 'dog.gif', 'bird': 'bird.gif','fish':'fish.gif'}
SOUNDS = {'cat': 'cat-meow-14536.mp3','dog': 'dog_barking-6296.mp3','bird':'cardinal-37075.mp3', 'fish':'fish-jumping-splash-1-40948.mp3' }
word = random.choice(list(WORDS.keys()))
sound = random.choice(list(SOUNDS.keys()))
if word == sound:
    correct = 1
else:
    correct = 0
# Initialize pygame mixer
pygame.mixer.init()

# Create the tkinter root window
root = tk.Tk()
root.title("Animal Sound Game")
root.configure(bg='beige')


# Load the image using PIL
gif = Image.open(WORDS[word])

# Create a list of GIF frames
frames = []
for frame in range(0, gif.n_frames):
    gif.seek(frame)
    gif2 = gif.resize((250, 250), Image.ANTIALIAS)
    frames.append(ImageTk.PhotoImage(gif2))

# Create a tkinter label to display the GIF
label = tk.Label(root, image=frames[0])
label.pack()


# Define a function to animate the GIF
def animate(frame):
    label.configure(image=frames[frame])
    root.after(50, animate, (frame + 1) % len(frames))

# Start the animation
root.after(0, animate, 0)


# Create a label for the title
title_label = tk.Label(root, text="Is the animal making the right sound?")

title_label.pack()

# Load the audio file
audio = pygame.mixer.Sound(SOUNDS[sound])

# Create a callback function to play the audio when the image is clicked
def play_audio(event):
    audio.play()

# Bind the callback function to the label's click event
# Bind the play_audio function to the left mouse button event of the GIF label
label.bind("<Button-1>", lambda event: play_audio(audio))



# Create a frame for the buttons and pack it below the image
button_frame = tk.Frame(root)
button_frame.pack()

win  = 0
def check_answer(correct):
    if correct == 1:
        print("You're correct!")
        win = 1
    else:
        print("Aw! Please try again.")
        win = 0

    # Do something with the win variable, e.g., update the score

def check_answer1(correct):
    if correct == 0:
        print("You're correct!")
        win = 1
    else:
        print("Aw! Please try again.")
        win = 0
    
# Create the "Correct" button and pack it into the frame
correct_button = tk.Button(button_frame, text="Correct", command=lambda:check_answer(correct))
correct_button.pack(side="left")

# Create the "Wrong" button and pack it into the frame
wrong_button = tk.Button(button_frame, text="Wrong", command=lambda: check_answer1(correct))
wrong_button.pack(side="left")

def on_tile_click(event):
    if(win==0):
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

    else:
        print("Sorry, you failed. Try again.")
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

tile_labels = [correct_button,wrong_button]
for tile_label in tile_labels:
    tile_label.bind("<Button-1>", on_tile_click)

# Start the tkinter main loop
root.mainloop()
