import argparse

def main():
    parser = argparse.ArgumentParser(
        description="Print Hello"
    )
    subparsers = parser.add_subparsers(dest="command")
    add_parser = subparsers.add_parser("add")
    add_parser.add_argument("title")
    subparsers.add_parser("list")
    args = parser.parse_args()
    if args.command == "add":
        print(f"Adding {args.title}")
    elif args.command == "list":
        print("Listing tasks")

if __name__ == "__main__":
    main()