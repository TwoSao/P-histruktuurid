import json
from datetime import datetime
import os

DRAFTS_FILE = "drafts.json"


def save_draft(email_entry, teema_entry, kiri_entry):
    draft = {
        "to": email_entry.get(),
        "subject": teema_entry.get(),
        "body": kiri_entry.get("1.0", "end-1c"),  # end-1c чтобы убрать лишний перенос
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    try:
        # Загружаем существующие черновики
        drafts = load_drafts()

        # Добавляем новый черновик
        drafts.append(draft)

        # Сохраняем (максимум 10 последних черновиков)
        with open(DRAFTS_FILE, "w") as f:
            json.dump(drafts[-10:], f, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Ошибка сохранения черновика: {e}")

def load_drafts():
    if os.path.exists(DRAFTS_FILE):
        try:
            with open(DRAFTS_FILE, "r") as f:
                return json.load(f)
        except:
            return []
    return []

def restore_last_draft(email_entry, teema_entry, kiri_entry):
    drafts = load_drafts()
    if drafts:
        last = drafts[-1]
        email_entry.delete(0, "end")
        teema_entry.delete(0, "end")
        kiri_entry.delete("1.0", "end")

        email_entry.insert(0, last.get("to", ""))
        teema_entry.insert(0, last.get("subject", ""))
        kiri_entry.insert("1.0", last.get("body", ""))

def clear_last_draft():
    drafts = load_drafts()
    if drafts:
        drafts.pop()  # Удаляем последний черновик
        with open(DRAFTS_FILE, "w") as f:
            json.dump(drafts, f, indent=2, ensure_ascii=False)

def delete_draft_from_file(index):
    drafts = load_drafts()
    if 0 <= index < len(drafts):
        drafts.pop(index)
        try:
            with open(DRAFTS_FILE, 'w') as f:
                json.dump(drafts, f, indent=2)
            return True
        except:
            return False
    return False