import random

words = ["õun", "banaan", "kirss", "kuupäev", "leedripuu"]

secret_word = random.choice(words)
word_length = len(secret_word)
print("Sõna on valitud!", "-" * word_length)

attempts = 6

colors = {"green": "\033[92m", "yellow": "\033[93m", "reset": "\033[0m"}

while attempts > 0:
    print("Sul on", attempts, "katset jäänud")
    guess = input("Sisesta sõna: ").lower()
    
    if len(guess) != word_length:
        print(f"Sõna peab olema {word_length} tähemärki pikk!")
        continue
    
    if guess == secret_word:
        print("Õnnitleme, arvasite sõna ära!")
        print("Sõna oli:", secret_word)
        break
    
    highlighted_guess = []
    for i in range(word_length):
        if guess[i] == secret_word[i]:
            highlighted_guess.append(f"{colors['green']}{guess[i]}{colors['reset']}")
        elif guess[i] in secret_word:
            highlighted_guess.append(f"{colors['yellow']}{guess[i]}{colors['reset']}")
        else:
            highlighted_guess.append(guess[i])
    
    print(" ".join(highlighted_guess))
    attempts -= 1

else:
    print("Sa kaotasid!")
    print("Õige sõna oli:", secret_word)
