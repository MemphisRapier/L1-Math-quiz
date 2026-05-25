def int_check(question):

    error = "Please enter a whole number (no decimals)."

    while True:
        response = input(question)

        try:
            # Change response into an integer
            response = int(response)

            # Return valid number
            return response

        except ValueError:
            # If user enters letters or decimals
            print(error)


# Main Routine

answer = int_check("Your answer: ")

print(f"You entered {answer}")