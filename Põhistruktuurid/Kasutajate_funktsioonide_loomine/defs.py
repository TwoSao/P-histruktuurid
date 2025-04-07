import datetime

def arithmetic(arv1: float, arv2: float, tehe: str) -> any:
    """
    Lihtne kalkulaator
    + - liitmine
    - - lahutamine
    * - korrutamine
    / - jagamine
    :param float arv1: Esimene arv
    :param float arv2: Teine arv
    :param str tehe: Tehe
    :rtype: Määrata tüüp(tekst, arv, jne)
    """
    
    if tehe in ['+', '-', '*', '/']:
        if arv2 == 0 and tehe == '/':
            return 'Nulliga ei saa jagada'
        if tehe == '+':
            vastus = arv1 + arv2
            return vastus
        elif tehe == '-':
            vastus = arv1 - arv2
            return vastus
        elif tehe == '*':
            vastus = arv1 * arv2
            return vastus
        elif tehe == '/':
            vastus = arv1 / arv2
            return vastus
    else:
        return "Неизвестная операция"

def is_year_leap(year: int) -> bool:
    """ 
    Kontrollib, kas aasta on liigaasta
    :param int year: Aasta
    :rtype: bool
    """
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def square(a: float) -> tuple:
    """
    Ruudu omadused
    :param float a: Ruudu külg
    :rtype: tuple
    """
    perimeter = 4 * a
    area = a ** 2
    diagonal = (2 * (a ** 2)) ** 0.5
    return perimeter, area, diagonal

def square_list(külg: float) -> list:
    """
    Ruudu omadused
    :param float külg: Ruudu külg
    :rtype: list
    """
    perimeter = 4 * külg
    area = külg ** 2
    diagonal = (2 * (külg ** 2)) ** 0.5
    return [perimeter, area, diagonal]

def season(month: int) -> str:
    """
    Määrab aastaaja kuu järgi
    :param int month: Kuu number
    :rtype: str
    """
    if month in [12, 1, 2]:
        return "talv"
    elif month in [3, 4, 5]:
        return "kevad"
    elif month in [6, 7, 8]:
        return "suvi"
    elif month in [9, 10, 11]:
        return "sügis"
    else:
        return "Vigane kuu"

def bank(a: float, years: int) -> float:
    """
    Arvutab summa pangakontol pärast teatud aastate möödumist
    :param float a: Esialgne summa
    :param int years: Aastate arv
    :rtype: float
    """
    for _ in range(years):
        a += a * 0.1
    return a

def is_prime(n: int) -> bool:
    """
    Kontrollib, kas arv on algarv
    :param int n: Arv
    :rtype: bool
    """
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def date(day: int, month: int, year: int) -> bool:
    """
    Kontrollib, kas kuupäev on kehtiv
    :param int day: Päev
    :param int month: Kuu
    :param int year: Aasta
    :rtype: bool
    """
    try:
        datetime.datetime(year, month, day)
        return True
    except ValueError:
        return False

def XOR_cipher(text: str, key: str) -> str:
    """
    XOR krüpteerimine
    :param str text: Tekst
    :param str key: Võti
    :rtype: str
    """
    encrypted = ""
    for i in range(len(text)):
        encrypted += chr(ord(text[i]) ^ ord(key[i % len(key)]))
    return encrypted

def XOR_uncipher(encrypted_text: str, key: str) -> str:
    """
    XOR dekrüpteerimine
    :param str encrypted_text: Krüpteeritud tekst
    :param str key: Võti
    :rtype: str
    """
    decrypted = ""
    for i in range(len(encrypted_text)):
        decrypted += chr(ord(encrypted_text[i]) ^ ord(key[i % len(key)]))
    return decrypted