# -*- coding: utf-8 -*-
"""
========================================================
  DecodeLabs - Python Project 3
  Random Password Generator
  Batch: 2026  |  Junior Developer Track
========================================================

Concepts covered:
  - Library Integration (import random, import string)
  - String manipulation and constants
  - Random choice, shuffling
  - User input and validation
"""

import random
import string
import sys

# Fix Windows console so it can display special characters
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")

def divider(char="-", length=56):
    print(char * length)

def header(title):
    print()
    divider("=")
    print("  " + title)
    divider("=")

def get_yes_no(prompt):
    """Utility to safely get a yes/no answer."""
    while True:
        ans = input("  " + prompt + " (y/n): ").strip().lower()
        if ans in ['y', 'yes']:
            return True
        elif ans in ['n', 'no']:
            return False
        else:
            print("  [!] Please enter 'y' or 'n'.")

def generate_password():
    """
    INPUT   : user preferences (length, include numbers, include symbols)
    PROCESS : build character pool, ensure constraints, generate sequence
    OUTPUT  : the generated secure password
    """
    header("[ * ]  GENERATE SECURE PASSWORD")
    
    # 1. Get length
    while True:
        try:
            length = int(input("  Enter desired password length (e.g., 8-32): "))
            if length < 4:
                print("  [!] Password should be at least 4 characters for basic security.")
            else:
                break
        except ValueError:
            print("  [!] Please enter a valid number.")

    # 2. Get preferences
    use_numbers = get_yes_no("Include numbers (0-9)?")
    use_symbols = get_yes_no("Include special characters (@, #, $, etc.)?")

    # 3. Build the character pool
    # Start with lowercase and uppercase letters
    pool = string.ascii_letters
    
    # Ensure at least one character from each requested pool
    guaranteed = []
    
    # We always guarantee at least one lowercase and uppercase to be safe
    guaranteed.append(random.choice(string.ascii_lowercase))
    guaranteed.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        pool += string.digits
        guaranteed.append(random.choice(string.digits))
        
    if use_symbols:
        pool += string.punctuation
        guaranteed.append(random.choice(string.punctuation))

    # 4. Generate the remaining characters
    remaining_length = length - len(guaranteed)
    
    if remaining_length > 0:
        # random.choices picks k items from the pool with replacement
        remaining_chars = random.choices(pool, k=remaining_length)
    else:
        # If length is smaller than our guaranteed list, just truncate the guaranteed list (rare)
        guaranteed = guaranteed[:length]
        remaining_chars = []

    # 5. Combine and shuffle
    password_list = guaranteed + remaining_chars
    random.shuffle(password_list) # Shuffle to avoid predictable patterns
    
    # Convert list back to string
    final_password = "".join(password_list)
    
    print("\n  [OK] Generated Password:")
    divider(" ")
    print(f"       {final_password}")
    divider(" ")
    print("  Keep this safe! 🛡️\n")

def main():
    """
    Main Program Loop.
    """
    print("\n  Welcome to DecodeLabs Password Generator! 🔐")
    
    while True:
        print()
        divider("=")
        print("  1. Generate a new password")
        print("  2. Exit")
        divider("=")
        
        choice = input("  Enter your choice (1-2): ").strip()

        if choice == "1":
            generate_password()
        elif choice == "2":
            print("\n  Goodbye! Stay secure.\n")
            break
        else:
            print("\n  [!] Invalid choice. Enter 1 or 2.\n")

if __name__ == "__main__":
    main()
