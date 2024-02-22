import pandas


# Functions...

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
    elif var_age < 65:
        price = 10.5

    # Ticket price is $6.50 for seniors (65+)
    else:
        price = 6.5

    return price


# Checks that user enters a valid response (e.g. yes / no ,
# cash / credit) based on a list of options
def string_checker(question, num_letters, valid_responses):
    # Make a custom error message depending on question
    error = f"Please choose {valid_responses[0]} or {valid_responses[1]}"

    while True:

        # Ask the question
        response = input(question).lower()

        # If response is a valid response or the correct short version, return item
        for item in valid_responses:
            if response == item[:num_letters] or response == item:
                return item

        # If response is no valid, print custom error
        print(error)


# Currency formatting function
def currency(x):
    return "${:.2f}".format(x)


# Contains instructions
def instructions():
    print('''
ℹℹℹ Instructions ℹℹℹ

Enter each persons name, age and payment method.  

When you are done, type 'xxx' for the name.

The program will output the details for the tickets you have sold.
    
    ''')


# Main Routine...

# Set maximum number of tickets below
MAX_TICKETS = 5
tickets_sold = 0

# Set up list of valid responses
yes_no_list = ["yes", "no"]
payment_list = ["cash", "credit"]

# Lists to hold ticket details
all_names = []
all_ticket_costs = []
all_surcharge = []

# Dictionary used to create data frame ie: column_name:list
mini_movie_dict = {
    "Name": all_names,
    "Ticket Price": all_ticket_costs,
    "Surcharge": all_surcharge
}

# Ask the user if they want to see the instructions
want_instructions = string_checker("\nDo you want to read the instructions? (y/n): ", 1, yes_no_list)

# If they say yes, show the instructions
if want_instructions == "yes":
    instructions()

# Loop to sell tickets
while tickets_sold < MAX_TICKETS:
    name = not_blank("\nPlease enter your name or 'xxx' to quit: ")

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

    # Get payment method
    pay_method = string_checker("Choose a payment method (Cash / Credit): ", 2, payment_list)
    print(f"you chose {pay_method}")

    # If users are paying cash they don't have to pay surcharge
    if pay_method == "cash":
        surcharge = 0
    else:
        # Calculate 5% surcharge if users are paying by credit card
        surcharge = ticket_cost * 0.05

    tickets_sold += 1

    # Add ticket name, cost and surcharge to lists
    all_names.append(name)
    all_ticket_costs.append(ticket_cost)
    all_surcharge.append(surcharge)

# Create data frame from dictionary to organise information
mini_movie_frame = pandas.DataFrame(mini_movie_dict)
mini_movie_frame = mini_movie_frame.set_index('Name')

# Calculate the total ticket cost (ticket + surcharge)
mini_movie_frame['Total'] = mini_movie_frame['Surcharge'] + mini_movie_frame['Ticket Price']

# Calculate the profit for each ticket
mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

# Calculate ticket and profit totals
total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

# Currency Formatting (uses currency function)
add_dollars = ['Ticket Price', 'Surcharge', 'Total', 'Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---- Ticket Data ----")
print()

# Output table with a ticket data
print(mini_movie_frame)
print()

print("---- Ticket Cost / Profit ----")

# Output total ticket sales and profit
print(f"Total Ticket Sales: ${total:.2f}")
print(f"Total Profit: ${profit:.2f}")
print()

# Output number of tickets sold
if tickets_sold == MAX_TICKETS:
    print("Congratulations! You have sold all the tickets")
else:
    print(f"You have sold {tickets_sold} ticket/s.  There is {MAX_TICKETS - tickets_sold} ticket/s remaining")
