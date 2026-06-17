# -*- coding: utf-8 -*-
"""
========================================================
  DecodeLabs - Python Project 1
  To-Do List Application
  Batch: 2026  |  Junior Developer Track
========================================================

Concepts covered:
  - Lists     : dynamic array to store all tasks
  - Dicts     : each task is a structured row (like a DB)
  - File I/O  : JSON persistence (volatile RAM -> permanent disk)
  - Functions : clean IPO separation (Input / Process / Output)
  - Loops     : core Python control flow
  - Search    : substring matching with list comprehension
"""

import os
import sys
import json
from datetime import datetime

# Fix Windows console so it can display special characters
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

# -------------------------------------------------------
#  CONSTANTS
# -------------------------------------------------------

DATA_FILE      = "tasks.json"   # persistence file (disk)
STATUS_PENDING = "Pending"
STATUS_DONE    = "Done"


# -------------------------------------------------------
#  PERSISTENCE LAYER  (disk <-> RAM)
# -------------------------------------------------------

def load_tasks():
    """
    Read tasks from JSON file into a Python list (disk -> RAM).
    Returns an empty list if no file exists yet.
    SQL equivalent: SELECT * FROM tasks
    """
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_tasks(tasks):
    """
    Write the in-memory task list back to disk (RAM -> disk).
    SQL equivalent: COMMIT / full table overwrite
    """
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4, ensure_ascii=False)


# -------------------------------------------------------
#  HELPER UTILITIES
# -------------------------------------------------------

def generate_id(tasks):
    """
    Auto-increment primary key - same idea as SERIAL in SQL.
    Scans the list once to find the current max id.
    """
    if not tasks:
        return 1
    return max(task["id"] for task in tasks) + 1


def get_timestamp():
    """Return current date-time as a readable string."""
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def divider(char="-", length=56):
    print(char * length)


def header(title):
    print()
    divider("=")
    print("  " + title)
    divider("=")


# -------------------------------------------------------
#  CORE OPERATIONS  (Process in IPO)
# -------------------------------------------------------

def add_task(tasks):
    """
    INPUT   : user types a task description
    PROCESS : build a dict (row), append to list (table)
    OUTPUT  : confirmation + new task ID

    Dict structure mirrors a DB table row:
        {
            "id"      : <int>   - unique primary key
            "title"   : <str>   - task description
            "status"  : <str>   - "Pending" or "Done"
            "created" : <str>   - creation timestamp
        }
    """
    header("[ + ]  ADD A NEW TASK")

    title = input("  Enter task description: ").strip()

    if not title:
        print("\n  [!] Task cannot be empty. Try again.\n")
        return tasks

    # Build the task dictionary (= one table row)
    task = {
        "id"      : generate_id(tasks),
        "title"   : title,
        "status"  : STATUS_PENDING,
        "created" : get_timestamp()
    }

    tasks.append(task)   # list.append()  ->  INSERT INTO tasks
    save_tasks(tasks)    # persist        ->  COMMIT

    print(f"\n  [OK] Task #{task['id']} added: \"{task['title']}\"\n")
    return tasks


def view_tasks(tasks, filter_status=None):
    """
    INPUT   : optional status filter
    PROCESS : iterate list, apply filter, format output
    OUTPUT  : tabular display of tasks

    Demonstrates: for-loops, if-conditions, string formatting
    """
    if filter_status:
        header(f"[LIST]  {filter_status.upper()} TASKS")
        display = [t for t in tasks if t["status"] == filter_status]
    else:
        header("[LIST]  ALL TASKS")
        display = tasks

    if not display:
        print("  No tasks found.\n")
        return

    # Table header
    print(f"  {'ID':<5} {'STATUS':<11} {'CREATED':<18} TITLE")
    divider(".")

    # Loop through every task and print a row
    for task in display:
        marker = "[DONE]" if task["status"] == STATUS_DONE else "[    ]"
        print(f"  {task['id']:<5} {task['status']:<11} {task['created']:<18} {marker} {task['title']}")

    divider(".")
    print(f"  Total: {len(display)} task(s)\n")


def mark_done(tasks):
    """
    INPUT   : task ID from user
    PROCESS : linear search the list; update status in dict
    OUTPUT  : success / already-done / not-found message

    Demonstrates: for-loop search, dictionary mutation
    SQL equivalent: UPDATE tasks SET status='Done' WHERE id=?
    """
    header("[OK]  MARK TASK AS DONE")
    view_tasks(tasks, filter_status=STATUS_PENDING)

    try:
        task_id = int(input("  Enter Task ID to mark as Done: "))
    except ValueError:
        print("\n  [!] Please enter a valid number.\n")
        return tasks

    # Linear scan -- O(n) -- like a full table scan without an index
    for task in tasks:
        if task["id"] == task_id:
            if task["status"] == STATUS_DONE:
                print(f"\n  [i] Task #{task_id} is already Done.\n")
            else:
                task["status"] = STATUS_DONE
                save_tasks(tasks)
                print(f"\n  [OK] Task #{task_id} marked as Done!\n")
            return tasks

    print(f"\n  [!] Task #{task_id} not found.\n")
    return tasks


def delete_task(tasks):
    """
    INPUT   : task ID from user (+ confirmation)
    PROCESS : list comprehension to filter out the target row
    OUTPUT  : success / cancelled / not-found message

    SQL equivalent: DELETE FROM tasks WHERE id=?
    """
    header("[X]  DELETE A TASK")
    view_tasks(tasks)

    try:
        task_id = int(input("  Enter Task ID to delete: "))
    except ValueError:
        print("\n  [!] Please enter a valid number.\n")
        return tasks

    # Find the task so we can show its title before deleting
    target = None
    for task in tasks:
        if task["id"] == task_id:
            target = task
            break

    if target is None:
        print(f"\n  [!] Task #{task_id} not found.\n")
        return tasks

    confirm = input(f"  Delete \"{target['title']}\"? Type YES to confirm: ").strip()
    if confirm.upper() == "YES":
        # Build a new list without the deleted item
        tasks = [t for t in tasks if t["id"] != task_id]
        save_tasks(tasks)
        print(f"\n  [X] Task #{task_id} deleted successfully.\n")
    else:
        print("\n  [<] Deletion cancelled.\n")

    return tasks


def search_tasks(tasks):
    """
    INPUT   : keyword string from user
    PROCESS : case-insensitive substring match on all titles
    OUTPUT  : list of matching tasks

    Demonstrates: list comprehension, str.lower(), str.in operator
    SQL equivalent: SELECT * FROM tasks WHERE title LIKE '%keyword%'
    """
    header("[?]  SEARCH TASKS")
    keyword = input("  Enter keyword to search: ").strip().lower()

    if not keyword:
        print("\n  [!] Please enter a keyword.\n")
        return

    # List comprehension with string membership test
    results = [t for t in tasks if keyword in t["title"].lower()]

    if not results:
        print(f"\n  No tasks found matching \"{keyword}\".\n")
        return

    print(f"\n  Found {len(results)} result(s) for \"{keyword}\":\n")
    print(f"  {'ID':<5} {'STATUS':<11} {'CREATED':<18} TITLE")
    divider(".")
    for task in results:
        marker = "[DONE]" if task["status"] == STATUS_DONE else "[    ]"
        print(f"  {task['id']:<5} {task['status']:<11} {task['created']:<18} {marker} {task['title']}")
    divider(".")
    print()


def show_summary(tasks):
    """
    OUTPUT : quick stats using basic aggregation.
    Demonstrates: sum(), conditional expression, division
    """
    header("[STAT]  SUMMARY")

    total   = len(tasks)
    done    = sum(1 for t in tasks if t["status"] == STATUS_DONE)
    pending = total - done

    print(f"  Total tasks  : {total}")
    print(f"  Done         : {done}")
    print(f"  Pending      : {pending}")

    if total > 0:
        pct         = (done / total) * 100
        filled      = int(pct / 5)          # 20-block bar
        empty       = 20 - filled
        bar         = ("#" * filled) + ("-" * empty)
        print(f"\n  Progress: [{bar}] {pct:.0f}%")

    print()


# -------------------------------------------------------
#  MENU  (Input gateway in IPO)
# -------------------------------------------------------

def show_menu():
    print()
    divider("=")
    print("     DecodeLabs  --  To-Do List Application")
    divider("=")
    print("  1. Add a new task")
    print("  2. View all tasks")
    print("  3. View PENDING tasks only")
    print("  4. View DONE tasks only")
    print("  5. Mark a task as Done")
    print("  6. Delete a task")
    print("  7. Search tasks")
    print("  8. Summary / Progress")
    print("  9. Exit")
    divider("=")


# -------------------------------------------------------
#  MAIN PROGRAM LOOP
# -------------------------------------------------------

def main():
    """
    Entry point.
    1. Load persisted tasks from disk into RAM (list of dicts).
    2. Present the menu in an infinite loop.
    3. Route each choice to the correct function.
    4. Every function that mutates data returns the updated list
       and also writes it to disk immediately.
    """
    tasks = load_tasks()

    print()
    print("  Welcome to DecodeLabs To-Do App!")
    print(f"  Loaded {len(tasks)} task(s) from storage.")

    while True:
        show_menu()
        choice = input("  Enter your choice (1-9): ").strip()

        if   choice == "1":
            tasks = add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            view_tasks(tasks, filter_status=STATUS_PENDING)
        elif choice == "4":
            view_tasks(tasks, filter_status=STATUS_DONE)
        elif choice == "5":
            tasks = mark_done(tasks)
        elif choice == "6":
            tasks = delete_task(tasks)
        elif choice == "7":
            search_tasks(tasks)
        elif choice == "8":
            show_summary(tasks)
        elif choice == "9":
            print("\n  Goodbye! Keep building great things.\n")
            break
        else:
            print("\n  [!] Invalid choice. Enter a number between 1 and 9.\n")


# -------------------------------------------------------
#  ENTRY POINT
# -------------------------------------------------------

if __name__ == "__main__":
    main()
