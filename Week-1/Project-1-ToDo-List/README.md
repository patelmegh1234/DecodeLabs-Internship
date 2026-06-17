# Project 1 – To-Do List Application

**Week 1 | DecodeLabs Industrial Training | Batch 2026**

---

## Overview

A command-line To-Do List app built in pure Python — no external libraries needed.  
This is the **logic phase** of the internship: mastering how to store, manage, and persist data programmatically before touching databases or frameworks.

---

## Features

| # | Feature | Python Concept Used |
|---|---------|-------------------|
| 1 | Add a task | `dict` + `list.append()` |
| 2 | View all tasks | `for` loop + f-string formatting |
| 3 | Filter by status | List comprehension |
| 4 | Mark task as Done | Linear search + dict mutation |
| 5 | Delete a task | List comprehension filter |
| 6 | Search by keyword | `str.lower()` + `in` operator |
| 7 | Summary + progress bar | `sum()` + integer math |
| 8 | Data persistence | `json.load()` / `json.dump()` |

---

## How to Run

```bash
python todo.py
```

> Requires Python 3.6+. No pip installs needed.

---

## Data Model

Each task is a **dictionary** (like a database row):

```python
{
    "id"      : 1,
    "title"   : "Finish Python assignment",
    "status"  : "Pending",   # or "Done"
    "created" : "2026-06-16 20:30"
}
```

All tasks live in a **list** (like a database table).  
The list is saved to `tasks.json` on every change — so your data persists between runs.

---

## Key Concept – IPO Model

```
INPUT  ──>  PROCESS  ──>  OUTPUT
(Menu)     (Functions)   (Display)
```

Every operation in this app follows the **Input → Process → Output** pattern, which is the foundation of all backend systems.

---

## Project Structure

```
Project-1-ToDo-List/
├── todo.py       ← main application
└── tasks.json    ← auto-created on first run (do not commit)
```

---

*DecodeLabs Industrial Training Kit – Batch 2026*
