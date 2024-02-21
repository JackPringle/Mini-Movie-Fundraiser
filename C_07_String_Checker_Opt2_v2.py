# Functions...

# Checks that user enters a valid response (eg yes / no ,
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    while True:

        # Ask user the question
        response = input(question).lower()

        # If the response is in valid responses, return the item
        for item in valid_responses:
            if response == item[0] or response == item:
                return item

        # If not, provide error message
        print("Please enter a valid response")


# Main Routine...
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Loops the question 5 times before moving on
for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
    print("You chose", want_instructions)

# Loops the question 5 times before moving on
for case in range(0, 5):
    pay_method = string_checker("Chose a payment method (cash / credit): ", 2, payment_list)
    print("You chose", pay_method)
