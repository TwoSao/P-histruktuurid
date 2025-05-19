import tkinter as tk
from tkinter import ttk, messagebox
from Eposti import send_email_notification
from utils import save_draft, load_drafts, restore_last_draft, delete_draft_from_file

themes = {
    "light": {
        "bg": "white",
        "fg": "black",
        "entry_bg": "white",
        "entry_fg": "black",
        "button_bg": "lightgray",
        "text_bg": "white",
        "text_fg": "black"
    },
    "dark": {
        "bg": "#2d2d2d",
        "fg": "white",
        "entry_bg": "#3d3d3d",
        "entry_fg": "white",
        "button_bg": "#4d4d4d",
        "text_bg": "#3d3d3d",
        "text_fg": "white"
    }
}
current_theme = "light"

def showpreview():
    prew = tk.Toplevel()
    prew.title("Preview email")
    prew["bg"] = themes[current_theme]["bg"]
    prew.geometry("600x400")

    body = kiri_entry.get("1.0", tk.END)
    senderE = email_entry.get()
    SenderT = teema_entry.get()

    senderE_label = ttk.Label(prew, text=f"To: {senderE}")
    senderE_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    SenderT_label = ttk.Label(prew, text=f"Subject: {SenderT}")
    SenderT_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    text_frame = ttk.Frame(prew)
    text_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

    SenderK = tk.Text(text_frame, wrap="word", bg=themes[current_theme]["text_bg"], fg=themes[current_theme]["text_fg"])
    SenderK.insert("1.0", body)
    SenderK.config(state="disabled")

    scroll = ttk.Scrollbar(text_frame, command=SenderK.yview)
    scroll.pack(side="right", fill="y")
    SenderK.pack(side="left", fill="both", expand=True)

    btn_close = ttk.Button(prew, text="Close", command=prew.destroy)
    btn_close.grid(row=3, column=0, pady=10)

def setup_autosave():
    save_draft(email_entry, teema_entry, kiri_entry)
    root.after(90000, setup_autosave)

def show_drafts_window():
    drafts_win = tk.Toplevel(root)
    drafts_win.title("Saved Drafts")
    drafts_win.geometry("600x400")
    drafts_win["bg"] = themes[current_theme]["bg"]

    drafts = load_drafts()

    if not drafts:
        ttk.Label(drafts_win, text="No drafts found").pack(pady=20)
        return

    scroll_frame = ttk.Frame(drafts_win)
    scroll_frame.pack(fill="both", expand=True, padx=10, pady=10)

    scrollbar = ttk.Scrollbar(scroll_frame)
    scrollbar.pack(side="right", fill="y")

    draft_list = tk.Listbox(
        scroll_frame,
        yscrollcommand=scrollbar.set,
        width=80,
        font=('Arial', 10),
        bg=themes[current_theme]["text_bg"],
        fg=themes[current_theme]["text_fg"]
    )

    for draft in reversed(drafts):
        preview = f"{draft.get('time','')} | To: {draft.get('to','')} | {draft.get('subject','')}"
        draft_list.insert(tk.END, preview)

    draft_list.pack(fill="both", expand=True)
    scrollbar.config(command=draft_list.yview)

    def load_draft():
        selected = draft_list.curselection()
        if selected:
            idx = len(drafts) - selected[0] - 1
            draft = drafts[idx]

            for widget, key in [
                (email_entry, 'to'),
                (teema_entry, 'subject'),
                (kiri_entry, 'body')
            ]:
                widget.delete(0, tk.END) if key != 'body' else widget.delete('1.0', tk.END)
                widget.insert(0, draft.get(key,'')) if key != 'body' else widget.insert('1.0', draft.get(key,''))

            drafts_win.destroy()

    def delete_draft():
        selected = draft_list.curselection()
        if selected:
            idx = len(drafts) - selected[0] - 1
            if delete_draft_from_file(idx):
                draft_list.delete(selected[0])

    btn_frame = ttk.Frame(drafts_win)
    btn_frame.pack(pady=5)

    buttons = [
        ("Load", load_draft),
        ("Delete", delete_draft),
        ("Close", drafts_win.destroy)
    ]

    for text, command in buttons:
        ttk.Button(btn_frame, text=text, width=10, command=command).pack(side="left", padx=5)

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    theme_btn.config(text="🌙" if current_theme == "dark" else "☀️")
    apply_theme()

def apply_theme():
    theme = themes[current_theme]
    root.config(bg=theme["bg"])
    frame.config(style="TFrame")

    for label in [email_label, teema_label, kiri_label]:
        label.config(style="TLabel")

    email_entry.config(style="TEntry")
    teema_entry.config(style="TEntry")

    kiri_entry.config(
        bg=theme["text_bg"],
        fg=theme["text_fg"],
        insertbackground=theme["fg"]
    )

    for button in [btn_saada, btn_preview, btn_drafts]:
        button.config(style="TButton")

root = tk.Tk()
style = ttk.Style()
style.theme_use("clam")

root.title("E-posti klient")
root.geometry("1980x1080")
root["bg"] = "white"

frame = ttk.Frame(root, padding="10")
frame.pack(fill="both", expand=True)

email_label = ttk.Label(frame, text="E-post:")
email_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

email_entry = ttk.Entry(frame, width=50)
email_entry.grid(row=0, column=1, padx=5, pady=5)

teema_label = ttk.Label(frame, text="Teema:")
teema_label.grid(row=1, column=0, padx=5, pady=5, sticky="w")

teema_entry = ttk.Entry(frame, width=50)
teema_entry.grid(row=1, column=1, padx=5, pady=5)

kiri_label = ttk.Label(frame, text="Kiri:")
kiri_label.grid(row=2, column=0, padx=5, pady=5, sticky="nw")

kiri_entry = tk.Text(frame, width=50, height=10)
kiri_entry.grid(row=2, column=1, padx=5, pady=5)

btn_frame = ttk.Frame(frame)
btn_frame.grid(row=3, column=0, columnspan=2, pady=10, sticky="e")

btn_saada = ttk.Button(btn_frame, text="Saada",
                       command=lambda: send_email_notification(
                           email_entry.get(),
                           teema_entry.get(),
                           kiri_entry.get("1.0", tk.END)
                       ))
btn_saada.pack(side="right", padx=5)

btn_preview = ttk.Button(btn_frame, text="Preview", command=showpreview)
btn_preview.pack(side="right", padx=5)

btn_drafts = ttk.Button(btn_frame, text="Mustandid", command=show_drafts_window)
btn_drafts.pack(side="right", padx=5)

theme_btn = tk.Button(btn_frame, text="☀️", command=toggle_theme, font=("Arial", 12))
theme_btn.pack(side="left", padx=5)

setup_autosave()
restore_last_draft(email_entry, teema_entry, kiri_entry)
root.protocol("WM_DELETE_WINDOW",
              lambda: [save_draft(email_entry, teema_entry, kiri_entry), root.destroy()])
apply_theme()
root.mainloop()