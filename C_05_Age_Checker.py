# Functions...

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


# Main Routine...
tickets_sold = 0

while True:

    # Ask user for their name
    name = input("Enter your name or 'xxx' to quit: ")

    # If exit code is entered, break
    if name == "xxx":
        break

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

    tickets_sold += 1

print(f"You have sold {tickets_sold} tickets")
