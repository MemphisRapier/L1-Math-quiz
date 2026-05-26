import random

# Type of questions that user want to display on quiz
def choose_question():

    print("\n🔴🔴Choose the type of questions you want to be quizzed on🔴🔴:")
    print("A) Addition")
    print("S) Subtraction")
    print("M) Multiplication")
    print("D) Division")

    while True:

        choice = input(
            "\nChoose: "
        ).lower()

        # Addition
        if choice in ["addition", "a"]:
            return "+"

        # Subtraction
        elif choice in ["subtraction", "s"]:
            return "-"

        # Multiplication
        elif choice in ["multiplication", "m"]:
            return "×"

        # Division
        elif choice in ["division", "d"]:
            return "÷"

        else:
            print(
                "Please enter A, S, M, D "
                "or the full word."
            )



# Asks maths question
def ask_question(function):

    a = random.randint(1, 20)
    b = random.randint(1, 20)

    # Addition
    if function == "+":
        answer = a + b

    # Subtraction (no negatives)
    elif function == "-":

        if a < b:
            a, b = b, a

        answer = a - b

    # Multiplication
    elif function == "×":
        answer = a * b

    # Division
    else:

        b = random.randint(1, 10)
        answer = random.randint(1, 10)
        a = answer * b

    # Ask question
    user_input = input(f"What is {a} {function} {b}? ")

    # Exit code
    if user_input.lower() == "xxx":
        return "exit", 0, "Exited game"

    try:

        user_answer = int(user_input)

        if user_answer == answer:

            feedback = "✅ Correct!"
            print(feedback)

            return True, 1, feedback

        else:

            feedback = f"❌ Wrong! Answer was {answer}"
            print(feedback)

            return False, 0, feedback

    except ValueError:

        feedback = "Please enter a whole number."
        print(feedback)

        return False, 0, feedback
