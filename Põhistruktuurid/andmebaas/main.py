import sqlite3
import customtkinter as ctk


create_table_query = """
CREATE TABLE IF NOT EXISTS movies (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    director TEXT,
    release_year INTEGER,
    genre TEXT,
    duration INTEGER,
    rating REAL,
    language TEXT,
    country TEXT,
    description TEXT
);"""

table_insert_query = """
INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description)
VALUES 
('The From In With.', 'Francis Ford Coppola', 1994, 'Drama', 142, 9.3, 'English', 'USA', 'The In With By On. A In From By The At. On A With By By On To A.'),
('The By On To.', 'Christopher Nolan', 2010, 'Sci-Fi', 148, 8.8, 'English', 'UK', 'The A The On The In. By To A At On The. From The In With At In To A.'),
('In The With On.', 'Quentin Tarantino', 1972, 'Crime', 175, 9.2, 'English', 'USA', 'On From The By At The A. In From By With To On. A The By In With At On To A.'),
('The A To From.', 'Steven Spielberg', 1994, 'Adventure', 154, 8.9, 'English', 'France', 'With By In The A On. The With To A At The From. On A From With At By The.'),
('On The From With.', 'Martin Scorsese', 2008, 'Action', 152, 9.0, 'English', 'Germany', 'The A By On In The. At With To A From On The. With On By The A In To From.'),
('From The By With.', 'Christopher Nolan', 1960, 'Drama', 134, 8.5, 'English', 'UK', 'The A On From The At. With To By In A The On. At The In From With By To A.'),
('The By On A.', 'Francis Ford Coppola', 1999, 'Thriller', 112, 7.8, 'English', 'USA', 'A The On By In The At. From With A On By To The. In The By With At A From.'),
('On A The From.', 'Quentin Tarantino', 2015, 'Comedy', 126, 7.9, 'English', 'Italy', 'By With A On In The From. The By At A With On To. At In The By From With A.'),
('By The On From.', 'Steven Spielberg', 1975, 'Action', 143, 8.7, 'English', 'France', 'A With On The By From In. The A At On With To From. By In The A From With At On.'),
('From With The By.', 'Martin Scorsese', 1980, 'Crime', 163, 9.1, 'English', 'Germany', 'On The A By In The From. With By On A The In From. To The In At By With On A.');
"""

def create_table():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Andmebaas ühendatud")
        cursor.execute(create_table_query)
        print("Tabel loodud või juba olemas")
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasi loomisel või andmete sisestamisel:", error)
    finally:
        if conn:
            conn.close()
            print("Andmebaas suletud")

def insert_table():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Andmebaas ühendatud")
        cursor.execute(table_insert_query)
        conn.commit()
        print("Andmed sisestatud")
    except sqlite3.Error as error:
        print("Tekkis viga andmete sisestamisel:", error)
    finally:
        if conn:
            conn.close()
            print("Andmebaas suletud")

def loe_tabel():
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        print("Andmebaas ühendatud")
        cursor.execute("SELECT * FROM movies")
        rows = cursor.fetchall()
        for row in rows:
            print(row)
    except sqlite3.Error as error:
        print("Tekkis viga andmebaasi lugemisel:", error)
    finally:
        if conn:
            conn.close()
            print("Andmebaas suletud")

def clear_entries(entries):
    for entry in entries.values():
        entry.delete(0, ctk.END)

def validate_data(entries):
    for label, entry in entries.items():
        if not entry.get():
            print(f"{label} ei saa olla tühi")
            return False
    return True

def insert_data(entries):
    if not validate_data(entries):
        return

    values = [entries[label].get() for label in entries]
    try:
        conn = sqlite3.connect('movies.db')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO movies (title, director, release_year, genre, duration, rating, language, country, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            values
        )
        conn.commit()
        print("Kasutaja andmed lisatud")
    except sqlite3.Error as error:
        print("Viga kasutaja andmete sisestamisel:", error)
    finally:
        if conn:
            conn.close()

def add_data():
    global entries

    root = ctk.CTk()
    root.title("Movie Database")
    root.geometry("500x750")

    ctk.CTkLabel(root, text="Movie Database GUI", font=("Arial", 20)).pack(pady=20)

    form_frame = ctk.CTkFrame(root)
    form_frame.pack(pady=10)

    labels = ["Pealkiri", "Režissöör", "Väljalaskeaasta", "Žanr", "Kestus", "Hinne", "Keel", "Riik", "Kirjeldus"]
    db_fields = ["title", "director", "release_year", "genre", "duration", "rating", "language", "country", "description"]
    entries = {}

    for i, label in enumerate(labels):
        ctk.CTkLabel(form_frame, text=label).grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entry = ctk.CTkEntry(form_frame)
        entry.grid(row=i, column=1, padx=10, pady=5)
        entries[db_fields[i]] = entry

    ctk.CTkButton(root, text="Sisesta", command=lambda: insert_data(entries)).pack(pady=10)
    ctk.CTkButton(root, text="Loo tabel", command=create_table).pack(pady=5)
    ctk.CTkButton(root, text="Sisesta andmed", command=insert_table).pack(pady=5)
    ctk.CTkButton(root, text="Näita andmeid", command=loe_tabel).pack(pady=5)
    ctk.CTkButton(root, text="Puhasta väljad", command=lambda: clear_entries(entries)).pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    add_data()