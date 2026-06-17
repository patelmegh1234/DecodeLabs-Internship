# -*- coding: utf-8 -*-
"""
========================================================
  DecodeLabs - Python Project 2
  Expense Tracker
  Batch: 2026  |  Junior Developer Track
========================================================

Concepts covered:
  - Math operations & Accumulators (total += new_expense)
  - Continuous data entry loops
  - Data accumulation and processing
"""

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

def show_menu():
    print()
    divider("=")
    print("     DecodeLabs  --  Expense Tracker")
    divider("=")
    print("  1. Add a new expense")
    print("  2. View all expenses")
    print("  3. View total spent")
    print("  4. Exit")
    divider("=")

def add_expense(expenses):
    """
    INPUT   : user types an expense description and amount
    PROCESS : append tuple to list, accumulate total
    OUTPUT  : confirmation
    """
    header("[ + ]  ADD NEW EXPENSE")
    
    desc = input("  Enter expense description (e.g., Lunch, Taxi): ").strip()
    if not desc:
        print("\n  [!] Description cannot be empty.\n")
        return expenses

    try:
        amount = float(input("  Enter amount spent: "))
        if amount <= 0:
            print("\n  [!] Amount must be positive.\n")
            return expenses
    except ValueError:
        print("\n  [!] Please enter a valid number.\n")
        return expenses

    expenses.append({"desc": desc, "amount": amount})
    print(f"\n  [OK] Added {desc}: ${amount:.2f}\n")
    return expenses

def view_expenses(expenses):
    """
    INPUT   : none
    PROCESS : iterate expenses, format output
    OUTPUT  : list of expenses
    """
    header("[LIST]  ALL EXPENSES")
    
    if not expenses:
        print("  No expenses recorded yet.\n")
        return

    print(f"  {'#':<4} {'DESCRIPTION':<30} {'AMOUNT'}")
    divider(".")
    
    for i, exp in enumerate(expenses, 1):
        print(f"  {i:<4} {exp['desc']:<30} ${exp['amount']:.2f}")
    
    divider(".")
    print(f"  Total entries: {len(expenses)}\n")

def view_total(expenses):
    """
    INPUT   : none
    PROCESS : calculate total using accumulator pattern
    OUTPUT  : total spent
    """
    header("[STAT]  TOTAL SPENT")
    
    # Accumulator pattern: total = total + new_expense
    total_spent = 0.0
    for exp in expenses:
        total_spent += exp["amount"]
        
    print(f"  Total amount spent: ${total_spent:.2f}\n")
    print("  Keep track of your budget! 💰\n")

def main():
    """
    Main Program Loop.
    """
    expenses = []
    
    print("\n  Welcome to DecodeLabs Expense Tracker! 📈")
    
    while True:
        show_menu()
        choice = input("  Enter your choice (1-4): ").strip()

        if choice == "1":
            expenses = add_expense(expenses)
        elif choice == "2":
            view_expenses(expenses)
        elif choice == "3":
            view_total(expenses)
        elif choice == "4":
            print("\n  Goodbye! Keep your finances in check.\n")
            break
        else:
            print("\n  [!] Invalid choice. Enter a number between 1 and 4.\n")

if __name__ == "__main__":
    main()
