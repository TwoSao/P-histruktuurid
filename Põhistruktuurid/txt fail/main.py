def failist_to_dict(f: str):
    riik_pealinn = {}  # sinastik riik : pealinn
    pealinn_riik = {}  # sinastik pealinn : riik
    riigid = []  # järjend kus talletakse riigide nimetused
    with open(f, 'r', encoding="utf-8-sig") as file:
        for line in file:
            k, v = line.strip().split('-')  # k - ключ, v - значение
            riik_pealinn[k] = v  # täidame riik_pealinn
            pealinn_riik[v] = k  # täidame pealinn_riik
            riigid.append(k)  
    return riik_pealinn, pealinn_riik, riigid

riik_pealinn, pealinn_riik, riigid = failist_to_dict('tund7.txt')

# print("riik_pealinn :", riik_pealinn)
# print("pealinn_riik :", pealinn_riik)

def kirjuta_failisse(f: str, riik_pealinn: dict):
    """Muudatuste salvestamine faili.
    """
    with open(f, 'w', encoding="utf-8-sig") as file:
        for riik, pealinn in riik_pealinn.items():
            file.write(f"{riik}-{pealinn}\n")

def find_riigid_pealinn(riik_pealinn, pealinn_riik, filename):
    """Näita pealinna riigi nime järgi või vastupidi.
    """
    find = input("Sisestage riigi või pealinna nimi: ")
    if find in riik_pealinn:
        print(f"Riiklik pealinn {find}: {riik_pealinn[find]}")
    elif find in pealinn_riik:
        print(f"Riik, mille pealinn on {find}: {pealinn_riik[find]}")
    else:
        print("See riik või pealinn ei ole nimekirjas!")
        add = input("Kas soovite selle nimekirja lisada? (jah/ei): ")
        if add == "jah":
            if find not in riik_pealinn and find not in pealinn_riik:
                if input("Kas see on riik? (jah/ei): ").strip().lower() == "jah":
                    new_capital = input("Sisestage riigi pealinn: ").strip()
                    riik_pealinn[find] = new_capital
                    pealinn_riik[new_capital] = find
                    kirjuta_failisse(filename, riik_pealinn)  # save
                    print("Lisatud!")
                else:
                    new_country = input("Sisestage riigi pealinn: ")
                    pealinn_riik[find] = new_country
                    riik_pealinn[new_country] = find
                    kirjuta_failisse(filename, riik_pealinn)  # save
                    print("Lisatud!")

def fix_errors(riik_pealinn, pealinn_riik, filename):
    """Sõnaraamatu vigade parandamine.
    """
    a = input("Sisestage riik või pealinn, mida soovite parandada: ")
    if a in riik_pealinn:
        print(f"Riigi praegune pealinn {a}: {riik_pealinn[a]}")
        new_capital = input("Sisestage uus pealinn: ")
        old_capital = riik_pealinn[a]
        riik_pealinn[a] = new_capital
        del pealinn_riik[old_capital]
        pealinn_riik[new_capital] = a
        kirjuta_failisse(filename, riik_pealinn) # save
        print("Fixed!")
    elif a in pealinn_riik:
        print(f"Praegune pealinna riik {a}: {pealinn_riik[a]}")
        new_country = input("Sisestage uus riik ").strip()
        old_country = pealinn_riik[a]
        pealinn_riik[a] = new_country
        del riik_pealinn[old_country]
        riik_pealinn[new_country] = a
        kirjuta_failisse(filename, riik_pealinn) # save
        print("Fixed!")
    else:
        print("See riik või pealinn ei ole nimekirjas!")

f = 'txt fail/riigid_pealinnad.txt'
riik_pealinn, pealinn_riik, _ = failist_to_dict(f)

while True:
    print("Menüü:")
    print("1. Leia pealinn või riik")
    print("2. Paranda viga")
    print("3. Välju")
    choice = input("Valige tegevus: ")

    if choice == "1":
        find_riigid_pealinn(riik_pealinn, pealinn_riik, f)
    elif choice == "2":
        fix_errors(riik_pealinn, pealinn_riik, f)
    elif choice == "3":
        print("Head aega!")
        break
    else:
        print("Vale valik. Proovige uuesti.")