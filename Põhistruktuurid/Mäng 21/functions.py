player=""
player_sum=0
from gui import *

def start():
    global player, player_sum
    player = name_entry.get()
    if player == "":
        text_label="Enter your name!"
        Error_label=ttk.Label(frame_game, text=text_label)
        Error_label.pack()
