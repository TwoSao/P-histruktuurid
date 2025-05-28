import tkinter as tk
from tkinter import ttk, messagebox
from database import get_movies, delete_movie
from gui_add_movie import open_add_movie_window, open_update_movie_window
from gui_utils import open_add_dictionary_item_window


def setup_main_window():
    """Создает и настраивает главное окно приложения"""
    root = tk.Tk()
    root.title("Filmid")
    root.geometry("1000x600")
    root.resizable(False, False)
    center_window(root, 1000, 600)

    # Таблица с фильмами
    tree = setup_movies_table(root)

    # Верхняя панель с поиском и кнопками, передаем tree для доступа
    setup_top_panel(root, tree)

    # Загрузка данных
    load_movies_data(tree)

    return root, tree


def center_window(win, width, height):
    """Центрирует окно на экране"""
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    win.geometry(f"{width}x{height}+{x}+{y}")


def setup_top_panel(root, tree):
    """Настраивает верхнюю панель с поиском и кнопками"""
    top_frame = tk.Frame(root)
    top_frame.pack(pady=10, fill=tk.X, padx=10)

    # Поиск
    search_frame = tk.Frame(top_frame)
    search_frame.pack(side=tk.LEFT, anchor="w")

    tk.Label(search_frame, text="Otsi filmi pealkirja järgi:").pack(side=tk.LEFT)
    search_entry = tk.Entry(search_frame)
    search_entry.pack(side=tk.LEFT, padx=10)

    search_button = tk.Button(search_frame, text="Otsi",
                              command=lambda: on_search(tree, search_entry.get()))
    search_button.pack(side=tk.LEFT)

    # Поиск по Enter
    search_entry.bind("<Return>", lambda event: on_search(tree, search_entry.get()))

    # Кнопки управления
    buttons_frame = tk.Frame(top_frame)
    buttons_frame.pack(side=tk.RIGHT, anchor="e")

    tk.Button(buttons_frame, text="Lisa film",
              command=lambda: open_add_movie_window(tree)).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Uuenda",
              command=lambda: on_update(tree)).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Kustuta",
              command=lambda: on_delete(tree)).pack(side=tk.LEFT, padx=5)

    # Кнопки для справочников
    tk.Button(buttons_frame, text="Lisa režissöör",
              command=lambda: open_add_dictionary_item_window('directors', 'Lisa režissöör')).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Lisa žanr",
              command=lambda: open_add_dictionary_item_window('genres', 'Lisa žanr')).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Lisa keel",
              command=lambda: open_add_dictionary_item_window('languages', 'Lisa keel')).pack(side=tk.LEFT, padx=5)
    tk.Button(buttons_frame, text="Lisa riik",
              command=lambda: open_add_dictionary_item_window('countries', 'Lisa riik')).pack(side=tk.LEFT, padx=5)


def setup_movies_table(root):
    """Настраивает таблицу для отображения фильмов"""
    frame = tk.Frame(root)
    frame.pack(pady=20, fill=tk.BOTH, expand=True, padx=10)

    scrollbar = tk.Scrollbar(frame)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    columns = (
        "title", "director", "year", "genre", "duration", "rating", "language", "country", "description"
    )

    tree = ttk.Treeview(frame, yscrollcommand=scrollbar.set, columns=columns, show="headings")
    tree.pack(fill=tk.BOTH, expand=True)

    scrollbar.config(command=tree.yview)

    # Настройка колонок
    columns_info = [
        ("title", "Pealkiri", 150),
        ("director", "Režissöör", 100),
        ("year", "Aasta", 60),
        ("genre", "Žanr", 100),
        ("duration", "Kestus", 60),
        ("rating", "Reiting", 60),
        ("language", "Keel", 80),
        ("country", "Riik", 80),
        ("description", "Kirjeldus", 200)
    ]

    for col_id, heading, width in columns_info:
        tree.heading(col_id, text=heading)
        tree.column(col_id, width=width, anchor=tk.W)

    return tree


def load_movies_data(tree, search_query=""):
    """Загружает данные фильмов в таблицу"""
    # Очищаем текущие данные
    for item in tree.get_children():
        tree.delete(item)

    # Получаем и отображаем фильмы
    movies = get_movies(search_query)
    for movie in movies:
        tree.insert("", "end", values=movie[1:], iid=movie[0])


def on_search(tree, search_query):
    """Обработчик поиска"""
    load_movies_data(tree, search_query)


def on_update(tree):
    """Обработчик обновления фильма"""
    selected_item = tree.selection()
    if selected_item:
        movie_id = selected_item[0]
        open_update_movie_window(tree, movie_id)
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")


def on_delete(tree):
    """Обработчик удаления фильма"""
    selected_item = tree.selection()
    if selected_item:
        movie_id = selected_item[0]
        confirm = messagebox.askyesno("Kinnita kustutamine", "Kas oled kindel, et soovid selle filmi kustutada?")
        if confirm:
            try:
                delete_movie(movie_id)
                load_movies_data(tree)
                messagebox.showinfo("Edu", "Film edukalt kustutatud!")
            except Exception as e:
                messagebox.showerror("Viga", f"Tekkis viga: {e}")
    else:
        messagebox.showwarning("Valik puudub", "Palun vali kõigepealt rida!")
