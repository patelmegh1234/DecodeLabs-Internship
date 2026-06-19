# Project 4: The General Knowledge Quiz
# Industrial Training Kit - 2026 Batch | DecodeLabs
# A "Decision Engine" that evaluates user responses and maintains system state

# ============================================================================
# STATE INITIALIZATION: Score Vault
# ============================================================================
score = 0

print("=" * 60)
print("GENERAL KNOWLEDGE QUIZ")
print("=" * 60)
print("Answer 3 questions. You get +1 point for each correct answer.\n")

# ============================================================================
# QUESTION 1: The Capital of France
# ============================================================================
print("Question 1: What is the capital of France?")

# Step 1: Ask & Capture (Input)
user_answer_1 = input("Your answer: ")

# Step 2: Sanitize Data (Filter Pipeline)
user_answer_1 = user_answer_1.strip().lower()

# Step 3: Evaluate (The Logic Gate)
correct_answer_1 = "paris"

# Step 4: Execute & State Management
if user_answer_1 == correct_answer_1:
    print("✓ Correct!\n")
    score += 1
else:
    print(f"✗ Incorrect. The correct answer is: {correct_answer_1}\n")

# ============================================================================
# QUESTION 2: The Largest Planet in Our Solar System
# ============================================================================
print("Question 2: What is the largest planet in our solar system?")

# Step 1: Ask & Capture (Input)
user_answer_2 = input("Your answer: ")

# Step 2: Sanitize Data (Filter Pipeline)
user_answer_2 = user_answer_2.strip().lower()

# Step 3: Evaluate (The Logic Gate)
correct_answer_2 = "jupiter"

# Step 4: Execute & State Management
if user_answer_2 == correct_answer_2:
    print("✓ Correct!\n")
    score += 1
else:
    print(f"✗ Incorrect. The correct answer is: {correct_answer_2}\n")

# ============================================================================
# QUESTION 3: The Author of the Harry Potter Series
# ============================================================================
print("Question 3: Who is the author of the Harry Potter series?")

# Step 1: Ask & Capture (Input)
user_answer_3 = input("Your answer: ")

# Step 2: Sanitize Data (Filter Pipeline)
user_answer_3 = user_answer_3.strip().lower()

# Step 3: Evaluate (The Logic Gate)
correct_answer_3 = "j.k. rowling"

# Step 4: Execute & State Management
if user_answer_3 == correct_answer_3:
    print("✓ Correct!\n")
    score += 1
else:
    print(f"✗ Incorrect. The correct answer is: {correct_answer_3}\n")

# ============================================================================
# DELIVERING RESULTS: Final Output with F-strings
# ============================================================================
print("=" * 60)
print(f"FINAL SCORE: {score:>2} / 3")
print("=" * 60)

if score == 3:
    print("Outstanding! Perfect score! 🎉")
elif score == 2:
    print("Great job! You got 2 out of 3 correct.")
elif score == 1:
    print("Good effort! You got 1 out of 3 correct.")
else:
    print("Keep practicing! You'll improve next time.")
