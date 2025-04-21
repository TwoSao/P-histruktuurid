from question import *
from respondents import *
import random

TOTAL_QUESTIONS = 5  # количество вопросов

def main():
    load_question()  # Загружаем вопросы
    load_respondent()  # Загружаем список респондентов
    correct=0
    name = input("Введите ваше имя: ").strip()

    if not add_respondent(name, ""):
        return

    correct = 0
    used_questions = []# Задаем вопросы


    for _ in range(TOTAL_QUESTIONS):
        while True:
            question, answer = select_random_question()

            if question in used_questions:
                continue  # Пропускаем уже заданные вопросы

            used_questions.append(question)
            user_answer = input(f"{name}, {question}: ").strip().lower()

            if user_answer == answer.lower():
                correct += 1
            break

    update_score(name, correct)

    print(f"\n{name}, вы ответили правильно на {correct} из {TOTAL_QUESTIONS} вопросов.")
    if correct > TOTAL_QUESTIONS // 2:
        print("Поздравляем, вы прошли тест успешно!")
    else:
        print("К сожалению, вы не прошли тест.")

if __name__ == "__main__":
    main()
