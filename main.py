#!/usr/bin/env python3
import argparse
import storage
import task

def build_parser():
    parser = argparse.ArgumentParser(
        description="A CLI tool to help keep track of your task"
    )
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    subparsers.add_parser("list")
    complete_parser = subparsers.add_parser("complete")
    complete_parser.add_argument("id", type=int)
    delete_parser = subparsers.add_parser("delete")
    delete_parser.add_argument("id", type=int)
    return parser

def handle_list():
    tasks = storage.load()
    print("Listing tasks")
    for t in tasks:
        print(f"{t.id}. [{"x" if t.completed else " "}] {t.title}") 

def handle_add(args):
    tasks = storage.load()
    if not tasks:
        new_id = 1
    else:
        new_id = max(tasks, key=lambda task_item: task_item.id).id + 1
    tasks.append(task.Task(new_id, args.title))
    storage.save(tasks)
    print(f"Adding {args.title}") 
        
def handle_complete(args):
    tasks = storage.load()
    for t in tasks:
        if t.id == args.id:
            t.completed = True
            storage.save(tasks)
    print(f"Task {args.id} completed")
    
def handle_delete(args):
    tasks = storage.load()
    for t in tasks:
        if t.id == args.id:
            tasks.remove(t)
    for index, item in enumerate(tasks, start=1):
        item.id = index
    storage.save(tasks)
    print(f"Task {args.id} deleted")

def main():
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "add":
        handle_add(args)
    elif args.command == "list":
        handle_list()
    elif args.command == "complete":
        handle_complete(args)
    elif args.command == "delete":
        handle_delete(args)

if __name__ == "__main__":
    main()