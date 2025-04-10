
dicts = {"привет": "tere", "спасибо": "aitäh", "пожалуйста": "palun", "да": "jah", "нет": "ei"}
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
    while True:
        try:
            word = input("Enter the word in Russian: ")
            if not word.isalpha():
                print("Please enter a valid word.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    word = word.lower()
    if word in dicts:
        print(f"Translation: {dicts[word]}")
    else:
        print("Word not found in the dictionary.")

def translate_est_to_rus():
    while True:
        try:
            word = input("Enter the word in Estonian: ")
            if not word.isalpha():
                print("Please enter a valid word.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    word = word.lower()
    for key, value in dicts.items():
        if value == word:
            print(f"Translation: {key}")
            return
    print("Word not found in the dictionary.")

def add_word():
    while True:
        try:
            rus_word = input("Enter the word in Russian: ")
            est_word = input("Enter the word in Estonian: ")
            if not rus_word.isalpha() or not est_word.isalpha():
                print("Please enter valid words.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    dicts[rus_word] = est_word
    print("Word added successfully.")

def change_word():
    while True:
        try:
            word = input("Enter the word to change: ")
            if not word.isalpha():
                print("Please enter a valid word.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")

    if word in dicts:
        new_word = input("Enter the new word: ")
        dicts[word] = new_word
        print("Word changed successfully.")
    else:
        print("Word not found in the dictionary.")

def testing():
    while True:
        try:
            word = input("Enter the word to check: ")
            if not word.isalpha():
                print("Please enter a valid word.")
                continue
            break
        except ValueError:
            print("Invalid input. Please try again.")
    word = word.lower()

    if word in dicts or word in dicts.values():
        print("The word is correct.")