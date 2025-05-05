from respondents import *
from question import add_question, save_question
load_questions()
load_respondents()
def main():
    M = 3  # mitu inimest

    while True:
        print("\n📋 MENÜÜ:\n1. Alusta küsimustikku\n2. Lisa uus küsimus\n3. Välju")
        while True:
            try:
                valik = input("Vali tegevus: ")
                if valik == "":
                    print("\n📋 MENÜÜ:\n1. Alusta küsimustikku\n2. Lisa uus küsimus\n3. Välju")
                else:
                    break
            except:
                pass

        if valik == "1":
            for i in range(M):
                name = input("Sisesta nimi: ")
                email = input("Sisesta email: ")
                if name in tests:
                    print("❗ See inimene on juba testitud.")
                else:
                    start_quiz(name, email)
        elif valik == "2":
            add_question()
            save_question()
        elif valik == "3":
            break
        else:
            print("❌ Vigane valik.")


if __name__ == "__main__":
    main()
