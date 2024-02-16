# Functions...


# Main Routine...
tickets_sold = 0

while True:

    name = input("Enter your name or 'xxx' to quit: ")

    if name == "xxx":
        break

    age = int(input("Age: "))

    if 12 <= age <= 20:
        pass
    elif age < 12:
        print("Sorry you must be atleast 12 to watch this movie!")
        continue
