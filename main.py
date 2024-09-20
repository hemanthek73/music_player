import tkinter as tk
import fnmatch
from tkinter import Label
import os
from pygame import mixer
from PIL import Image, ImageTk 
mixer.init()
canvas=tk.Tk()
canvas.title("music player")
canvas.geometry("600x800")
canvas.config(bg="black")
background_image = Image.open("bg.jpg")
background_image = background_image.resize((1920, 1080))  # Resize to fit window
background_photo = ImageTk.PhotoImage(background_image)

# Create a label for the background
background_label =Label(canvas, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
rootpath="C:\\Users\heman\OneDrive\Desktop\music_player"
pattern="*.mp3"
prev_img=tk.PhotoImage(file='prev_img.png')
stop_img=tk.PhotoImage(file='stop_img.png')
play_img=tk.PhotoImage(file='play_img.png')
pause_img=tk.PhotoImage(file='pause_img.png')
next_img=tk.PhotoImage(file='next_img.png')

def select():
  label.config(text=listbox.get("anchor"))
  mixer.music.load(rootpath+"\\"+ listbox.get("anchor"))
  mixer.music.play()

def stop():
  mixer.music.stop()
  listbox.select_clear('active')

def play_next():
    next_song = listbox.curselection()
    next_song = next_song[0] + 1
    if next_song >= listbox.size():
        next_song = 0
    next_song_name = listbox.get(next_song)
    label.config(text=next_song_name)
    mixer.music.load(rootpath + "\\" + next_song_name)
    mixer.music.play()
    listbox.select_clear(0, 'end')
    listbox.activate(next_song)
    listbox.select_set(next_song)


def play_prev():
    prev_song = listbox.curselection()
    prev_song = prev_song[0] - 1
    if prev_song < 0:
        prev_song = listbox.size() - 1
    prev_song_name = listbox.get(prev_song)
    label.config(text=prev_song_name)
    mixer.music.load(rootpath + "\\" + prev_song_name)
    mixer.music.play()
    
    listbox.select_clear(0, 'end')
    listbox.activate(prev_song)
    listbox.select_set(prev_song)


def pause_song():
  if pause_btn["text"]=='Pause':
    mixer.music.pause()
    pause_btn['text']="Play"
  else:
    mixer.music.unpause()
    pause_btn['text']='Pause'

listbox=tk.Listbox(canvas,fg="cyan",bg="black",width=100,font=('poppins',14))
listbox.pack(padx=15,pady=15)

label=tk.Label(canvas,text='',bg='black',fg='yellow',font=('poppins',18))
label.pack(pady=15)

top=tk.Frame(canvas,bg='black')
top.pack(padx=10,pady=5,anchor='center')

prev_btn=tk.Button(canvas,text='Prev',image=prev_img,bg='black',borderwidth=0,command=play_prev)
prev_btn.pack(pady=15,in_=top,side='left')

stop_btn=tk.Button(canvas,text='Stop',image=stop_img,bg='black',borderwidth=0,command=stop)
stop_btn.pack(pady=15,in_=top,side='left')

play_btn=tk.Button(canvas,text='Play',image=play_img,bg='black',borderwidth=0,command=select)
play_btn.pack(pady=15,in_=top,side='left')

pause_btn=tk.Button(canvas,text='Pause',image=pause_img,bg='black',borderwidth=0,command=pause_song)
pause_btn.pack(pady=15,in_=top,side='left')

next_btn=tk.Button(canvas,text='Next',image=next_img,bg='black',borderwidth=0,command=play_next)
next_btn.pack(pady=15,in_=top,side='left')

for rood,dirs,files in os.walk(rootpath):
  for filename in fnmatch.filter(files,pattern):
    listbox.insert("end",filename)

canvas.mainloop()