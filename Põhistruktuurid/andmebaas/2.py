import tkinter as tk
from tkinter import ttk, messagebox
import customtkinter as ctk
import sqlite3
import subprocess

# Avab lisamise faili
entries = {}
def add_data():
    subprocess.run(['python', 'andmebaas/main.py'])


# Otsingufunktsioon
def on_search():
    search_query = search_entry.get()
    load_data_from_db(tree, search_query)

# Funktsioon, mis laadib andmed SQLite andmebaasist ja sisestab need Treeview tabelisse
def load_data_from_db(tree, search_query=""):
    for item in tree.get_children():
        tree.delete(item)

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()

    if search_query:
        cursor.execute("""
            SELECT id, title, director, release_year, genre, duration, rating, language, country, description
            FROM movies
            WHERE title LIKE ?
        """, ('%' + search_query + '%',))
    else:
        cursor.execute("""
            SELECT id, title, director, release_year, genre, duration, rating, language, country, description
            FROM movies
        """)

    rows = cursor.fetchall()
    for row in rows:
        tree.insert("", "end", values=row[1:], iid=row[0])

    conn.close()

# Funktsioon, mis näitab valitud rea ID-d ja avab muutmise vormi
def on_update():
    selected_item = tree.selection()
    if selected_item:
        record_id = selected_item[0]
        open_update_window(record_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

# Funktsioon, mis avab uue akna andmete muutmiseks
def open_update_window(record_id):
    update_window = tk.Toplevel(root)
    update_window.title("Muuda filmi andmeid")

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        SELECT title, director, release_year, genre, duration, rating, language, country, description
        FROM movies
        WHERE id=?
    """, (record_id,))
    record = cursor.fetchone()
    conn.close()

    labels = ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]
    entries = {}

    for i, label in enumerate(labels):
        tk.Label(update_window, text=label).grid(row=i, column=0, padx=10, pady=5, sticky=tk.W)
        entry = tk.Entry(update_window, width=50)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entry.insert(0, record[i])
        entries[label] = entry

    save_button = tk.Button(update_window, text="Salvesta", command=lambda: update_record(record_id, entries, update_window))
    save_button.grid(row=len(labels), column=0, columnspan=2, pady=10)

# Funktsioon, mis uuendab andmed andmebaasis
def update_record(record_id, entries, window):
    data = [entries[label].get() for label in ["Pealkiri", "Režissöör", "Aasta", "Žanr", "Kestus", "Reiting", "Keel", "Riik", "Kirjeldus"]]

    conn = sqlite3.connect('movies.db')
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE movies
        SET title=?, director=?, release_year=?, genre=?, duration=?, rating=?, language=?, country=?, description=?
        WHERE id=?
    """, (*data, record_id))
    conn.commit()
    conn.close()

    load_data_from_db(tree)
    window.destroy()
    messagebox.showinfo("Salvestamine", "Andmed on edukalt uuendatud!")

# Ühendatud funktsioon kustutamiseks
def on_delete():
    selected_item = tree.selection()
    if selected_item:
        record_id = selected_item[0]
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle rea kustutada?")
        if confirm:
            try:
                conn = sqlite3.connect('movies.db')
                cursor = conn.cursor()
                cursor.execute("DELETE FROM movies WHERE id=?", (record_id,))
                conn.commit()
                conn.close()
                load_data_from_db(tree)
                messagebox.showinfo("Edukalt kustutatud", "Rida on edukalt kustutatud!")
            except sqlite3.Error as e:
                messagebox.showerror("Viga", f"Andmebaasi viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")

root = tk.Tk()
root.title("Filmid")
root.geometry("1000x600")

top_frame = tk.Frame(root)
top_frame.pack(pady=10, fill=tk.X, padx=10)

search_frame = tk.Frame(top_frame)
search_frame.pack(side=tk.LEFT, anchor="w")

search_label = tk.Label(search_frame, text="Otsi filmi pealkirja järgi:")
search_label.pack(side=tk.LEFT)

search_entry = tk.Entry(search_frame)
search_entry.pack(side=tk.LEFT, padx=10)

search_button = tk.Button(search_frame, text="Otsi", command=on_search)
search_button.pack(side=tk.LEFT)

buttons_frame = tk.Frame(top_frame)
buttons_frame.pack(side=tk.RIGHT, anchor="e")

open_button = tk.Button(buttons_frame, text="Lisa andmeid", command=add_data)
open_button.pack(side=tk.LEFT, padx=5)

update_button = tk.Button(buttons_frame, text="Uuenda", command=on_update)
update_button.pack(side=tk.LEFT, padx=5)

delete_button = tk.Button(buttons_frame, text="Kustuta", command=on_delete)
delete_button.pack(side=tk.LEFT, padx=5)

frame = tk.Frame(root)
frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=10)
scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=(
    "title", "director", "year", "genre", "duration", "rating", "language", "country", "description"), show="headings")
tree.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=tree.yview)

tree.heading("title", text="Pealkiri")
tree.heading("director", text="Režissöör")
tree.heading("year", text="Aasta")
tree.heading("genre", text="Žanr")
tree.heading("duration", text="Kestus")
tree.heading("rating", text="Reiting")
tree.heading("language", text="Keel")
tree.heading("country", text="Riik")
tree.heading("description", text="Kirjeldus")

tree.column("title", width=150)
tree.column("director", width=100)
tree.column("year", width=60)
tree.column("genre", width=100)
tree.column("duration", width=60)
tree.column("rating", width=60)
tree.column("language", width=80)
tree.column("country", width=80)
tree.column("description", width=200)

load_data_from_db(tree)

root.mainloop()