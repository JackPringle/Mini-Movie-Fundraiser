# String checker function
def string_checker(question, valid_list, error):
    while True:

        # Ask user for string (and put string in lowercase)
        response = input(question).lower()

        # Check the string is in the valid list
        for item in valid_list:

            # Check if the response matches the entire item or just the first character
            # of the item (if it's not empty)
            if response == item or (len(item) > 0 and response == item[0]):
                return item

        # If not in valid list, print error
        print(error)
        print()


# Main routine...

# List of valid responses
payment_options = ["1", "2", "3", "4", "xxx"]
while True:
    # Ask the question, call the string checker function
    print("How would you like to pay?")
    print("Press [1] for Credit Card")
    print("Press [2] for Debit card")
    print("Press [3] for Eftpos")
    print("Press [4] for Cash")
    chosen_payment = string_checker("Chosen payment: ",
                                    payment_options, "Please enter a valid option, or 'xxx' to quit.")

# Display what the user has chosen

    if chosen_payment == "1":
        print("You have chosen to pay using Credit")
        print()

    elif chosen_payment == "2":
        print("You have chosen to pay using Debit")
        print()

    elif chosen_payment == "3":
        print("You have chosen to pay using Eftpos")
        print()

    elif chosen_payment == "4":
        print("You have chosen to pay using Cash")
        print(" * You must pay for your ticket at the theater *")
        print()

    # If the exit code is entered, break
    elif chosen_payment == "xxx":
        print("< You have chosen to quit >")
        print()
        break
