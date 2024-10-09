# music_player.py

import os
import random
import pygame

# Initialize pygame mixer
pygame.mixer.init()

# Global variables
playlist = []
current_song_index = 0
paused = False

# Functions
def load_songs(files):
    global playlist
    playlist = list(files)  # Store the list of songs from the form
    return playlist

def play_song():
    global paused, current_song_index
    if playlist:
        pygame.mixer.music.load(playlist[current_song_index])
        pygame.mixer.music.play(loops=0)
        paused = False
        return os.path.basename(playlist[current_song_index])

def pause_song():
    global paused
    if not paused:
        pygame.mixer.music.pause()
        paused = True
    else:
        pygame.mixer.music.unpause()
        paused = False
    return paused

def stop_song():
    pygame.mixer.music.stop()

def next_song():
    global current_song_index
    if current_song_index < len(playlist) - 1:
        current_song_index += 1
    else:
        current_song_index = 0
    return play_song()

def prev_song():
    global current_song_index
    if current_song_index > 0:
        current_song_index -= 1
    else:
        current_song_index = len(playlist) - 1
    return play_song()

def recommend_song():
    return random.choice(playlist) if playlist else None
