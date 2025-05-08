
import tkinter as tk
from  tkinter import ttk
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
    prew["bg"] = "white"
    prew.geometry("600x400")

    body = kiri_entry.get("1.0", tk.END)
    senderE = email_entry.get()
    SenderT = teema_entry.get()

    senderE_label = tk.Label(prew, text=f"To: {senderE}", bg="white", anchor="w")
    senderE_label.grid(row=0, column=0, sticky="w", padx=10, pady=5)

    SenderT_label = tk.Label(prew, text=f"Subject: {SenderT}", bg="white", anchor="w")
    SenderT_label.grid(row=1, column=0, sticky="w", padx=10, pady=5)

    text_frame = tk.Frame(prew, bd=1, relief="solid", bg="white")
    text_frame.grid(row=2, column=0, sticky="nsew", padx=10, pady=5)

    SenderK = tk.Text(text_frame, wrap="word", bg="white")
    SenderK.insert("1.0", body)
    SenderK.config(state="disabled")  # Только для чтения

    scroll = tk.Scrollbar(text_frame, command=SenderK.yview)
    scroll.pack(side="right", fill="y")
    SenderK.pack(side="left", fill="both", expand=True)

    btn_close = tk.Button(prew, text="Close", command=prew.destroy)
    btn_close.grid(row=3, column=0, pady=10)

def setup_autosave():
    save_draft(email_entry, teema_entry, kiri_entry)
    root.after(90000, setup_autosave)

def show_drafts_window():

    drafts_win = tk.Toplevel(root)
    drafts_win.title("Saved Drafts")
    drafts_win.geometry("600x400")

    drafts = load_drafts()

    if not drafts:
        tk.Label(drafts_win, text="No drafts found", pady=20).pack()
        return

    scroll_frame = tk.Frame(drafts_win)
    scroll_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    scrollbar = tk.Scrollbar(scroll_frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    draft_list = tk.Listbox(
        scroll_frame,
        yscrollcommand=scrollbar.set,
        width=80,
        font=('Arial', 10)
    )

    # Display newest drafts first
    for draft in reversed(drafts):
        preview = f"{draft.get('time','')} | To: {draft.get('to','')} | {draft.get('subject','')}"
        draft_list.insert(tk.END, preview)

    draft_list.pack(fill=tk.BOTH, expand=True)
    scrollbar.config(command=draft_list.yview)

    # Button functions
    def load_draft():
        selected = draft_list.curselection()
        if selected:
            idx = len(drafts) - selected[0] - 1  # Reverse index
            draft = drafts[idx]

            # Clear and populate fields
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
            if delete_draft_from_file(idx):  # Implement this in utils.py
                draft_list.delete(selected[0])

    # Button panel
    btn_frame = tk.Frame(drafts_win)
    btn_frame.pack(pady=5)

    buttons = [
        ("Load", load_draft),
        ("Delete", delete_draft),
        ("Close", drafts_win.destroy)
    ]

    for text, command in buttons:
        tk.Button(
            btn_frame,
            text=text,
            width=10,
            command=command
        ).pack(side=tk.LEFT, padx=5)

def delete_draft(listbox, drafts):
    selection = listbox.curselection()
    if selection:
        draft_index = len(drafts) - selection[0] - 1
        if delete_draft(draft_index):
            listbox.delete(selection[0])

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    theme_btn.config(text="🌙" if current_theme == "dark" else "☀️")
    apply_theme()

def apply_theme():
    theme = themes[current_theme]

    root.config(bg=theme["bg"])
    frame.config(bg=theme["bg"])

    for label in [email_label, teema_label, kiri_label]:
        label.config(bg=theme["bg"], fg=theme["fg"])

    email_entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])
    teema_entry.config(bg=theme["entry_bg"], fg=theme["entry_fg"])

    kiri_entry.config(
        bg=theme["text_bg"],
        fg=theme["text_fg"],
        insertbackground=theme["fg"]
    )

    # Кнопки
    for button in [btn_saada, btn_preview, btn_drafts, theme_btn]:
        button.config(bg=theme["button_bg"], fg=theme["fg"])

root = tk.Tk()
root.title("E-posti klient")
root.geometry("600x400")
root["bg"] = "white"



frame = tk.Frame(root, bg="lightblue")
frame.pack(pady=10, padx=10, fill="both", expand=True)

email_label = tk.Label(frame, text="E-post:", bg="white")
email_label.grid(row=0, column=0, padx=5, pady=5)
email_label.config(font=("Arial", 12))

email_entry = tk.Entry(frame, width=50, bg="white")
email_entry.grid(row=0, column=1, padx=5, pady=5)

teema_label = tk.Label(frame, text="Teema:", bg="white")
teema_label.grid(row=1, column=0, padx=5, pady=5)
teema_label.config(font=("Arial", 12))

teema_entry = tk.Entry(frame, width=50, bg="white")
teema_entry.grid(row=1, column=1, padx=5, pady=5)

kiri_label = tk.Label(frame, text="Kiri:", bg="white")
kiri_label.grid(row=2, column=0, padx=5, pady=5)
kiri_label.config(font=("Arial", 12))

kiri_entry = tk.Text(frame, width=50, height=10, bg="white")
kiri_entry.grid(row=2, column=1, padx=5, pady=5)

btn_frame = tk.Frame(root, bg="white")
btn_frame.pack()
btn_saada = tk.Button(btn_frame, text="Saada", bg="green", command=lambda: send_email_notification(email_entry.get(), teema_entry.get(), kiri_entry.get("1.0", tk.END)))
btn_saada.grid(row=3, column=3, padx=5, pady=5, sticky="e")

btn_preview = tk. Button(btn_frame, text="Preview", bg="gray", command=lambda: showpreview())
btn_preview.grid(row=3, column=2, padx=5, pady=5, sticky="e")

btn_drafts = tk.Button(btn_frame, text="Mustandid", bg="lightgray", command=show_drafts_window)
btn_drafts.grid(row=3, column=1, padx=5, pady=5, sticky="w")

theme_btn = tk.Button(
    btn_frame,
    text="☀️",
    command=toggle_theme,
    font=("Arial", 12))
theme_btn.grid(row=3, column=0, sticky="w", padx=5, pady=5)


setup_autosave()
restore_last_draft(email_entry, teema_entry, kiri_entry)
root.protocol("WM_DELETE_WINDOW",
              lambda: [save_draft(email_entry, teema_entry, kiri_entry), root.destroy()])
apply_theme()
root.mainloop()


