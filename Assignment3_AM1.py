import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(filename, numbers):
    with open(filename, "w") as f:
        for n in numbers:
            f.write(f"{n}\n")
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f.readlines()]

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(filename, data):
    with open(filename, "w", newline="") as f:
        writer= csv.writer(f)
        writer.writerows(data)
    result = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            result.append([int(x) for x in row])
    return result

# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return np.array([float(x) for x in content.split()])

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(numbers):
    plt.plot(range(len(numbers)), numbers, marker='o', linestyle='-')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Curve Plot")
    plt.grid(True)
    plt.show()
    return

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data, color_map='gray'):
    plt.hist(data, bins=50, density=True, color='gray')
    plt.xlabel("Value")
    plt.ylabel("Density")
    plt.title("Density Plot")
    plt.show()
    return


