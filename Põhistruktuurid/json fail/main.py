import requests
import json
linn = input("Sisesta linna nimi: ").strip()

if not linn:
    print("Linna nimi ei tohi olla tühi.")
else:
    api_key = "9047111acd0af1c8a3ebede3007620c8"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={linn}&appid={api_key}&units=metric&lang=et"

    try:
        vastus = requests.get(url)
        andmed = vastus.json()

        if andmed.get("cod") != "404":
            peamine = andmed["main"]
            temperatuur = round(peamine["temp"], 1)
            niiskus = peamine["humidity"]
            kirjeldus = andmed["weather"][0]["description"]
            tuul = andmed["wind"]["speed"]

            print(f"\nIlm linnas {linn.capitalize()}:")
            print(f"Temperatuur: {temperatuur}°C")
            print(f"Kirjeldus: {kirjeldus.capitalize()}")
            print(f"Niiskus: {niiskus}%")
            print(f"Tuule kiirus: {tuul} m/s")
        else:
            print("Linna ei leitud. Palun kontrolli nime õigekirja.")
    except requests.exceptions.RequestException:
        print("Viga võrguühenduse loomisel. Palun kontrolli internetiühendust.")
