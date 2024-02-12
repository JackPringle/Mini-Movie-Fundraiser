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
    # Ask the user
    show_instructions = yes_no("Do you know how to purchase tickets? ")

    # If they say yes, output 'program continues'
    if show_instructions == "yes" or show_instructions == "y":
        print("program continues")

    # If they say no, output 'display instructions'
    elif show_instructions == "no" or show_instructions == "n":
        print("display instructions")
