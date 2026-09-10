# Task Manager CLI

A simple command-line task manager written in Python. Tasks are stored in `tasks.json` (auto-created on first use).

## Usage

    python task_manager.py add <description>
    python task_manager.py list
    python task_manager.py complete <id>
    python task_manager.py delete <id>

## Example

    $ python task_manager.py add Buy milk
    Task added: "Buy milk" (ID: 1)

    $ python task_manager.py list
    [ ] 1: Buy milk

    $ python task_manager.py complete 1
    Task 1 marked as completed.

    $ python task_manager.py list
    [x] 1: Buy milk

## Notes

- Task IDs are auto-assigned (incrementing).
- `[ ]` means pending, `[x]` means completed.
- Data lives in `tasks.json` next to the script.
