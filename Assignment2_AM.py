# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
     # Convert the list to a set to remove duplicates, then sort it back into a list
    my_list_sorted = sorted(set(numbers))
    return my_list_sorted

numbers = [1, 5, -10, 70, 70, 55, 2, 5, -10, 40]    # Example list with duplicates
print("Question 1")
print(remove_duplicates_and_sort(numbers))   # Expected: sorted unique values

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []      # List to store the cumulative sums
    total = 0        # Running total
    for num in arr:     # Loop through each number in the list
        total += num     # Add the current number to the running total
        result.append(total)        # Append the current total to the result list
    return result
arr = [1, 2, 3, 4, 5]      # Example list
print("Question 2")
print(cumulative_sum(arr))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
     # Use list slicing with a step value to extract every Nth element
    return lst[::step]
lst = [10, 20, 30, 40, 50, 60]         # Example list and step value
step = 2
print("Question 3")
print(slice_every_nth(lst, step))

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):     # This function takes two lists (of the same length) and returns their dot product.
    result = 0
    for a, b in zip(list1, list2):     # zip() pairs up corresponding elements from both lists
        result += a*b                  # Multiply and add to running total
    return result

# Example vectors
list1 = (15, 35)
list2 = (40, 10)
print("Question 4")
print(dot_product(list1, list2))

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):      #assume both are 2 by 2 matrices
     # Extract individual elements from the first matrix
    a11, a12 = matrix1[0][0], matrix1[0][1]
    a21, a22 = matrix1[1][0], matrix1[1][1]
    # Extract individual elements from the second matrix
    b11, b12 = matrix2[0][0], matrix2[0][1]
    b21, b22 = matrix2[1][0], matrix2[1][1]
     # Perform standard 2x2 matrix multiplication
    return [
        [a11*b11 + a12*b21, a11*b12 + a12*b22],
        [a21*b11 + a22*b21, a21*b12 + a22*b22]
        ]
# Example matrices
matrix1 = [
    [1, 6],
    [5, 12]
]

matrix2 = [
    [4, 13],
    [31, 11]
]

print("Question 5")
print(matrix_multiplication(matrix1, matrix2))