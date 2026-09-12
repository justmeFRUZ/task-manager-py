import json
import os
import sys
import argparse


TASKS_FILE = "tasks.json"

def load_tasks(path=TASKS_FILE):
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)

    else:
        return []


def save_tasks(tasks, path=TASKS_FILE):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def add_task(description, path=TASKS_FILE):
    tasks = load_tasks(path)
    new_id = max([t["id"] for t in tasks], default=0) + 1
    tasks.append({"id": new_id, "description": description, "completed": False})
    save_tasks(tasks, path)
    return new_id



def list_tasks(path=TASKS_FILE):
    return load_tasks(path)

def main():
    parser = argparse.ArgumentParser(description="Task manager CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", nargs="+", help="Task description")

    parser_list = subparsers.add_parser("list", help="List all tasks")

    parser_complete = subparsers.add_parser("complete", help="Mark a task as completed")
    parser_complete.add_argument("id", type=int, help="Task ID")

    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")

    args = parser.parse_args()

    if args.command == "add":
        description = " ".join(args.description)
        new_id = add_task(description)
        print(f'Task added: "{description}" (ID: {new_id})')

    elif args.command == "list":
        tasks = list_tasks()
        if not tasks:
            print("No tasks found.")
            return
        for t in tasks:
            status = "[x]" if t["completed"] else "[ ]"
            print(f"{status} {t['id']}: {t['description']}")

    elif args.command == "complete":
        task_id = args.id
        tasks = load_tasks()
        found = False
        for t in tasks:
            if t["id"] == task_id:
                t["completed"] = True
                found = True
                break
        if not found:
            print(f"Error: No task with ID {task_id}.")
            return
        save_tasks(tasks)
        print(f"Task {task_id} marked as completed.")

    elif args.command == "delete":
        task_id = args.id
        tasks = load_tasks()
        original_len = len(tasks)
        tasks = [t for t in tasks if t["id"] != task_id]
        if len(tasks) == original_len:
            print(f"Error: No task with ID {task_id}.")
            return
        save_tasks(tasks)
        print(f"Task {task_id} deleted.")

if __name__ == "__main__":
    main()