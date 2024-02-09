show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they know how to purchase the tickets
    show_instructions = input("Do you know how to purchase tickets? ").lower()

    # If they say yes, output 'program continues'
    # If they say no, output 'display instructions'
    # If the answer is invalid, print an error.

    if show_instructions == "yes" or show_instructions == "y":
        show_instructions = "yes"
        print("program continues")

    elif show_instructions == "no" or show_instructions == "n":
        show_instructions = "no"
        print("display instructions")

    else:
        print("Please answer yes / no")
