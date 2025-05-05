import random

from Registreerimine_ja_autoriseerimine.My import send_email_notification
from question import kus_vas, load_questions
import json
from emails import saada_email

QUESTION_FILE2="tests.json"


tests = {}
def load_respondents():
    global tests
    try:
        with open(QUESTION_FILE2, "r", encoding="utf-8") as f:
            tests = json.load(f)
    except FileNotFoundError:
        tests = {}
def start_quiz(name, email):
    load_questions()
    N = 5
    selected = random.sample(list(kus_vas.items()), min(N, len(kus_vas)))
    score = 0

    for q, a in selected:
        ans = input(f"{name}, {q} ").strip().lower()
        if ans == a.lower():
            print()
            score += 1

    if score >= N//2:
        print("Поздравляю вы успешно ответили на все вопросы")
        tests[name]=score
        with open(QUESTION_FILE2, "w", encoding="utf-8") as f:
            json.dump(tests, f, ensure_ascii=False, indent=2)

    else:
        print("Вы ответили на меньшинство ответов")
        tests[name]=score
        with open(QUESTION_FILE2, "w", encoding="utf-8") as f:
            json.dump(tests, f, ensure_ascii=False, indent=2)
        saada_email(email, "Teate testi sooritamise kohta", f"{name}:{email}, sooritasite testi edukalt {score} küsimusega {N}")
    return name, email
load_respondents()
print(tests)