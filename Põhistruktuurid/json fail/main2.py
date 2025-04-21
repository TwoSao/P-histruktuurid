import json

sisestatud_nimi = input("Sisesta oma nimi: ")

with open("json fail/andmed.json", "r", encoding="utf-8") as fail:
    andmed = json.load(fail)

if andmed.get("name") == sisestatud_nimi:
    print(f"\nAutod kasutajal {sisestatud_nimi}:")
    for auto in andmed.get("autod", []):
        print(f"- {auto.get('muudel')} {auto.get('varv')} ({auto.get('joung')}) - Hind: {auto.get('hind')}")
else:
    print("Kasutajat ei leitud.")
