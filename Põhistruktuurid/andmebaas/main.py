from database import initialize_database
from gui_main import setup_main_window

def main():
    # Инициализация базы данных
    initialize_database()

    # Создание и запуск главного окна
    root, tree = setup_main_window()
    root.mainloop()

if __name__ == "__main__":
    main()