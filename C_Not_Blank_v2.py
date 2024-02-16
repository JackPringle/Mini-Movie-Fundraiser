# Functions...

# Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # If the response is blank after stripping whitespace, output error
        if response == "":
            print("Sorry this can't be blank. Please try again")

        # If exit code is entered, break
        elif response == "xxx":
            print("< You have chosen to quit >")
            return response

        else:
            return response


# Main Routine...

while True:
    # Ask user what their name is, call not blank function
    name = not_blank("Enter your name (or 'xxx' to quit): ")

    # If they have chosen to quit, output the name they chose
    if name != "xxx":
        print(f"Your name is {name}")
