# Functions...

# Checks user has entered yes / no to a question
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


# Checks that the user response is not blank
def not_blank(question):
    while True:
        response = input(question).strip()

        # If the response is blank after stripping whitespace, output error
        if response == "":
            print("Sorry this can't be blank. Please try again")
        else:
            return response


# Checks user enters an integer to a given question
def num_check(question):

    while True:

        try:

            # check response for an integer
            response = int(input(question))
            return response

        # If not an integer, output error
        except ValueError:
            print("Please enter an integer")


# Calculate the ticket price based on the age
def calc_ticket_price(var_age):

    # Ticket is $7.50 for users under 16
    if var_age < 16:
        price = 7.5

    # Ticket is $10.50 for users between 16 and 64
    elif var_age <65:
        price = 10.5

    # Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Main Routine...

# Set maximum number of tickets below
MAX_TICKETS = 3
tickets_sold = 0

# Ask the user if they want to see the instructions
want_instructions = yes_no("Do you want to read the instructions? ")

# If they say yes, show the instructions
if want_instructions == "yes" or want_instructions == "y":
    print("Show Instructions...")

# If they say no, continue program
elif want_instructions == "no" or want_instructions == "n":
    print()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("Please enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break
    else:
        print(f"Your name is {name}")

    # Ask for age, call number checker
    age = num_check("Age: ")

    # Accept user age if it is >= 12 or <= 120
    if 12 <= age <= 120:
        pass

    # Check if the user is too young
    elif age < 12:
        print("Sorry you must be at least 12 to watch this movie!")
        continue
    else:
        print("?? That looks like a typo, please try again!")
        continue

    # Calculate ticket cost
    ticket_cost = calc_ticket_price(age)
    print(f"Age: {age}, Ticket Price: ${ticket_cost:.2f}")

    tickets_sold += 1

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations! You have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s.  There is {MAX_TICKETS - tickets_sold} ticket/s remaining")
