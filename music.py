import os
import pygame
import random
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk 

# Initialize pygame mixer
pygame.mixer.init()

# Initialize the main window
root = Tk()
root.title("Python Music Player")
root.geometry("700x600")#500x400
background_image = Image.open("bg.jpg")
background_image = background_image.resize((1920, 1080))  # Resize to fit window
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background
background_label = Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Global variables
playlist = []
current_song_index = 0
paused = False

# Functions
def load_songs():
    files = filedialog.askopenfilenames(initialdir="C:/Users/heman/OneDrive/Desktop/music_player/", title="Select Music Files", filetypes=(("mp3 Files", "*.mp3"),))
    for file in files:
        playlist.append(file)
    update_playlist_display()

def play_song():
    global paused
    if playlist:
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play(loops=0)
        song_label.config(text=os.path.basename(playlist[current_song_index]))
        paused = False

def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    play_song()

def prev_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
    else:
        current_song_index = len(playlist) - 1
    play_song()

def update_playlist_display():
    playlist_box.delete(0, END)
    for song in playlist:
        playlist_box.insert(END, os.path.basename(song))

def recommend_song():
    recommended_song = random.choice(playlist)
    messagebox.showinfo("Recommended Song", f"How about playing: {os.path.basename(recommended_song)}?")

custom_font = ("Helvetica", 25, "bold italic") 
# UI Elements

song_label = Label(root, text="No song playing", font=custom_font, fg="black", bg="lightblue")
song_label.pack(pady=30)

custom_font1 = ("Helvetica", 12, "bold italic")
playlist_box = Listbox(root, bg="black", fg="white", width=70, height=20,font=custom_font1)
playlist_box.pack(pady=20)

controls_frame = Frame(root,bg="lightgray")
controls_frame.pack(pady=20)

load_button = Button(root,bg="blue", fg="white", text="Load Songs", command=load_songs ,width=16, height=2,font=custom_font1)

load_button.pack()

play_button = Button(controls_frame,bg="green", fg="black", text="Play", command=play_song,width=16, height=2,font=custom_font1)
play_button.grid(row=0, column=0, padx=5)

pause_button = Button(controls_frame,bg="yellow", fg="black", text="Pause", command=pause_song,width=16, height=2,font=custom_font1)
pause_button.grid(row=0, column=1, padx=5)

stop_button = Button(controls_frame,bg="red", fg="black", text="Stop", command=stop_song,width=16, height=2,font=custom_font1)
stop_button.grid(row=0, column=2, padx=5)

prev_button = Button(controls_frame,bg="skyblue", fg="black", text="Prev", command=prev_song,width=16, height=2,font=custom_font1)
prev_button.grid(row=0, column=3, padx=5)

next_button = Button(controls_frame,bg="skyblue", fg="black", text="Next", command=next_song,width=16, height=2,font=custom_font1)
next_button.grid(row=0, column=4, padx=5)

recommend_button = Button(root, text="Recommend a Song", command=recommend_song ,width=16, height=2,font=custom_font1)
recommend_button.pack(pady=5)

# Start the main loop
root.mainloop()
