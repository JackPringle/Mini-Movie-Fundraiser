# Functions...

# Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question)

        # If the response is blank, output error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        else:
            return response


# Main Routine...

# Ask user what their name is, call not blank function
name = not_blank("Enter your name (or 'xxx' to quit): ")

# If they have chosen to quit, output the name they chose
if name is not None:
    print(f"Your name is {name}")
