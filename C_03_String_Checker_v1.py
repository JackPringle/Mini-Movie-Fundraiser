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
                print("program continues")
                return item

        # If not in valid list, print error
        print(error)
        print()


# Main routine...

# List of valid responses
payment_options = ["credit", "debit", "eftpos", "cash"]

# Ask the question, call the string checker function
chosen_payment = string_checker("How would you like to pay? 'credit', 'debit', 'eftpos', or 'cash': ",
                                "payment_options", "Please enter 'credit', 'debit', "
                                                   "eftpos', or 'cash' ")
