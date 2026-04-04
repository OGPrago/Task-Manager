# Task Manager CLI

A simple command-line task manager built with Python. Add, list, complete, and delete tasks — all stored locally in a JSON file.

## Requirements

- Python 3.6+

## Installation

### Option 1 — Install via pip (recommended)

```bash
pip install git+https://github.com/OGPrago/Task-Manager.git
```

Then use `task-manager` from anywhere on your machine.

### Option 2 — Run from source

```bash
git clone https://github.com/OGPrago/Task-Manager.git
cd Task-Manager
python main.py <command>
```

## Usage

```bash
task-manager add "Task title"     # Add a new task
task-manager list                 # List all tasks
task-manager complete <id>        # Mark a task as complete
task-manager delete <id>          # Delete a task
```

### Examples

```bash
$ task-manager add "Go to gym"
Adding Go to gym

$ task-manager add "Buy groceries"
Adding Buy groceries

$ task-manager list
Listing tasks
1. [ ] Go to gym
2. [ ] Buy groceries

$ task-manager complete 1
Task 1 completed

$ task-manager list
Listing tasks
1. [x] Go to gym
2. [ ] Buy groceries

$ task-manager delete 1
Task 1 deleted

$ task-manager list
Listing tasks
1. [ ] Buy groceries
```

## Project Structure

```
Task-Manager/
├── main.py          # Entry point and CLI routing
├── task.py          # Task model
├── storage.py       # JSON persistence layer
├── pyproject.toml   # Package configuration
└── tasks.json       # Local task data (auto-created)
```

## Notes

- Tasks are saved to `tasks.json` in the directory where you run the command.
- Task IDs are automatically resequenced after deletion.
