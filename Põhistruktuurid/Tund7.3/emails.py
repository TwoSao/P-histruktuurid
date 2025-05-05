import smtplib

def saada_email(saaja, teema, sisu):
    try:
        smtp_server = "smtp.gmail.com"
        smtp_port = 587
        saatja_email = "illyablagun@gmail.com"
        saatja_parool = "xgxi pxhz beoz hwor"

        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(saatja_email, saatja_parool)


        email_message = (
            f"Subject: {teema}\n"
            f"From: {saatja_email}\n"
            f"To: {saaja}\n"
            f"Content-Type: text/plain; charset=utf-8\n\n"
            f"{sisu}" )

        server.sendmail(saatja_email, saaja, email_message.encode('utf-8'))
        server.quit()
        print(f"E-kiri saadetud: {saaja}")
    except Exception as e:
        print(f"Viga e-kirja saatmisel: {e}")
