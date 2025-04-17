import smtplib
import ssl
from email.message import EmailMessage
from tkinter import Tk, filedialog

email_subject= "Email test from python"
sender_email_address="illyablagun@gmail.com"
receiver_email_address="illyablagun@gmail.com"

def saada_kiri():
    kellele=input("Kellele saata:")
    teema=input("Teema: ")
    sisu=input("Sisu: ")
    smtp_server="smtp.gmail.com"
    smtp_port=587
    kellelt="illyablagun@gmail.com"
    password=input("Password from email: ")
    msg=EmailMessage()
    msg["Subject"]=teema
    msg["From"]=kellelt
    msg["To"]=kellele
    msg.set_content(sisu)

    fail=filedialog.askopenfilename(title="Vali fail", filetypes=[("All files", "*.*")])
    with open(fail,"rb") as f:
        faili_sisu=f.read()
        faili_nimi=fail.split("/")[-1]
        msg.add_attachment(faili_sisu, maintype="application", subtype="octet-stream", filename=faili_nimi)
    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, password)
            server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga: ", e)


import smtplib
import ssl
from email.message import EmailMessage

def htmlmsg():
    kellele = input("Kellele saata: ")
    smtp_server = "smtp.gmail.com"
    smtp_port = 587
    kellelt = "illyablagun@gmail.com"
    password = input("Password from email: ")

    msg = EmailMessage()
    msg["Subject"] = "HTML kiri"
    msg["From"] = kellelt
    msg["To"] = kellele

    with open("meassege.html", "r", encoding="utf-8") as file:
        file_content = file.read()

    msg.add_alternative(file_content, subtype='html')

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls(context=ssl.create_default_context())
            server.login(kellelt, password)
            server.send_message(msg)
        print("Kiri saadetud")
    except Exception as e:
        print("Viga:", e)

htmlmsg()
