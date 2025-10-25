# Function 1: Rotate the Array
# This function creates an array of a specified size, fills it with numbers starting from `starting_integer` and decreasing by 3,
# then rotates elements at even indices 2 positions to the left.
def rotate_the_array(array_size, starting_integer):
  # initialize an array of array_size with all zeros
   the_array = [0] * array_size

   for i in range(array_size):
      the_array[i] = starting_integer - 3*i
   print(f"Original array: {the_array}")
   for i in range(0, array_size - 2, 2):
        temp = the_array[i]
        the_array[i] = the_array[i + 2]
        the_array[i + 2] = temp
   return the_array
 
print("Question 1: Rotate the Array")
starting_integer = int(input("Enter your starting integer: "))
array_size = int(input("Enter your array size: "))
print(f"Rotated array: {rotate_the_array(array_size, starting_integer)}")