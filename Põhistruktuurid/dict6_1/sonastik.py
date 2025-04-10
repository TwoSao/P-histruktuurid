
dicts = {"привет": "tere", "спасибо": "aitäh", "пожалуйста": "palun", "да": "jah", "нет": "ei"}
def mainmenu():
    print("1. Translate from Russian to Estonian")
    print("2. Translate from Estonian to Russian")
    print("3. Add new word")
    print("4. Change existing word")
    print("5. Checking correctness of the word")
    choice = input("Enter your choice: ")
    return choice

def translate_rus_to_est():
    word = input("Enter the word in Russian: ")
    if word in dicts:
        print(f"Translation: {dicts[word]}")
    else:
        print("Word not found in the dictionary.")

def translate_est_to_rus():
    word = input("Enter the word in Estonian: ")
    for key, value in dicts.items():
        if value == word:
            print(f"Translation: {key}")
            return
    print("Word not found in the dictionary.")

def add_word():
    rus_word = input("Enter the word in Russian: ")
    est_word = input("Enter the word in Estonian: ")
    dicts[rus_word] = est_word
    print("Word added successfully.")

def change_word():
    word = input("Enter the word to change: ")
    if word in dicts:
        new_word = input("Enter the new word: ")
        dicts[word] = new_word
        print("Word changed successfully.")
    else:
        print("Word not found in the dictionary.")

def testing():
    word = input("Enter the word to check: ")
    if word in dicts or word in dicts.values():
        print("The word is correct.")