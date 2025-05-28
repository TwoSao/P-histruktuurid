import tkinter as tk
from tkinter import ttk, messagebox
from database import add_movie, update_movie, get_movies, get_dictionary_items, add_dictionary_item

def open_add_movie_window(tree):
    """Открывает окно для добавления нового фильма"""
    window = tk.Toplevel()
    window.title("Lisa film")

    # Получаем данные для Combobox
    directors = get_dictionary_items('directors')
    genres = get_dictionary_items('genres')
    languages = get_dictionary_items('languages')
    countries = get_dictionary_items('countries')

    # Создаем и размещаем элементы формы
    title_entry = create_form_field(window, "Pealkiri:", 0)
    director_combo = create_combobox_field(window, "Režissöör:", directors, 1,
                                           lambda: add_dictionary_item_and_refresh(
                                               'directors', 'Lisa režissöör', director_combo))
    year_entry = create_form_field(window, "Aasta:", 2)
    genre_combo = create_combobox_field(window, "Žanr:", genres, 3,
                                        lambda: add_dictionary_item_and_refresh(
                                            'genres', 'Lisa žanr', genre_combo))
    duration_entry = create_form_field(window, "Kestus:", 4)
    rating_entry = create_form_field(window, "Reiting:", 5)
    language_combo = create_combobox_field(window, "Keel:", languages, 6,
                                           lambda: add_dictionary_item_and_refresh(
                                               'languages', 'Lisa keel', language_combo))
    country_combo = create_combobox_field(window, "Riik:", countries, 7,
                                          lambda: add_dictionary_item_and_refresh(
                                              'countries', 'Lisa riik', country_combo))
    description_entry = create_text_field(window, "Kirjeldus:", 8)

    # Кнопка сохранения
    tk.Button(window, text="Salvesta",
              command=lambda: save_movie(
                  None,  # Для нового фильма ID нет
                  {
                      'title': title_entry.get(),
                      'director': director_combo.get(),
                      'year': year_entry.get(),
                      'genre': genre_combo.get(),
                      'duration': duration_entry.get(),
                      'rating': rating_entry.get(),
                      'language': language_combo.get(),
                      'country': country_combo.get(),
                      'description': description_entry.get("1.0", tk.END)
                  },
                  window,
                  tree
              )).grid(row=9, column=0, columnspan=3, pady=10)

def open_update_movie_window(tree, movie_id):
    """Открывает окно для редактирования фильма"""
    window = tk.Toplevel()
    window.title("Muuda filmi andmeid")

    # Получаем данные фильма
    movies = get_movies()
    movie_data = next((m for m in movies if m[0] == int(movie_id)), None)

    if not movie_data:
        messagebox.showerror("Viga", "Filmi ei leitud!")
        window.destroy()
        return

    # Получаем данные для Combobox
    directors = get_dictionary_items('directors')
    genres = get_dictionary_items('genres')
    languages = get_dictionary_items('languages')
    countries = get_dictionary_items('countries')

    # Создаем и размещаем элементы формы с текущими данными
    title_entry = create_form_field(window, "Pealkiri:", 0, movie_data[1])
    director_combo = create_combobox_field(window, "Režissöör:", directors, 1,
                                           lambda: add_dictionary_item_and_refresh(
                                               'directors', 'Lisa režissöör', director_combo),
                                           movie_data[2])
    year_entry = create_form_field(window, "Aasta:", 2, movie_data[3])
    genre_combo = create_combobox_field(window, "Žanr:", genres, 3,
                                        lambda: add_dictionary_item_and_refresh(
                                            'genres', 'Lisa žanr', genre_combo),
                                        movie_data[4])
    duration_entry = create_form_field(window, "Kestus:", 4, movie_data[5])
    rating_entry = create_form_field(window, "Reiting:", 5, movie_data[6])
    language_combo = create_combobox_field(window, "Keel:", languages, 6,
                                           lambda: add_dictionary_item_and_refresh(
                                               'languages', 'Lisa keel', language_combo),
                                           movie_data[7])
    country_combo = create_combobox_field(window, "Riik:", countries, 7,
                                          lambda: add_dictionary_item_and_refresh(
                                              'countries', 'Lisa riik', country_combo),
                                          movie_data[8])
    description_entry = create_text_field(window, "Kirjeldus:", 8, movie_data[9])

    # Кнопка сохранения
    tk.Button(window, text="Salvesta",
              command=lambda: save_movie(
                  movie_id,
                  {
                      'title': title_entry.get(),
                      'director': director_combo.get(),
                      'year': year_entry.get(),
                      'genre': genre_combo.get(),
                      'duration': duration_entry.get(),
                      'rating': rating_entry.get(),
                      'language': language_combo.get(),
                      'country': country_combo.get(),
                      'description': description_entry.get("1.0", tk.END)
                  },
                  window,
                  tree
              )).grid(row=9, column=0, columnspan=3, pady=10)

def create_form_field(window, label_text, row, default_value=""):
    """Создает поле формы с меткой"""
    tk.Label(window, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
    entry = tk.Entry(window, width=40)
    entry.grid(row=row, column=1, padx=10, pady=5)
    if default_value:
        entry.insert(0, default_value)
    return entry

def create_combobox_field(window, label_text, values, row, add_callback, default_value=""):
    """Создает поле Combobox с меткой и кнопкой добавления"""
    tk.Label(window, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
    combo = ttk.Combobox(window, values=values, state="readonly", width=37)
    combo.grid(row=row, column=1, padx=10, pady=5)
    if default_value:
        combo.set(default_value)
    tk.Button(window, text="Lisa uus", command=add_callback).grid(row=row, column=2, padx=5)
    return combo

def create_text_field(window, label_text, row, default_value=""):
    """Создает текстовое поле с меткой"""
    tk.Label(window, text=label_text).grid(row=row, column=0, padx=10, pady=5, sticky=tk.W)
    text = tk.Text(window, width=30, height=5)
    text.grid(row=row, column=1, padx=10, pady=5)
    if default_value:
        text.insert("1.0", default_value)
    return text

def add_dictionary_item_and_refresh(table_name, title, combo):
    """Добавляет новый элемент в справочник и обновляет Combobox"""
    from gui_utils import open_add_dictionary_item_window
    open_add_dictionary_item_window(table_name, title, lambda: refresh_combobox(combo, table_name))

def refresh_combobox(combo, table_name):
    """Обновляет данные в Combobox"""
    items = get_dictionary_items(table_name)
    combo['values'] = items

def save_movie(movie_id, movie_data, window, tree):
    """Сохраняет фильм (добавляет новый или обновляет существующий)"""
    # Валидация данных
    if not movie_data['title']:
        messagebox.showerror("Viga", "Pealkiri ei saa olla tühi!")
        return

    try:
        if movie_id is None:
            # Добавляем новый фильм
            add_movie(movie_data)
            messagebox.showinfo("Edu", "Film edukalt lisatud!")
        else:
            # Обновляем существующий фильм
            update_movie(movie_id, movie_data)
            messagebox.showinfo("Edu", "Film edukalt uuendatud!")

        # Обновляем таблицу и закрываем окно
        load_movies_data(tree)
        window.destroy()
    except Exception as e:
        messagebox.showerror("Viga", f"Tekkis viga: {e}")

def load_movies_data(tree, search_query=""):
    """Загружает данные фильмов в таблицу (для обновления после изменений)"""
    movies = get_movies(search_query)
    for item in tree.get_children():
        tree.delete(item)
    for movie in movies:
        tree.insert("", "end", values=movie[1:], iid=movie[0])