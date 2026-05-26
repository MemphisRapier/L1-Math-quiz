


# checks if users enter yes (y) or no (n)
def yes_no(question):


    while True:


        if want_instructions == "yes" or want_instructions == "y":
            return "yes"
        elif want_instructions == "no" or want_instructions == "n":
            return "no"
        else:
            print("please enter yes / no")

def instructions():

    print('''

📘 Instructions 📘

There will be maths questions displayed in this quiz
based on basic maths facts.

The questions may include:
➕ Addition
➖ Subtraction
✖ Multiplication
➗ Division

None of the questions will contain negative numbers,
so don't worry 🙂🙂

Type 'xxx' anytime to quit the game.

Good luck!
''')




#Main Routine Starts here

print()
print("✖️Welcome to my Math Quiz➗ ")
print()


want_instructions = yes_no("Do you want to read the instructions? ")

# checks users enter yes (y) or no (n)
if  want_instructions == "yes":
         instructions()

