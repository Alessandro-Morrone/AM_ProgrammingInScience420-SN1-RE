# Function 1: Using Python built-in functions
# This function should take three numbers as input and return their max.
def built_in_functions_max(num1, num2, num3):        
    numbers = [num1, num2, num3]
    return max(numbers)              #function returns the max of the user's inputed values

print("Question 1: Maximum")                                #User inputs their 3 numbers
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
num3 = float(input("Enter your 3rd number: "))
print("Your max number is " + str(built_in_functions_max(num1, num2, num3)))            #Output of user's max number

# Function 2: Using Python built-in functions
# This function should take three numbers as input and return their min.
def built_in_functions_min(num1, num2, num3):                   
    numbers = [num1, num2, num3]
    return min(numbers)                              #function returns the min of the user's inputed values
    
print("Question 2: Minimum")                                 #User inputs their 3 numbers
num1 = float(input("Enter your 1st number: "))
num2 = float(input("Enter your 2nd number: "))
num3 = float(input("Enter your 3rd number: "))
print("Your min number is " + str(built_in_functions_min(num1, num2, num3)))                 #Output of user's min number

# Function 3: Conditional Statements – The If Statement
# This function should check if a number is positive, negative, or zero and return the corresponding message.
def check_number(number):
    if number< 0:                              #Negative numbers give an output of "Negative"
        return "Your number is negative"
    elif number== 0:
        return "Your number is zero"              #0 gives "Zero"
    else: 
        return "Your number is positive"            #Else prints Even

print("Question 3: Checking Number")
number = float(input("Enter your number: "))             #User inputs their number
print(check_number(number))                             #Output of sign of number

# Function 4: For Loop – Making a Star Shape
# This function should return a string representing a star shape.
def star_shape(rows):
    total_rows = range(0, rows+1)
    for i in total_rows:
        print("*"*i)                             #multiple * by the row number to create star shape

print("Question 4: Making a Star Shape")
rows = int(input("Enter the number of rows: "))              #user inputs the number of rows they want in the star shape
star_shape(rows)                                                        #call function star_shape(rows)

# Function 5: While Loop – Counting Multiples of 3
# This function should return a list of numbers from 1 to limit, replacing multiples of 3 with "Multiple of 3".
def count_multiples_of_3(limit):
    count = []                            #starting value of 0
    n = 1
    while n <= limit:
        if n % 3 ==0:                          #if divisible by 3, prints multiple of 3
            print("Multiple of 3")
        elif n%3 !=0:
            print(n)                 #prints other non-3 divisible numbers regularly
        n+=1                         

print("Question 5: Counting Multiples of 3")
limit = int(input("Enter your endpoint: "))                #user inputs endpoint
count_multiples_of_3(limit)                              #Function call


# Function 6: Sum of Even Numbers in a Range
# This function should calculate and return the sum of even numbers within a given range.
def sum_of_even_numbers(start, end):
    total = 0                             #starting point
    for i in range(start, end+1):
        if i % 2 !=0:                 #skips uneven numbers with continue
            continue
        elif i % 2 ==0:                  
            total += i                    #adds even numbers
    return f"the sum of even numbers in your range is {total}"

print("Question 6: Sum of even numbers in a range")            #user inputs their start and end values
start = int(input("Enter your starting number: "))
end = int(input("Enter your end point: "))
print(sum_of_even_numbers(start, end))                       #prints function result



