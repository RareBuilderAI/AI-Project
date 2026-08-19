import json

def load_memory():
    try:
        with open("memory.json", "r") as file:
            return json.load(file)

    except FileNotFoundError:
        return {"message": "No memory found yet"}


memory = load_memory()

print(memory)