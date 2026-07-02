# Project 4 – General Knowledge Quiz

**Week 4 | DecodeLabs Industrial Training | Batch 2026 | Optional Mastery Phase**

---

## Overview

A command-line General Knowledge Quiz engine built in pure Python.
This is the **Optional Mastery Phase** — proving you can build interactive **Decision Engines** that fork, evaluate, and react to human input in real-time, rather than just writing static line-by-line scripts.

---

## Features

| Feature | Description |
|---------|-------------|
| 5-question quiz bank | Questions cover geography, science, and culture |
| Input sanitization | `.strip()` + `.lower()` applied to every answer |
| Score tracking | Integer accumulator incremented per correct answer |
| Granular feedback | Correct answer revealed on wrong responses |
| Final grade report | Formatted with f-strings and percentage score |

---

## The 4-Step Question Block

Every question in this quiz follows the same micro-architecture:

```
Step 1 -- Ask & Capture   →  input()
Step 2 -- Sanitize Data   →  .strip().lower()
Step 3 -- Evaluate        →  answer == correct_answer
Step 4 -- Execute & State →  if/else + score += 1
```

---

## DecodeLabs Verification Checklist

| Requirement | Implementation |
|-------------|---------------|
| Logic Consistency | All branches covered — no silent logic gaps |
| Whitespace Audit | `.strip()` on every `input()` call |
| Data Normalization | `.lower()` applied uniformly |
| Type Integrity | `score = 0` — explicit integer initialization |
| Output Clarity | f-strings with alignment spec `f'{score:>2}'` |

---

## How to Run

```bash
python quiz.py
```

> Requires Python 3.6+. No pip installs needed.

---

## IPOS Architecture

```
INPUT   →  User answer via input()
PROCESS →  Sanitize + equality check (== logic gate)
OUTPUT  →  Correct/Incorrect feedback + final score
STORAGE →  score integer maintained in memory (state)
```

---

*DecodeLabs Industrial Training Kit – Batch 2026*
