#Tund1
# Запрашиваем имя пользователя
from re import T


nimi = input("Sisesta oma nimi: ")  # Введите своё имя

# Запрашиваем возраст пользователя
vanus = input("Sisesta oma vanus: ")  # Введите свой возраст

# Выводим приветственное сообщение с именем и возрастом
print(f"Tere, maailm! Tervitan sind {nimi}! Sa oled {vanus} aastat vana.")
# Привет, мир! Приветствую тебя {имя}! Тебе {возраст} лет.
T

#Tund 2
# Определяем переменные
vanus = 18  # Возраст (целое число)
eesnimi = "Jaak"  # Имя (строка)
pikkus = 16.5  # Рост (число с плавающей точкой)
kas_käib_koolis = True  # Ходит ли в школу (логическое значение)

# Проверяем типы переменных
print(type(vanus))  # int (целое число)
print(type(eesnimi))  # str (строка)
print(type(pikkus))  # float (число с плавающей точкой)
print(type(kas_käib_koolis))  # bool (логическое значение)

# Пример: альтернативное значение для переменной "kas_käib_koolis"
kas_käib_koolis = False  # Логическое значение также может быть False
print(type(kas_käib_koolis))  # Проверяем тип переменной

#Tund 3
# Задаём начальное количество конфет на столе
kommide_arv = 10  # На столе 10 конфет
print(f"Laud alguses: {kommide_arv} kommi.")  # Выводим начальное количество конфет

# Запрашиваем у пользователя, сколько конфет он хочет взять
võetud_kummid = int(input("Mitu kommi sa soovid võtta? "))  # Введите количество конфет, которые хотите взять

# Вычитаем количество взятых конфет из общего количества
kommide_arv -= võetud_kummid  # Уменьшаем количество конфет
print(f"Laud nüüd: {kommide_arv} kommi.")  # Выводим оставшееся количество конфет ss