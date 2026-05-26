# Check how many rounds is being displayed
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
