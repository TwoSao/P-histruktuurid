
logins = []
passwords = []

import random
str0=".,:;!_*-+()/#¤%&"
str1 = '0123456789'
str2 = 'qwertyuiopasdfghjklzxcvbnm'
str3 = str2.upper()

def generate_password(length: int) -> str:
    """
    Parooli genereerimine
    :param int length: Parooli pikkus
    :rtype: str
    """
    password = ''
    for i in range(length):
        if i % 4 == 0:
            password += random.choice(str0)
        elif i % 4 == 1:
            password += random.choice(str1)
        elif i % 4 == 2:
            password += random.choice(str2)
        elif i % 4 == 3:
            password += random.choice(str3)
    return password

def reading():
    while True:
        try:
            login=input('Sisestage kasutajanimi: \nKui soovite tagasi minna, sisestage 0\n')
            
            password=input('Sisestage parool: ')
            print(authorize(login, password))
            if login in logins and password==passwords[logins.index(login)]: break
            elif login=="0": break
        except ValueError:
            print('Viga')
            continue

def writing():
    while True:
        try:
            login=input('Sisestage kasutajanimi: ')
            if login in logins:
                print('Kasutajanimi on juba võetud')
                continue
            while True:
                try:
                    choose=input('Kas soovite genereerida parooli? (1/0) ')
                    if choose in ['1', '0']: break
                except ValueError:
                    print('Viga')
                    continue
            if choose=='1':
                password=generate_password(16)
                print(password)
            else:
                while True:
                    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"

                    password = input('Sisestage parool: ')
                    
                    has_digit = has_upper = has_special = False
                    
                    for c in password:
                        if c.isdigit():
                            has_digit = True
                        elif c.isupper():
                            has_upper = True
                        elif c in special_chars:
                            has_special = True
                    
                    if has_digit and has_upper and has_special:
                        break
                    
                    print('Parool peab sisaldama vähemalt ühte suurt tähte, ühte numbrit ja ühte spetsiaalset märki.')
            print(register(login, password))
            return register(login, password)
        except ValueError:
            print('Viga')
            continue

def register(login: str, password: str) -> str:
    """
    Registreerimine
    :param str login: Kasutajanimi
    :param str password: Parool
    :rtype: str
    """
    if login in logins:
        return 'Kasutajanimi on juba võetud'
    else:
        logins.append(login)
        passwords.append(password)
        return 'Kasutaja on registreeritud'

def authorize(login: str, password: str) -> str:
    """
    Autoriseerimine
    :param str login: Kasutajanimi
    :param str password: Parool
    :rtype: str
    """
    if login in logins:
        if password==passwords[logins.index(login)]:
            return 'Autoriseeritud'
        else:
            return 'Vale parool'
    else:
        return 'Kasutajat ei eksisteeri'


def change_password():
    """Parooli muutmine
    :param str login: Kasutajanimi
    :param str old_password: Vana parool
    :param str new_password: Uus parool
    :rtype: str
    """
    login=input('Sisestage kasutajanimi: ')
    if login in logins:
        old_password=input('Sisestage vana parool: ')
        if old_password==passwords[logins.index(login)]:
            new_password=input('Sisestage uus parool: ')
            passwords[logins.index(login)]=new_password
            return 'Parool on muudetud'
        else:
            return 'Vale parool'
    else:
        return 'Kasutajat ei eksisteeri'
    

def password_recovery():
    """Parooli taastamine
    :param str login: Kasutajanimi
    :param str email: E-mail
    :rtype: str
    """
    login=input('Sisestage kasutajanimi: ')
    if login in logins:
        password=generate_password(16)
        print(f"Uus parool: {password}")
        passwords[logins.index(login)]=password
        return 'Parool on taastatud'
    else:
        print('Kasutajat ei eksisteeri')
        return 'Kasutajat ei eksisteeri'