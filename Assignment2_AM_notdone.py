# Function : Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    my_list_sorted = sorted((set(numbers)))
    return my_list_sorted

numbers = [1, 5, -10, 70, 70, 55, 2, 5, -10, 40]
print("Question 1")
print(remove_duplicates_and_sort(numbers))

# Function : Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    result = []
    total = 0
    for num in arr:
        total += num
        result.append(total)
    return result
arr = [1, 2, 3, 4, 5]
print("Question 2")
print(cumulative_sum(arr))

# Function : Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]
lst = [10, 20, 30, 40, 50, 60]
step = 2
print("Question 3")
print(slice_every_nth(lst, step))

# Function : Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    result = 0
    for a, b in zip(list1, list2):
        result += a*b
    return result

list1 = (15, 35)
list2 = (40, 10)
print("Question 4")
print(dot_product(list1, list2))

# Function : Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    return [[0, 0], [0, 0]]
 
