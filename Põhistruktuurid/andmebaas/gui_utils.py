import tkinter as tk
from tkinter import messagebox
from database import add_dictionary_item, get_dictionary_items

def open_add_dictionary_item_window(table_name, title, callback=None):
    """Открывает окно для добавления элемента в справочник"""
    window = tk.Toplevel()
    window.title(title)

    tk.Label(window, text=f"{title.split()[-1]}:").pack(pady=5)
    entry = tk.Entry(window)
    entry.pack(pady=5)

    def save_item():
        item_name = entry.get()
        if item_name:
            try:
                add_dictionary_item(table_name, item_name)
                if callback:
                    callback()
                window.destroy()
                messagebox.showinfo("Edu", "Andmed edukalt lisatud!")
            except Exception as e:
                messagebox.showerror("Viga", f"Tekkis viga: {e}")
        else:
            messagebox.showerror("Viga", "Nimi ei saa olla tühi!")

    tk.Button(window, text="Salvesta", command=save_item).pack(pady=10)