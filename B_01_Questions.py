import random


# Asks random maths question
def ask_question():

    # Random numbers
    a = random.randint(1, 20)
    b = random.randint(1, 20)

    # Random operator
    operator = random.choice(["+", "-", "*", "/"])

    # Addition
    if operator == "+":
        answer = a + b

    # Subtraction
    elif operator == "-":
        answer = a - b

    # Multiplication
    elif operator == "*":
        answer = a * b

    # Division
    else:

        # Makes division answers whole numbers
        answer = a
        b = random.randint(1, 10)
        a = answer * b

        answer = a // b

    # Ask question
    user_input = input(f"What is {a} {operator} {b}? ")

    # Exit code
    if user_input.lower() == "xxx":
        return "exit"

    try:
        user_answer = int(user_input)

        if user_answer == answer:
            print("✅ Correct!")

        else:
            print(f"❌ Wrong! The answer was {answer}")

    except ValueError:
        print("Please enter a whole number.")