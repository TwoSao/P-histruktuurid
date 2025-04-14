import random

FILENAME = "dictionary.txt"
dicts = {}

def load_dictionary():
    try:
        with open(FILENAME, "r", encoding="utf-8") as f:
            for line in f:
                if ":" in line:
                    rus, est = line.strip().split(":", 1)
                    dicts[rus.strip()] = est.strip()
    except FileNotFoundError:
        print("Dictionary file not found.")

def save_dictionary():
    with open(FILENAME, "w", encoding="utf-8-sig") as f:
        for rus, est in dicts.items():
            f.write(f"{rus}:{est}\n")

def mainmenu():
    print("1. Translate from Russian to Estonian")
    print("2. Translate from Estonian to Russian")
    print("3. Add new word")
    print("4. Change existing word")
    print("5. Checking correctness of the word")
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if choice < 1 or choice > 5:
                print("Please enter a valid choice (1-5).")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 5.")
    return choice

def translate_rus_to_est():
    word = input("Enter the word in Russian: ").lower()
    if word in dicts:
        print(f"Translation: {dicts[word]}")
    else:
        print("Word not found in the dictionary.")

def translate_est_to_rus():
    word = input("Enter the word in Estonian: ").lower()
    for key, value in dicts.items():
        if value == word:
            print(f"Translation: {key}")
            return
    print("Word not found in the dictionary.")

def add_word():
    rus_word = input("Enter the word in Russian: ").lower()
    est_word = input("Enter the word in Estonian: ").lower()
    dicts[rus_word] = est_word
    save_dictionary()
    print("Word added successfully.")

def change_word():
    word = input("Enter the Russian word to change: ").lower()
    if word in dicts:
        new_word = input("Enter the new Estonian translation: ").lower()
        dicts[word] = new_word
        save_dictionary()
        print("Word changed successfully.")
    else:
        print("Word not found in the dictionary.")

def testing():
    if not dicts:
        print("Sõnastik on tühi")
        return
    questions = list(dicts.items())
    random.shuffle(questions)
    correct = 0
    total = len(questions)

    for rus, est in questions:
        answer = input(f"Kuidas tõlgib '{rus}' eesti keelde? ")
        if answer.lower() == est.lower():
            print("Õige!")
            correct += 1
        else:
            print(f"Vale. Õige vastus on: {est}")

    print(f"Test on lõpetatud! Teie tulemus on: {round(correct / total * 100)}%")

load_dictionary()
while True:
    user_choice = mainmenu()
    if user_choice == 1:
        translate_rus_to_est()
    elif user_choice == 2:
        translate_est_to_rus()
    elif user_choice == 3:
        add_word()
    elif user_choice == 4:
        change_word()
    elif user_choice == 5:
        testing()
