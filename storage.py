from task import Task
import json

def load():
    try:
        with open("task.json", 'r') as file:
            data_list = json.load(file)
            converted_data_list = []
            for i in data_list:
                converted_data_list.append(Task.from_dict(i))
            return converted_data_list
    except(FileNotFoundError, json.JSONDecodeError):
        return []

def save(tasks):
    with open("task.json", 'w') as file:
        converted_list = [task.to_dict() for task in tasks]
        json.dump(converted_list, file, indent=2)