import customtkinter as ctk
from tkinter import Canvas
import pygame
from logic import toggle_osa, salvesta_pilt, max_pildid, indeksid, loenda_pildid
from config import osa_info

def loo_ui(app):
    pygame.mixer.init()
    pygame.mixer.music.load("PhotoRobot/mus.mp3")

    canvas = Canvas(app, width=400, height=500, bg="white")
    canvas.pack(side="right", padx=10, pady=10)

    frame = ctk.CTkFrame(app)
    frame.pack(side="left", padx=10, pady=10)

    label_style = {"font": ("Arial", 16), "text_color": "black"}
    button_style = {
        "width": 150, "height": 40,
        "font": ("Arial", 16),
        "fg_color": "white", "hover_color": "lightblue",
        "corner_radius": 20,
    }

    ctk.CTkLabel(frame, text="Vali näoosad:", **label_style).pack(pady=10)

    for nimi, label in [
        ("frame", "Näokuju"),
        ("kulmud", "Kulmud"),
        ("silma", "Silma"),
        ("nina", "Nina"),
        ("suu", "Suu"),
    ]:
        ctk.CTkButton(frame, text=label, command=lambda n=nimi: toggle_osa(n, canvas, 200, 250), **button_style).pack(pady=5)

    ctk.CTkButton(frame, text="💾 Salvesta", command=lambda: salvesta_pilt(küsi_failinimi()), **button_style).pack(pady=10)

    frame_music = ctk.CTkFrame(frame)
    frame_music.pack(pady=10)
    ctk.CTkButton(frame_music, text="▶ Mängi muusikat", command=lambda: pygame.mixer.music.play(), **button_style).pack(pady=5)
    ctk.CTkButton(frame_music, text="⏸ Paus", command=lambda: pygame.mixer.music.pause(), **button_style).pack(pady=5)

    return canvas

def küsi_failinimi():
    from tkinter import simpledialog
    nimi = simpledialog.askstring("Salvesta pilt", "Sisesta failinimi:")
    return nimi + ".png" if nimi else "salvestatud_robot.png"

def valmistu():
    for nimi, kaust in osa_info.items():
        max_pildid[nimi] = loenda_pildid(kaust)
        indeksid[nimi] = -1
