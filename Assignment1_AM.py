# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):
    numbers = [num1, num2, num3]
    return max(numbers)

print("Question 1")
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
num3 = float(input("Enter your 3rd number: "))
print("Your max number is " + str(built_in_functions_max(num1, num2, num3)))

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):
    numbers = [num1, num2, num3]
    return min(numbers)
    
print("Question 2")
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
num3 = float(input("Enter your 3rd number: "))
print("Your min number is " + str(built_in_functions_min(num1, num2, num3)))

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number< 0:
        return "Your number is negative"
    elif number== 0:
        return "Your number is zero"
    else:
        return "Your number is positive"

print("Question 3")
number = float(input("Enter your number: ")
print(check_number(number))

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    total_rows = range(0, rows+1)
    for i in total_rows:
        print("*"*i)

print("Question 4: Making a Star Shape")
rows = int(input("Enter the number of rows: "))
star_shape(rows)

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    count_numbers = range(0, limit+1)                #PROBLEM HERE IN FUNCTION
    n = 0
    while n <= limit:
        if n % 3 ==0:
            print("Multiple of 3")
        else:
            print(n)

print("Question 5: Counting Multiples of 3")
limit = int(input("Enter your endpoint: "))
count_multiples_of_3(limit)

# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    # TODO: Implement this function
    pass  # Replace with your code


