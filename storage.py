from task import Task
import json

def load():
    try:
        with open("task.json", 'r') as file:
            raw_tasks = json.load(file)
            return [Task.from_dict(item) for item in raw_tasks]
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save(tasks):
    with open("task.json", 'w') as file:
        json.dump([task.to_dict() for task in tasks], file, indent=2)