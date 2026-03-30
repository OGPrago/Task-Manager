# Task Manager CLI

A simple command-line task manager built with Python. Add, list, complete, and delete tasks — all stored locally in a JSON file.

## Requirements

- Python 3.6+

## Installation

```bash
git clone https://github.com/OGPrago/Task-Manager.git
cd task-manager
```

No dependencies to install — uses Python's standard library only.

## Usage

```bash
python main.py add "Task title"     # Add a new task
python main.py list                 # List all tasks
python main.py complete <id>        # Mark a task as complete
python main.py delete <id>          # Delete a task
```

### Examples

```bash
$ python main.py add "Go to gym"
Adding Go to gym

$ python main.py add "Buy groceries"
Adding Buy groceries

$ python main.py list
Listing tasks
1. [ ] Go to gym
2. [ ] Buy groceries

$ python main.py complete 1
Task 1 completed

$ python main.py list
Listing tasks
1. [x] Go to gym
2. [ ] Buy groceries

$ python main.py delete 1
Task 1 deleted

$ python main.py list
Listing tasks
1. [ ] Buy groceries
```

## Project Structure

```
task-manager/
├── main.py        # Entry point and CLI routing
├── task.py        # Task model
├── storage.py     # JSON persistence layer
└── tasks.json     # Local task data (auto-created)
```

## Notes

- Tasks are saved to `tasks.json` in the project directory.
- Task IDs are automatically resequenced after deletion.
