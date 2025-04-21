
import json
import os

path = "respondents.json"
respondents = {}
def save_respondent():
    with open(path, "w", encoding="utf-8") as file:
        json.dump(respondents, file, ensure_ascii=False, indent=4)

def load_respondent():
    global respondents
    try:
        with open(path,"r", encoding="utf-8") as file:
            respondents=json.load(file)
    except FileNotFoundError:
        respondents = {}

def is_respondent_processed(name):
    for respondent in respondents:
        if respondent["name"].lower() == name.lo    wer():
            return True
    return False

def add_respondent(name, email):
    if is_respondent_processed(name):
        print("❗ Этот человек уже проходил тест.")
        return False
    respondents["name"]=name
    respondents["email"]=email
    save_respondent()
    return True

def update_score(name, correct):
    for respondent in respondents:
        if respondent["name"].lower() == name.lower():
            respondent["correct"] = correct
            break
    save_respondent()
