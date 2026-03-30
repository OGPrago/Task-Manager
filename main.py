import argparse
import storage
import task

def main():
    parser = argparse.ArgumentParser(
        description="Print Hello"
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
        existing_task = storage.load()
        if not existing_task:
            new_id = 1
        else:
            new_id = max(existing_task, key=lambda t: t.id).id + 1
        existing_task.append(task.Task(new_id, args.title))
        storage.save(existing_task)
        print(f"Adding {args.title}")
    elif args.command == "list":
        load_existing_task = storage.load()
        print("Listing tasks")
        for i in load_existing_task:
            print(f"{i.id}. [{"x" if i.completed else " "}] {i.title}")
    elif args.command == "complete":
        load_existing_task = storage.load()
        for i in load_existing_task:
            if i.id == args.id:
                i.completed = True
                storage.save(load_existing_task)
        print(f"Task {args.id} completed")
    elif args.command == "delete":
        load_existing_task = storage.load()
        for i in load_existing_task:
            if i.id == args.id:
                load_existing_task.remove(i)
                storage.save(load_existing_task)
        print(f"Task {args.id} deleted")

if __name__ == "__main__":
    main()