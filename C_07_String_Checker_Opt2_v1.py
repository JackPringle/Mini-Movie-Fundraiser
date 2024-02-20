# Functions...
def cash_credit(question):

    while True:
        response = input(question).lower()

        # If the response is ca or cash, return cash
        if response == "cash" or response == "ca":
            return "cash"

        # If the response is cr or credit, return credit
        elif response == "credit" or response == "cr":
            return "credit"

        # If exit code is entered, break from loop
        elif response == "xxx":
            print(" - You have chosen to exit -")
            break

        # Other responses will trigger a helpful statement
        else:
            print("Please chose a valid payment method")


# Main Routine...
while True:
    # Ask the user how they want to pay
    payment_method = cash_credit("Choose a payment method (Cash or Credit): ")

    # If they say cash, tell them
    if payment_method == "cash":
        print("You have chosen to pay with cash")

    # If they say credit, tell them
    elif payment_method == "credit":
        print("You have chosen to pay using a Credit card")
