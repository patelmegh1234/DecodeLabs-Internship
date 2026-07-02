# -*- coding: utf-8 -*-
"""
========================================================
  DecodeLabs - Python Project 4
  General Knowledge Quiz
  Batch: 2026  |  Optional Mastery Phase
========================================================

Architecture: IPOS (Input, Process, Output, Storage)
Core Concept: Decision Engine -- if/elif/else control flow

Each question follows the 4-step "Question Block":
  1. Ask & Capture   (input)
  2. Sanitize Data   (.strip().lower())
  3. Evaluate        (== comparison)
  4. Execute & State (if/else + score += 1)
"""

import sys

# Fix Windows console encoding
if sys.platform == "win32":
    sys.stdout.reconfigure(encoding="utf-8")


# -------------------------------------------------------
#  QUIZ BANK
#  Each entry is a dict: question, answer, hint
#  Easy to extend -- just add more dicts to this list.
# -------------------------------------------------------

QUESTIONS = [
    {
        "question" : "What is the capital of France?",
        "answer"   : "paris",
        "hint"     : "City of Light"
    },
    {
        "question" : "What is the largest planet in our solar system?",
        "answer"   : "jupiter",
        "hint"     : "Named after the king of the Roman gods"
    },
    {
        "question" : "Who wrote the Harry Potter series?",
        "answer"   : "j.k. rowling",
        "hint"     : "British author, initials J.K."
    },
    {
        "question" : "How many continents are there on Earth?",
        "answer"   : "7",
        "hint"     : "Think Asia, Africa, North America..."
    },
    {
        "question" : "What gas do plants absorb from the atmosphere?",
        "answer"   : "carbon dioxide",
        "hint"     : "Used during photosynthesis (CO2)"
    },
]


# -------------------------------------------------------
#  HELPER UTILITIES
# -------------------------------------------------------

def divider(char="-", length=56):
    print(char * length)


def display_result(score, total):
    """
    OUTPUT phase of IPOS.
    Uses f-strings with alignment syntax exactly as specified.
    """
    print()
    divider("=")
    print(f"  QUIZ COMPLETE -- FINAL RESULTS")
    divider("=")
    # f-string with right-aligned score using format spec
    print(f"  Score : {score:>2} / {total}")
    print(f"  Pct   : {(score / total * 100):>5.1f}%")
    divider("-")

    # elif chain to handle every score scenario (no silent logic gaps)
    if score == total:
        print("  [**] PERFECT! Outstanding performance!")
    elif score >= total * 0.8:
        print("  [OK] Excellent! Almost there.")
    elif score >= total * 0.6:
        print("  [OK] Good effort! Keep learning.")
    elif score >= total * 0.4:
        print("  [--] Keep practicing, you can do better!")
    else:
        print("  [--] Don't give up -- review and try again.")

    divider("=")
    print()


# -------------------------------------------------------
#  QUESTION BLOCK  (the 4-step micro-architecture)
# -------------------------------------------------------

def ask_question(number, q_data):
    """
    Implements the full 4-step Question Block for one question.

    Step 1 -- Ask & Capture  : input()
    Step 2 -- Sanitize Data  : .strip().lower()
    Step 3 -- Evaluate       : == (equality / boolean gate)
    Step 4 -- Execute        : if/else + return 1 or 0
    """
    print(f"\n  Q{number}. {q_data['question']}")
    print(f"  (Hint: {q_data['hint']})")

    # Step 1: Ask & Capture
    raw_input = input("  Your answer: ")

    # Step 2: Sanitize Data -- Whitespace Audit + Data Normalization
    # .strip() removes leading/trailing whitespace
    # .lower() normalises casing (avoids "Paris" != "paris" problem)
    sanitized = raw_input.strip().lower()

    correct = q_data["answer"]

    # Step 3 & 4: Evaluate then Execute
    if sanitized == correct:
        print("  [Correct!]")
        return 1   # success path -- increment score vault
    else:
        print(f"  [Incorrect. Answer: {correct.title()}]")
        return 0   # failure path -- state unchanged


# -------------------------------------------------------
#  MAIN PROGRAM
# -------------------------------------------------------

def run_quiz():
    """
    Orchestrates the full quiz session.

    IPOS Mapping:
      I -- user answers captured per question
      P -- equality comparison + conditional routing
      O -- formatted score display with f-strings
      S -- score integer maintained in memory (state)
    """
    divider("=")
    print("       DecodeLabs -- General Knowledge Quiz")
    divider("=")
    print(f"  Total Questions : {len(QUESTIONS)}")
    print("  Instructions    : Type your answer and press Enter.")
    print("  Note            : Answers are NOT case-sensitive.")
    divider("=")

    # STATE INITIALIZATION -- Score Vault (Type Integrity: integer)
    score = 0

    # Loop through every question in the bank
    for i, q_data in enumerate(QUESTIONS, start=1):
        score += ask_question(i, q_data)

    # Deliver Results
    display_result(score, len(QUESTIONS))


# -------------------------------------------------------
#  ENTRY POINT
# -------------------------------------------------------

if __name__ == "__main__":
    run_quiz()
