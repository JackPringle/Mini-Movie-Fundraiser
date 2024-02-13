# Functions...
def yes_no(question):

    while True:
        response = input(question).lower()

        # If the response is yes or y, return yes
        if response == "yes" or response == "y":
            return "yes"

        # If the response is no or n, return no
        elif response == "no" or response == "n":
            return "no"

        # If exit code is entered, break from loop
        elif response == "xxx":
            print(" - You have chosen to exit -")
            break

        # Other responses will trigger a helpful statement
        else:
            print("Please enter yes or no")


# Main Routine...
while True:
    # Ask the user if they want to see the instructions
    want_instructions = yes_no("Do you want to read the instructions? ")

    # If they say yes, show the instructions
    if want_instructions == "yes" or want_instructions == "y":
        print("Show Instructions...")

    # If they say no, continue program
    elif want_instructions == "no" or want_instructions == "n":
        print("program continues")
