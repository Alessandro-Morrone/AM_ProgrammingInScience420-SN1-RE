# Function 1: Check if the given number is a proper day number and return "It is a Weekday!" if it is, or "It is a Weekend!" if it is not.
def check_weekday_or_weekend(day_number):
    if day_number == 0:
        return "Not a proper day number!"
    elif day_number<=5:
        return "It is a Weekday!" 
    elif 7>=day_number>5:
        return "It is a Weekend!"
    else:
        return "invalid"

# Function 2: Check if the given number is a proper day number and return the corresponding day name.
def get_day_name(day_number):
    if day_number == 1:
        return "It is a Monday!"
    elif day_number == 2:
        return "It is a Tuesday!"
    elif day_number == 3:
        return "It is a Wednesday!"
    elif day_number == 4:
        return "It is a Thursday!"
    elif day_number == 5:
        return "It is a Friday!"
    elif day_number == 6:
        return "It is a Saturday!"
    elif day_number == 7:
        return "It is a Sunday!"
    else:
        return "Invalid"

print("Question 1 and 2")
print(check_weekday_or_weekend(day_number=(int(input("1. Enter a valid day number (1-7) : ")))))
print(get_day_name(day_number= int(input("2. Enter a valid day number (1-7) : "))))