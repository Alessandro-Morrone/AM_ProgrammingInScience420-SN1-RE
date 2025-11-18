import csv
import matplotlib.pyplot as plt
import numpy as np

# Function 1: File I/O - Writing and Reading from a Text File
# Writes a list of numbers to a file and then reads them back as a list of integers.
def write_and_read_txt(numbers, filename="numbers.txt"):
    with open(filename, "w") as f:
        for n in numbers:
            f.write(f"{n}\n")
    with open(filename, "r") as f:
        return [int(line.strip()) for line in f.readlines()]

# Function 2: File I/O - Writing and Reading from a CSV File
# Writes a list of lists to a CSV file and reads it back.
def write_and_read_csv(data, filename="data.csv"):
    with open(filename, "w", newline="") as f:
        writer= csv.writer(f)
        writer.writerows(data)
    result = []
    with open(filename, "r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            result.append(row)
    return result

# Function 3: Reading an Array from a File
# Reads a space-separated array from a text file and converts it to a NumPy array.
def read_array_from_file(filename):
    with open(filename, 'r') as f:
        content = f.read().strip()
    return np.array([float(x) for x in content.split()])

# Function 4: Plotting Data with plot() and show()
# This function plots a given list of numbers as a line graph.
def plot_data(x_values, y_values):
    plt.plot(x_values, y_values, marker='o', linestyle='-')
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Curve Plot")
    plt.grid(True)
    plt.show()
    return

# Function 5: Density Plot
# This function takes a list of numbers and plots a density plot.
def density_plot(data, color_map='gray'):
    plt.hist2d(data[:, 0], data[:, 1], bins=50, cmap=color_map, density=True)
    plt.colorbar(label="Density")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.title("Density Plot")
    plt.show()
    return



import unittest
import os
import numpy as np
import matplotlib.pyplot as plt
from Assignment3 import *
# Test case for write_and_read_txt() function
def test_write_and_read_txt():
    filename = "test_numbers.txt"
    numbers = [1, 2, 3, 4, 5]
    result = write_and_read_txt(filename, numbers)
    assert result == numbers
    os.remove(filename)

# Test case for write_and_read_csv() function
def test_write_and_read_csv():
    filename = "test_data.csv"
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = write_and_read_csv(filename, data)
    assert result == data
    os.remove(filename)

# Test case for read_array_from_file() function
def test_read_array_from_file():
    filename = "test_array.txt"
    with open(filename, 'w') as file:
        file.write("1.5 2.5 3.5 4.5 5.5")
    
    expected_array = np.array([1.5, 2.5, 3.5, 4.5, 5.5])
    result = read_array_from_file(filename)
    np.testing.assert_array_equal(result, expected_array)
    os.remove(filename)

# Test case for plot_data() function
def test_plot_data():
    numbers = [1, 2, 3, 4, 5]
    plt.figure()
    plot_data(numbers)  # This function only displays the plot, no assertion needed.

# Test case for density_plot() function
def test_density_plot():
    data = np.random.normal(0, 1, 1000)
    plt.figure()
    density_plot(data)  # This function only displays the plot, no assertion needed.

if __name__ == '__main__':
    unittest.main()