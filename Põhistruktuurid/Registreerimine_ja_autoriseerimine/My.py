import random
import smtplib
import ssl
from email.message import EmailMessage

logins = []
passwords = []
emails = []

# Генерация пароля
def generate_password(length: int) -> str:
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
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

def load_users():
    try:
        with open("users.txt", "r", encoding="utf-8") as file:
            for line in file:
                login, password, email = line.strip().split(":")
                logins.append(login)
                passwords.append(password)
                emails.append(email)
    except FileNotFoundError:
        pass

def save_users():
    with open("users.txt", "w", encoding="utf-8") as file:
        for login, password, email in zip(logins, passwords, emails):
            file.write(f"{login}:{password}:{email}\n")

# Отправка письма
def send_email_notification(to_email: str, subject: str, content: str):
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    from_email = "illyablagun@gmail.com"
    password = "zqka wgus gobb uyna"

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = from_email
    msg["To"] = to_email
    msg.set_content(content)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(from_email, password)
            server.send_message(msg)
    except Exception as e:
        print("Email saatmine ebaõnnestus:", e)

def authorize(login: str, password: str) -> str:
    if login in logins:
        if password == passwords[logins.index(login)]:
            return 'Autoriseeritud'
        else:
            return 'Vale parool'
    else:
        return 'Kasutajat ei eksisteeri'

def register(login: str, password: str, email: str) -> str:
    if login in logins:
        return 'Kasutajanimi on juba võetud'
    else:
        logins.append(login)
        passwords.append(password)
        emails.append(email)
        save_users()
        send_email_notification(email, "Registreerimine", f"Tere {login}, olete edukalt registreeritud!")
        return 'Kasutaja on registreeritud'

# Смена пароля
def change_password():
    login = input('Sisestage kasutajanimi: ')
    if login in logins:
        old_password = input('Sisestage vana parool: ')
        if old_password == passwords[logins.index(login)]:
            new_password = input('Sisestage uus parool: ')
            passwords[logins.index(login)] = new_password
            save_users()
            send_email_notification(emails[logins.index(login)], "Parooli muutmine", f"Tere {login}, teie parool on edukalt muudetud.")
            return 'Parool on muudetud'
        else:
            return 'Vale parool'
    else:
        return 'Kasutajat ei eksisteeri'

def password_recovery():
    login = input('Sisestage kasutajanimi: ')
    if login in logins:
        new_password = generate_password(16)
        passwords[logins.index(login)] = new_password
        save_users()
        send_email_notification(emails[logins.index(login)], "Parooli taastamine", f"Tere {login}, teie uus parool on: {new_password}")
        print(f"Uus parool: {new_password}")
        return 'Parool on taastatud'
    else:
        print('Kasutajat ei eksisteeri')
        return 'Kasutajat ei eksisteeri'

def reading():
    while True:
        try:
            login = input('Sisestage kasutajanimi: \nKui soovite tagasi minna, sisestage 0\n')
            if login == "0":
                break
            password = input('Sisestage parool: ')
            print(authorize(login, password))
            if login in logins and password == passwords[logins.index(login)]:
                break
        except ValueError:
            print('Viga')
            continue

def writing():
    while True:
        try:
            login = input('Sisestage kasutajanimi: ')
            if login in logins:
                print('Kasutajanimi on juba võetud')
                continue
            email = input('Sisestage oma e-mail: ')
            while True:
                choose = input('Kas soovite genereerida parooli? (1/0) ')
                if choose in ['1', '0']:
                    break
            if choose == '1':
                password = generate_password(16)
                print(password)
            else:
                while True:
                    special_chars = "!@#$%^&*()-_=+[]{}|;:'\",.<>?/`~"
                    password = input('Sisestage parool: ')
                    has_digit = has_upper = has_special = False
                    for c in password:
                        if c.isdigit(): has_digit = True
                        elif c.isupper(): has_upper = True
                        elif c in special_chars: has_special = True
                    if has_digit and has_upper and has_special:
                        break
                    print('Parool peab sisaldama vähemalt ühte suurt tähte, ühte numbrit ja ühte spetsiaalset märki.')
            print(register(login, password, email))
            return
        except ValueError:
            print('Viga')
            continue

# Запуск
load_users()
