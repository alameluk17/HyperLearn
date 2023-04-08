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

def window2(txt):
    root.destroy()
    window2_main = tk.Tk()
    window2_main.configure(bg='beige')
    tk.Label(window2_main, text=txt).pack()
    return window2_main
    
    

'''words=["cat","dog","fish","bird"]
images=['../cat.jpg','../dog.png','../fish.jpg','../bird.jpg']'''

#WORDS = {'cat': '../cat.jpg', 'dog': '../dog.png', 'bird': '../bird.jpg','fish':'../fish.jpg'} 

WORDS = {'cat': 'cat.gif', 'dog': 'dog.gif', 'bird': 'bird.gif','fish':'fish.gif'}


# Define the word to be guessed
word = random.choice(list(WORDS.keys()))
#image = WORDS[word]



# Create a list of letters from the word and shuffle them
letters = list(word)
shuffle(letters)

# Create a list of underscore placeholders for each letter in the word
placeholders = ["_" for _ in word]

# Create a window
root = tk.Tk()
root.title("Word Game")
root.configure(bg='beige')

gif = Image.open(WORDS[word])
'''gif2 = gif1.resize((250, 250), Image.ANTIALIAS)
gif=ImageTk.PhotoImage(gif2)

label = tk.Label(root, image=gif)
label.config(image=gif)
label.pack()'''

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


'''img = Image.open(image)
img = img.resize((250, 250), Image.ANTIALIAS) # resize the image
img_tk = ImageTk.PhotoImage(img)

# Create a label widget to display the image
label = tk.Label(root, image=img_tk)
label.pack()'''

# Create a label for the title
title_label = tk.Label(root, text="Unscramble the word!")

title_label.pack()


# Initialize the text-to-speech engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id) 

# Set properties
engine.setProperty('rate', 150)    # Speed percent (can go over 100)
engine.setProperty('volume', 1)  # Volume 0-1

for i in word: 
    engine.say(i)
    engine.runAndWait()

engine.say(word)
engine.runAndWait()

# Create a frame for the tiles
tile_frame = tk.Frame(root)
tile_frame.pack(side=tk.BOTTOM)

# Create tile labels for each letter and pack them into the frame
tile_labels = []
for letter in letters:
    tile_label = tk.Label(tile_frame, text=letter, relief=tk.RAISED, borderwidth=2)
    tile_label.pack(side=tk.LEFT, padx=5, pady=5)
    tile_labels.append(tile_label)

# Create a frame for the placeholders
placeholder_frame = tk.Frame(root)
placeholder_frame.pack(side=tk.TOP)

# Create placeholder labels for each letter and pack them into the frame
placeholder_labels = []
for placeholder in placeholders:
    placeholder_label = tk.Label(placeholder_frame, text=placeholder, font=("Arial", 24), relief=tk.SUNKEN, borderwidth=2, width=2, height=1)
    placeholder_label.pack(side=tk.LEFT, padx=5, pady=5)
    placeholder_labels.append(placeholder_label)

# Create a function to handle tile label clicks
def on_tile_click(event):
    # Get the clicked tile label
    tile_label = event.widget
    
    # Find the leftmost free placeholder label
    for i, placeholder_label in enumerate(placeholder_labels):
        if placeholder_label["text"] == "_":
            break
    else:
        # If there are no free placeholders, return
        return
    
    # Put the letter from the clicked tile into the leftmost free placeholder
    placeholder_label.configure(text=tile_label["text"])
    tile_label.pack_forget()
    
    # Check if all placeholders have been filled
    if all([placeholder_label["text"] != "_" for placeholder_label in placeholder_labels]):
        # If all placeholders are filled, check if the word is correct
        guessed_word = "".join([placeholder_label["text"] for placeholder_label in placeholder_labels])
        if guessed_word == word:
            play_mp3_file('winbanjo-96336.mp3')
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
            play_mp3_file('yay-6326.mp3')
    
    
            
        else:
            print("Sorry, you failed. Try again.")
            play_mp3_file('good-6081.mp3')
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
            '''#engine.say("Sorry, you failed. Try again.")
            # Re-shuffle the tiles
            shuffle(letters)
            for i, tile_label in enumerate(tile_labels):
                tile_label.configure(text=letters[i])
            # Reset the placeholders
            for placeholder_label in placeholder_labels:
                placeholder_label.configure(text="_")'''

# Bind tile label clicks to the on_tile_click function
for tile_label in tile_labels:
    tile_label.bind("<Button-1>", on_tile_click)

# Start the tkinter mainloop
root.mainloop()
