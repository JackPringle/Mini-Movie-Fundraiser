from datetime import date

# Get today's date
today = date.today()

# Get day, month and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Output the date and file name
heading = f"The current date is {day}/{month}/{year}"
filename = f"MMF_{day}_{month}_{year}"

# Heading
print(heading)
print(f"The filename will be {filename}.txt")