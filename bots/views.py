import json
from difflib import get_close_matches
import os
from datetime import datetime
from cloudMixBack.settings import BASE_DIR

def load_knowledge_base(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data


def save_knowledge_base(file_path, data):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=2)


def find_best_match(user_question, questions):
    matches = get_close_matches(user_question, questions, n=1, cutoff=0.6)
    return matches[0] if matches else None


def get_answer_for_question(question, knowledge_base):
    for q in knowledge_base["questions"]:
        if q["question"] == question:
            return q["answer"]


def chat_bot(question):
    knowledge_dir = os.path.join(BASE_DIR, 'bots/knowledge.json')
    knowledge = load_knowledge_base(knowledge_dir)

    best_match = find_best_match(question.lower(), [q["question"] for q in knowledge["questions"]])

    if best_match:
        answer = get_answer_for_question(best_match, knowledge)
        return answer

    return "Sorry, I can't answer"


def create_bot_reply(question):
    answer = chat_bot(question)
    timestamp = datetime.now()
    return {"content": answer, "timestamp": timestamp, "read_status": False, "is_from_bot": True}

