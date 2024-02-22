# Functions...

# Checks that user enters a valid response (eg yes / no ,
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):

    # Make a custom error message depending on question
    error = f"Please choose {valid_responses[0]} or { valid_responses[1]}"

    while True:

        # Ask the question
        response = input(question).lower()

        # If response is a valid response or the correct short version, return item
        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        # If response is no valid, print custom error
        print(error)


# Main Routine...

# Set up list of valid responses
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Loop question 5 times
for case in range(0, 5):
    want_instructions = string_checker("Do you want to read the instructions? (y/n): ", 1, yes_no_list)
    print("You chose", want_instructions)

# Loop question 5 times
for case in range(0, 5):
    pay_method = string_checker("Chose a payment method (cash / credit): ", 2, payment_list)
    print("You chose", pay_method)
