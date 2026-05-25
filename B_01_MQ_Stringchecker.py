
def string_checker(question, valid_ans):
    """Checks user enters a valid answer (full word or first letter)"""

    error = f"Please choose from {valid_ans}"

    while True:
        response = input(question).lower()

        for item in valid_ans:
            if response == item or response == item[0]:
                return item

        print(error)
        print()


def check_answer(num1, num2, question):
    """Asks math question and checks answer"""

    symbols = {
        "addition": "+",
        "subtraction": "-",
        "multiplication": "×",
        "division": "÷"
    }

    # Work out correct answer
    if question == "addition":
        correct = num1 + num2
    elif question == "subtraction":
        correct = num1 - num2
    elif question == "multiplication":
        correct = num1 * num2
    elif question == "division":
        if num2 == 0:
            print("Cannot divide by zero")
            return
        correct = num1 / num2

    # Ask question
    user_input = input(f"What is {num1} {symbols[question]} {num2}? ")

    # Check answer
    try:
        if float(user_input) == correct:
            print("Correct!")
        else:
            print(f"Wrong! The answer was {correct}")
    except ValueError:
        print("Please enter a number.")


# Main program

valid_function = ("Addition", "Subtraction", "Multiplication", "Division")

num1 = 10
num2 = 5

function = string_checker(
    "Choose: Addition (a), Subtraction (s), Multiplication (m), Division (d): ",
    valid_function
)

check_answer(num1, num2, function)

