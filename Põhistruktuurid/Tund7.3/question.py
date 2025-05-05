import json

QUESTION_FILE = "questions.json"
kus_vas = {}

def load_questions():
    global kus_vas
    try:
        with open(QUESTION_FILE, "r", encoding="utf-8") as f:
            kus_vas = json.load(f)
    except FileNotFoundError:
        kus_vas = {}

def save_question():
    with open(QUESTION_FILE, "w", encoding="utf-8") as f:
        json.dump(kus_vas, f, ensure_ascii=False, indent=2)

def add_question():
    question = input("Sisesta uus küsimus: ")
    answer = input("Sisesta õige vastus: ")
    load_questions()
    kus_vas[question] = answer
    save_question()
    print("✅ Küsimus lisatud.")
load_questions()
print(kus_vas)