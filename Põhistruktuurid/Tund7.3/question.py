import json
question = {}
path="Tund7.3/kusimused_vastused.json"
def save_question():
    with open(path, "w", encoding="utf-8") as file:
        json.dump(question, file, ensure_ascii=False, indent=4)

def load_question():
    global question
    try:
        with open(path, "r", encoding="utf-8") as file:
            question = json.load(file)
    except FileNotFoundError:
        question = {}

def add_question():
    while True:
        try:
            question_text = input("Enter the question(q - exit): ")
            if question_text == "q":
                break
            if question_text == "":
                print("Question cannot be empty.")
                continue
            else:
                answer = input("Enter the answer: ")
                if answer == "":
                    print("Answer cannot be empty.")
                    continue
                else:
                    question[question_text] = answer
                    save_question()
                    print("Question and answer saved successfully.")
                    break

        except Exception as e:
            print(f"An error occurred: {e}")
            break
def select_random_question():
    import random
    if not question:
        print("No questions available.")
        return None
    question_text = random.choice(list(question.keys()))
    answer = question[question_text]
    return question_text, answer