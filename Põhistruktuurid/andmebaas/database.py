import sqlite3

def create_connection():
    conn = sqlite3.connect('movies_normalized.db')
    return conn

def initialize_database():

    conn = create_connection()
    cursor = conn.cursor()

    # Создание таблиц
    tables = {
        'directors': """
            CREATE TABLE IF NOT EXISTS directors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )""",
        'genres': """
            CREATE TABLE IF NOT EXISTS genres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )""",
        'languages': """
            CREATE TABLE IF NOT EXISTS languages (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )""",
        'countries': """
            CREATE TABLE IF NOT EXISTS countries (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL UNIQUE
            )""",
        'movies': """
            CREATE TABLE IF NOT EXISTS movies (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                director_id INTEGER,
                release_year INTEGER,
                genre_id INTEGER,
                duration INTEGER,
                rating REAL,
                language_id INTEGER,
                country_id INTEGER,
                description TEXT,
                FOREIGN KEY (director_id) REFERENCES directors(id),
                FOREIGN KEY (genre_id) REFERENCES genres(id),
                FOREIGN KEY (language_id) REFERENCES languages(id),
                FOREIGN KEY (country_id) REFERENCES countries(id)
            )"""
    }

    for table in tables.values():
        cursor.execute(table)

    # Заполнение начальных данных
    initial_data = {
        'directors': ['Francis Ford Coppola', 'Christopher Nolan', 'Quentin Tarantino',
                      'Steven Spielberg', 'Martin Scorsese'],
        'genres': ['Drama', 'Sci-Fi', 'Crime', 'Adventure', 'Action', 'Thriller', 'Comedy'],
        'languages': ['English', 'Estonian', 'French', 'German', 'Italian'],
        'countries': ['USA', 'UK', 'France', 'Germany', 'Italy', 'Estonia']
    }

    for table, items in initial_data.items():
        cursor.execute(f"SELECT COUNT(*) FROM {table}")
        if cursor.fetchone()[0] == 0:
            for item in items:
                cursor.execute(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (item,))

    conn.commit()
    conn.close()

def get_movies(search_query=""):
    conn = create_connection()
    cursor = conn.cursor()

    query = """
        SELECT m.id, m.title, d.name, m.release_year, g.name, 
               m.duration, m.rating, l.name, c.name, m.description
        FROM movies m
        LEFT JOIN directors d ON m.director_id = d.id
        LEFT JOIN genres g ON m.genre_id = g.id
        LEFT JOIN languages l ON m.language_id = l.id
        LEFT JOIN countries c ON m.country_id = c.id
    """

    params = ()
    if search_query:
        query += " WHERE m.title LIKE ?"
        params = ('%' + search_query + '%',)

    cursor.execute(query, params)
    movies = cursor.fetchall()
    conn.close()

    return movies

def get_dictionary_items(table_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"SELECT name FROM {table_name} ORDER BY name")
    items = []
    rows = cursor.fetchall()
    for row in rows:
        items.append(row[0])
    conn.close()
    return items

def add_dictionary_item(table_name, item_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute(f"INSERT OR IGNORE INTO {table_name} (name) VALUES (?)", (item_name,))
    conn.commit()
    conn.close()
    return cursor.lastrowid

def get_or_create_id(conn, table_name, item_name):
    if not item_name:
        return None

    cursor = conn.cursor()
    cursor.execute(f"SELECT id FROM {table_name} WHERE name=?", (item_name,))
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        cursor.execute(f"INSERT INTO {table_name} (name) VALUES (?)", (item_name,))
        conn.commit()
        return cursor.lastrowid

def add_movie(movie_data):
    conn = create_connection()
    cursor = conn.cursor()

    director_id = get_or_create_id(conn, 'directors', movie_data['director'])
    genre_id = get_or_create_id(conn, 'genres', movie_data['genre'])
    language_id = get_or_create_id(conn, 'languages', movie_data['language'])
    country_id = get_or_create_id(conn, 'countries', movie_data['country'])

    cursor.execute("""
        INSERT INTO movies (title, director_id, release_year, genre_id, 
                          duration, rating, language_id, country_id, description)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        movie_data['title'],
        director_id,
        movie_data['year'],
        genre_id,
        movie_data['duration'],
        movie_data['rating'],
        language_id,
        country_id,
        movie_data['description']
    ))

    conn.commit()
    conn.close()

def update_movie(movie_id, movie_data):
    conn = create_connection()
    cursor = conn.cursor()

    director_id = get_or_create_id(conn, 'directors', movie_data['director'])
    genre_id = get_or_create_id(conn, 'genres', movie_data['genre'])
    language_id = get_or_create_id(conn, 'languages', movie_data['language'])
    country_id = get_or_create_id(conn, 'countries', movie_data['country'])

    cursor.execute("""
        UPDATE movies
        SET title=?, director_id=?, release_year=?, genre_id=?, 
            duration=?, rating=?, language_id=?, country_id=?, description=?
        WHERE id=?
    """, (
        movie_data['title'],
        director_id,
        movie_data['year'],
        genre_id,
        movie_data['duration'],
        movie_data['rating'],
        language_id,
        country_id,
        movie_data['description'],
        movie_id
    ))

    conn.commit()
    conn.close()

def delete_movie(movie_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM movies WHERE id=?", (movie_id,))
    conn.commit()
    conn.close()

