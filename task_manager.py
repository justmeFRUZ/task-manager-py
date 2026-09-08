import json
import os
import sys


TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)

    else:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def main():
    if len(sys.argv) < 2:
        print("Usage: python task_manager.py <command>")
        return

    command = sys.argv[1]

    if command == "add":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py add <description>")
            return
        description = " ".join(sys.argv[2:])

        tasks = load_tasks()

        new_id = max([t["id"] for t in tasks], default=0) + 1
        tasks.append({"id": new_id, "description": description, "completed": False})

        save_tasks(tasks)
        print(f'Task added: "{description}" (ID: {new_id})')


    elif command == "list":
        tasks = load_tasks()
        if not tasks:
            print("No tasks found.")
            return
        for t in tasks:
            status = "[x]" if t["completed"] else "[ ]"
            print(f"{status} {t['id']}: {t['description']}")


    elif command == "complete":
        if len(sys.argv) < 3:
            print("Usage python task_manager complete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be a number.")
            return


        tasks = load_tasks()
        found = False
        for t in tasks:
            if t["id"] == task_id:
                t["completed"] = True
                found = True
                break


        if not found:
            print(f"Error: No task with ID {task_id}")
            return

        save_tasks(tasks)
        print(f"Task {task_id} marked as complete.")
        
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Usage: python task_manager.py delete <id>")
            return
        try:
            task_id = int(sys.argv[2])
        except ValueError:
            print("Error: ID must be a number.")
            return


        tasks = load_tasks()

        original_len = len(tasks)
        tasks = [t for t in tasks if t["id"] != task_id]

        if len(tasks) == original_len:
            print(f"Error: No task with  ID {task_id}.")
            return

        save_tasks(tasks)
        print(f"Task {task_id} deleted.")    

if __name__ == "__main__":
    main()