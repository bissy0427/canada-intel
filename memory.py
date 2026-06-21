import json
import os

MEMORY_FILE = "memory.json"


def load_memory():
    if not os.path.exists(MEMORY_FILE):
        return []
    return json.load(open(MEMORY_FILE))


def save_memory(memory):
    json.dump(memory, open(MEMORY_FILE, "w"))


def add_memory(question, answer):
    memory = load_memory()
    memory.append({"q": question, "a": answer})
    save_memory(memory)


def get_memory():
    return load_memory()
