from PIL import Image, ImageTk
import os
from config import base_path, osa_info

pildid = {}
tk_pildid = {}
objektid = {}
olemas = {}
indeksid = {}
max_pildid = {}

def loenda_pildid(kaust):
    full_path = os.path.join(base_path, kaust)
    if not os.path.exists(full_path):
        print(f"❌ Kausta ei leitud: {full_path}")
        return 0
    return len([f for f in os.listdir(full_path) if f.endswith(".png")])

def toggle_osa(nimi, canvas, x, y):
    kaust = osa_info[nimi]
    max_index = max_pildid[nimi]
    indeksid[nimi] = (indeksid.get(nimi, -1) + 1) % max_index
    pildi_nimi = f"{indeksid[nimi] + 1}.png"
    path = os.path.join(base_path, kaust, pildi_nimi)

    if not os.path.exists(path):
        print(f"❌ Puudub: {path}")
        return

    pil_img = Image.open(path).convert("RGBA").resize((400, 400))
    tk_img = ImageTk.PhotoImage(pil_img)
    pildid[nimi] = pil_img
    tk_pildid[nimi] = tk_img

    if olemas.get(nimi):
        canvas.itemconfig(objektid[nimi], image=tk_img)
    else:
        objektid[nimi] = canvas.create_image(x, y, image=tk_img)
        olemas[nimi] = True

def salvesta_pilt(filename="salvestatud_robot.png"):
    taust = Image.new("RGBA", (400, 500), "white")
    for nimi in osa_info:
        if olemas.get(nimi):
            taust.alpha_composite(pildid[nimi], (0, 50))
    taust.save(filename)
    print(f"Pilt salvestatud kui {filename}")
