# Example for n = 5:
# *****
# *   *
# *   *
# *   *
# *****
def hollow_square(n):
    result = ""
    row = 1
    while row <= n:
        if row == 1 or row == n:
            result += '*' * n + '\n'
        else:
            result += '*' + ' ' * (n - 2) + '*' + '\n'
        row += 1
    return result.strip()  # Removes the trailing newline

print("Question 1: Hollow Square")
n = int(input("Enter side length of square: "))
print(hollow_square(n))

# 1
# 12
# 123
# 1234
def number_pattern(n):
    result = ""
    row = 1
    while row <= n:
        number = 1
        line = ""
        while number <= row:
            line += str(number)
            number += 1
        result += line + '\n'
        row += 1
    return result.strip()

print("Question 2: Number Pattern")
n = int(input("Enter your number pattern height: "))
print(number_pattern(n))

# Example: For n = 5, sum = 1 + 2 + 3 + 4 + 5 = 15
def sum_of_natural_numbers(n):
    total = 0
    count = 1
    while count <= n:
        total += count
        count += 1
    return total

print("Question 3: Sum of first n natural numbers")
n = int(input("Enter your n: "))
print(sum_of_natural_numbers(n))

# Example for n = 4:
#    *
#   ***
#  *****
# *******
def centered_star_pyramid(n):
    result = ""
    row = 1
    while row <= n:
        spaces = ' ' * (n - row)
        stars = '*' * (2 * row - 1)
        line = spaces + stars
        result += line
        if row != n:
            result += '\n'
        row += 1
    return result

print("Question 4: Centered Star Pyramid")
n = int(input("Enter your height for the pyramid: "))
print(centered_star_pyramid(n))