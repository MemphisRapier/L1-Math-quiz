import random


# Checks if user enters yes or no
def yes_no(question):

    while True:

        response = input(question).lower()

        if response in ["yes", "y"]:
            return "yes"

        elif response in ["no", "n"]:
            return "no"

        else:
            print("Please enter yes / no\n")


# Instructions that will display if user wants it
def instructions():

    print('''

📘 Instructions 📘

There will be maths questions displayed in this quiz
based on basic maths facts.

The questions may include:
➕ Addition
➖ Subtraction
✖️ Multiplication
➗ Division

None of the questions will contain negative numbers,
so don't worry 🙂🙂

Type 'xxx' anytime to quit the game.

Good luck!
''')


# Check how many rounds
def int_check(question):

    error = "Please enter an integer that is 1 or more."

    while True:

        response = input(question)

        if response == "":
            return "infinite"

        if response.lower() == "xxx":
            return "exit"

        try:
            response = int(response)

            if response < 1:
                print(error)

            else:
                return response

        except ValueError:
            print(error)


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


# Main Routine

print("➕ Welcome to the Maths Quiz ➕\n")

want_instructions = yes_no(
    "Do you want to read the instructions? "
)

if want_instructions == "yes":
    instructions()

# Choose maths type
operation = choose_question()

# Ask rounds
num_rounds = int_check(
    "\nHow many rounds would you like?\n"
    "Press <enter> for infinite mode: "
)

# Variables
mode = "regular"
rounds_played = 0
score = 0

game_history = []

# Exit if needed
if num_rounds == "exit":

    print("\nGame exited.")

else:

    # Infinite mode
    if num_rounds == "infinite":

        mode = "infinite"
        num_rounds = 5

    # Game loop
    while rounds_played < num_rounds:

        # Heading
        if mode == "infinite":

            heading = (
                f"\n♾ Round {rounds_played + 1} "
                f"(Infinite Mode) ♾"
            )

        else:

            heading = (
                f"\n⭐ Round {rounds_played + 1} "
                f"of {num_rounds} ⭐"
            )

        print(heading)

        # Ask question
        result, points, feedback = ask_question(operation)

        # Exit game
        if result == "exit":
            break

        # Update score
        score += points
        rounds_played += 1

        # Save history
        history_item = (
            f"Round {rounds_played}: {feedback}"
        )

        game_history.append(history_item)

        # Infinite mode increases rounds
        if mode == "infinite":
            num_rounds += 1

    # End game
    print("\n🏁 Game Over 🏁")

    # Statistics
    if rounds_played > 0:

        percentage = (score / rounds_played) * 100

        print("\n📊 Statistics 📊")
        print(f"Score: {score}/{rounds_played}")
        print(f"Accuracy: {percentage:.1f}%")

        # Ask for history
        see_history = yes_no(
            "\nDo you want to see game history? "
        )

        if see_history == "yes":

            print("\n📜 Game History 📜")

            for item in game_history:
                print(item)

    else:

        print(
            "😯 Oops - you did not play any rounds."
        )