import argparse
import storage
import task

def main():
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
    args = parser.parse_args()
    if args.command == "add":
        tasks = storage.load()
        if not tasks:
            new_id = 1
        else:
            new_id = max(tasks, key=lambda task_item: task_item.id).id + 1
        tasks.append(task.Task(new_id, args.title))
        storage.save(tasks)
        print(f"Adding {args.title}")
    elif args.command == "list":
        tasks = storage.load()
        print("Listing tasks")
        for t in tasks:
            print(f"{t.id}. [{"x" if t.completed else " "}] {t.title}")
    elif args.command == "complete":
        tasks = storage.load()
        for t in tasks:
            if t.id == args.id:
                t.completed = True
                storage.save(tasks)
        print(f"Task {args.id} completed")
    elif args.command == "delete":
        tasks = storage.load()
        for t in tasks:
            if t.id == args.id:
                tasks.remove(t)
        for index, item in enumerate(tasks, start=1):
            item.id = index
        storage.save(tasks)
        print(f"Task {args.id} deleted")

if __name__ == "__main__":
    main()