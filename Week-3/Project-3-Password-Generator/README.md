# Project 3 – Random Password Generator

**Week 3 | DecodeLabs Industrial Training | Batch 2026**

---

## Overview

A command-line Random Password Generator built in Python.
This project represents the **security phase** of the internship. It focuses on Library Integration and String Manipulation — bridging the gap between basic coding and functional security tools by using built-in Python libraries to generate non-predictable, secure data.

---

## Features

| Feature | Description |
|---------|-------------|
| Password Length | Ask the user for desired password length. |
| Numbers Toggle | Option to guarantee at least one number in the password. |
| Symbols Toggle | Option to include special characters like `@`, `#`, `$`. |
| Secure Generation | Uses `random` and `string` modules for complex generation. |

---

## Key Concept – Library Integration

```python
import random
import string

pool = string.ascii_letters + string.digits + string.punctuation
random_char = random.choice(pool)
```

By leveraging `random.choice`, `random.choices`, and `random.shuffle`, this script ensures that the generated string is secure and non-predictable.

---

## How to Run

```bash
python password_generator.py
```

> Requires Python 3.6+. No pip installs needed.

---

*DecodeLabs Industrial Training Kit – Batch 2026*
