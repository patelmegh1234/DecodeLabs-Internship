# DecodeLabs Internship – Python Developer Track

![Batch](https://img.shields.io/badge/Batch-2026-blue?style=flat-square)
![Track](https://img.shields.io/badge/Track-Junior%20Python%20Developer-green?style=flat-square)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen?style=flat-square)
![Language](https://img.shields.io/badge/Language-Python%203-yellow?style=flat-square)
![Powered By](https://img.shields.io/badge/Powered%20By-DecodeLabs-purple?style=flat-square)

---

## About This Repository

This repository is the complete portfolio of all **4 weekly Python projects** completed during the **DecodeLabs Industrial Training Program (Batch 2026)**.

Each project builds on the previous one — progressing from core data management logic, through numerical processing, into library integration, and finally to building interactive decision engines. Together, they form a structured backend Python foundation.

---

## Progress Timeline

| Week | Theme | Project | Status |
|------|-------|---------|--------|
| [Week 1](./Week-1/) | Python Logic & Data Management | [To-Do List App](./Week-1/Project-1-ToDo-List/) | ✅ Complete |
| [Week 2](./Week-2/) | Data Accumulation & Processing | [Expense Tracker](./Week-2/Project-2-Expense-Tracker/) | ✅ Complete |
| [Week 3](./Week-3/) | Security & Library Integration | [Password Generator](./Week-3/Project-3-Password-Generator/) | ✅ Complete |
| [Week 4](./Week-4/) | Decision Engines & Control Flow | [GK Quiz](./Week-4/Project-4-GK-Quiz/) | ✅ Complete |

---

## Repository Structure

```
DecodeLabs-Internship/
│
├── Week-1/
│   ├── README.md
│   └── Project-1-ToDo-List/
│       ├── todo.py
│       └── README.md
│
├── Week-2/
│   ├── README.md
│   └── Project-2-Expense-Tracker/
│       ├── expense_tracker.py
│       └── README.md
│
├── Week-3/
│   ├── README.md
│   └── Project-3-Password-Generator/
│       ├── password_generator.py
│       └── README.md
│
├── Week-4/
│   ├── README.md
│   └── Project-4-GK-Quiz/
│       ├── quiz.py
│       └── README.md
│
├── .gitignore
└── README.md
```

---

## Project Summaries

### Week 1 — To-Do List App
A full CLI task manager with add, view, filter, mark-done, delete, search, and summary features. Tasks are persisted to a JSON file so data survives between runs.

**Key concepts:** `list.append()`, dictionaries, `json.load/dump`, f-strings, for-loops.

### Week 2 — Expense Tracker
A CLI expense tracker that records descriptions and amounts, then calculates total spending using the **accumulator pattern**.

**Key concepts:** `float()` type casting, `total += amount`, input validation with `try/except`.

### Week 3 — Password Generator
A CLI tool that generates cryptographically-inspired secure passwords of custom length with user-controlled character sets.

**Key concepts:** `import random`, `import string`, `random.choices()`, `random.shuffle()`, `"".join()`.

### Week 4 — General Knowledge Quiz *(Optional Mastery)*
A 5-question quiz engine that implements the IPOS architecture. Every answer is sanitized through a `.strip().lower()` filter pipeline before evaluation.

**Key concepts:** `if/elif/else`, accumulator state management, input sanitization, f-string alignment formatting.

---

## How to Run

> **Requirements:** Python 3.6+ — no external libraries needed for any project.

```bash
# Week 1
cd Week-1/Project-1-ToDo-List
python todo.py

# Week 2
cd Week-2/Project-2-Expense-Tracker
python expense_tracker.py

# Week 3
cd Week-3/Project-3-Password-Generator
python password_generator.py

# Week 4
cd Week-4/Project-4-GK-Quiz
python quiz.py
```

---

## Skills Progression

```
Week 1  →  Lists, Dicts, File I/O, JSON, for-loops
Week 2  →  Math operations, Accumulators, Type casting, try/except
Week 3  →  import random/string, Randomization, String manipulation
Week 4  →  if/elif/else, IPOS architecture, Input sanitization, f-strings
```

---

## Internship Details

| Field | Info |
|-------|------|
| Organization | DecodeLabs |
| Program | Industrial Training Kit |
| Batch | 2026 |
| Role | Junior Python Developer (Intern) |
| Contact | decodelabs.tech@gmail.com |
| Phone | +91 89330 06408 |
| Website | [www.decodelabs.tech](https://www.decodelabs.tech) |
| Location | Greater Lucknow, India |

---

*All projects completed and verified per the DecodeLabs quality standard.*
