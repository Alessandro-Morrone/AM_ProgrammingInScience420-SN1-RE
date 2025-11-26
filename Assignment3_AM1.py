import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    with open(filename, "w") as f:            #Write numbers to file, each on a separate line
        for n in numbers:
            f.write(f"{n}\n")
    with open(filename, "r") as f:             #Read the file and convert each line back into an integer
        return [int(line.strip()) for line in f.readlines()]

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):
    with open(filename, "w") as f:      #Write the rows as comma-separated values
        for row in data:
            f.write(",".join(str(x) for x in row) + "\n")
    result = []           # Read the file back and convert each value to int
    with open(filename, "r") as f:
        for line in f:
            values = line.strip().split(",")
            result.append([int(x) for x in values])
    return result

# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    values = []
    with open(filename, 'r') as f:
        for x in f.read().split():
            values.append(float(x))
    return np.array(values)   

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):
    plt.plot(range(len(numbers)), numbers, marker='o', linestyle='-')
    plt.xlabel("X Axis")           #Add labels and title for clarity
    plt.ylabel("Y Axis")
    plt.title("Curve Plot")
    plt.grid(True)
    plt.show()         #Display the plot window
    return

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data, color_map='gray'):
    plt.hist(data, bins=50, density=True, color='gray', alpha=0.7)      #Histogram with density=True shows a normalized density curve
    plt.xlabel("Value")          # Add plot labels and title
    plt.ylabel("Density")
    plt.title("Density Plot")
    plt.show()            # Display the plot
    return







